import axios from 'axios';
import { Message } from '@arco-design/web-vue';

export const apiServerInstance = axios.create({
	baseURL: 'http://localhost:8000',
	validateStatus: status => status >= 200 && status < 300,
});

apiServerInstance.interceptors.request.use(config => {
	const { token } = JSON.parse(
		window.localStorage.getItem('user') || JSON.stringify({ token: '' }),
	);

	if (token && config.headers) {
		config.headers['X-AUTH-TOKEN'] = token;
	}

	return config;
});

apiServerInstance.interceptors.response.use(
	res => res,
	err => {
		if (axios.isCancel(err)) {
			return new Promise(() => {});
		}

		if (err.response && err.response.status) {
			// TODO:
			// 当verify jwt返回false时, 执行"退出"动作
			// 提醒并跳转到登录页
			switch (err.response.status) {
				case 500:
				case 504:
					return Promise.reject(err);

				case 404:
					return Promise.reject(err);
				default:
					return Promise.reject(err);
			}
		}

		if (err.message === 'Network Error') {
			Message.error({
				content: 'Сервер істен шықты, кейінірек қайталаңыз',
			});

			return new Promise(() => {});
		}

		console.log('\n\n开发中的未知错误!');
		console.log(err);
		console.log('\n\n\n');
		return Promise.reject(err);
	},
);
