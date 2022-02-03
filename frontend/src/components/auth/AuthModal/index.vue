<template>
	<a-modal
		v-model:visible="page.authModalVisible"
		:okText="title"
		:footer="false"
		hide-cancel
		unmount-on-close
		modal-class="auth-modal"
	>
		<template #title>
			<h3 @click="jump2Another" style="cursor: pointer">
				{{ title }} /
				<span style="color: rgb(var(--primary-6))">{{ another }}</span>
			</h3>
		</template>
		<a-form
			:model="authFormData"
			layout="vertical"
			@submit-success="handleSubmit"
		>
			<a-form-item
				field="phone"
				label="Телефон нөмер"
				validate-trigger="input"
				:rules="[
					{ required: true, message: 'бос қалмау керек' },
					{
						minLength: 11,
						message: '11 орынды болу керек',
					},
					{
						maxLength: 11,
						message: '11 орынды болу керек',
					},
				]"
			>
				<a-input v-model="authFormData.phone" />
			</a-form-item>
			<a-form-item
				field="password"
				label="Құпия сөз"
				validate-trigger="input"
				:rules="[
					{ required: true, message: 'бос қалмау керек' },
					{
						minLength: 4,
						message: '4 орыннан кем болмау керек',
					},
					{
						maxLength: 60,
						message: '60 орыннан көп болмау керек',
					},
				]"
			>
				<a-input-password v-model="authFormData.password" />
			</a-form-item>

			<a-form-item>
				<a-button
					type="primary"
					html-type="submit"
					long
					:loading="authReqLoading"
					:disabled="authReqLoading"
					>{{ title }}</a-button
				>
			</a-form-item>
		</a-form>
	</a-modal>
</template>

<script setup lang="ts">
import type {
	UserStateProperties,
	PageStateProperties,
} from '#/global-shared-state';

import { inject, shallowRef, reactive, computed } from 'vue';
import { Message } from '@arco-design/web-vue';
import { reqLog, reqReg } from '@/api/auth-api';
import { localStorage } from '@/utils';
import '@/assets/style/auth-modal.css';

const user: UserStateProperties = inject('$user', {
	username: '',
	phone: '',
	is_admin: false,
	birthday: null,
	gender: false,
	avatar: '',
	create_time: null,
	token: '',
});
const page: PageStateProperties = inject('$page', { authModalVisible: false });

const title = shallowRef('Кіру');
const another = computed(() => (title.value === 'Кіру' ? 'Тіркелу' : 'Кіру'));

function jump2Another() {
	title.value = another.value;
}

// auth form data
const authFormData = reactive({
	phone: '',
	password: '',
});

const authReqLoading = shallowRef(false);

// handle auth form
function handleSubmit(values: any) {
	authReqLoading.value = true;

	if (title.value === 'Кіру') {
		reqLog(values)
			.then(res => {
				authFormData.phone = '';
				authFormData.password = '';

				const { data } = res;
				const { user: _user } = data;

				user.username = _user.username;
				user.phone = _user.phone;
				user.is_admin = _user.is_admin;
				user.birthday = _user.birthday;
				user.gender = _user.gender;
				user.avatar = _user.avatar;
				user.create_time = _user.create_time;
				user.token = data.token;
				localStorage.set('user', user);

				Message.success(data.message);
				authReqLoading.value = false;
				page.authModalVisible = false;
			})
			.catch(err => {
				Message.error(err.message);
				authReqLoading.value = false;
			});

		return;
	}

	reqReg(values)
		.then(res => {
			authFormData.phone = '';
			authFormData.password = '';

			const { data } = res;
			const { user: _user } = data;

			user.username = _user.username;
			user.phone = _user.phone;
			user.is_admin = _user.is_admin;
			user.birthday = _user.birthday;
			user.gender = _user.gender;
			user.avatar = _user.avatar;
			user.create_time = _user.create_time;
			user.token = data.token;
			localStorage.set('user', user);

			Message.success(data.message);
			authReqLoading.value = false;
			page.authModalVisible = false;
		})
		.catch(err => {
			Message.error(err.message);
			authReqLoading.value = false;
		});
}
</script>
