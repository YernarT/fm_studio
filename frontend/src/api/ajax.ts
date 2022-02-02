import axios from 'axios';

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
		if (err.response && err.response.status) {
			let { status } = err.response;
			// TODO:
			// 当verify jwt返回false时, 执行"退出"动作
			// 提醒并跳转到登录页

			if (status >= 500) {
				return Promise.reject({
					message: 'сервер құлап қалды...',
				});
			} else if (status >= 400 && status < 500) {
				return Promise.reject(err.response.data);
			} else {
				return Promise.reject({
					message: 'белгісіз жағдай, кейінірек қайталаңыз',
				});
			}
		}

		if (err.message === 'Network Error') {
			return Promise.reject({
				message: 'сервер істен шықты, кейінірек қайталаңыз',
			});
		}

		console.log('\n\n\n开发中的未知错误!');
		console.log(err);
		console.log('\n\n\n');
		return Promise.reject({
			message: 'сервер істен шықты, кейінірек қайталаңыз',
		});
	},
);
