<template>
	<a-modal
		v-model:visible="page.authModalVisible"
		:okText="title"
		:footer="false"
		hide-cancel
		unmount-on-close
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
				<a-button type="text" html-type="submit" long>{{ title }}</a-button>
			</a-form-item>
		</a-form>
	</a-modal>
</template>

<script setup lang="ts">
import type {
	UserStateProperties,
	PageStateProperties,
} from '#/global-shared-state';

import { inject, shallowRef, ref, computed } from 'vue';
import { reqLog, reqReg } from '@/api/auth-api';

const user: UserStateProperties = inject('$user', {
	username: '',
	phone: '',
	is_admin: false,
	birthday: null,
	gender: false,
	avatar: '',
	create_time: null,
});
const page: PageStateProperties = inject('$page', { authModalVisible: false });

const title = shallowRef('Кіру');
const another = computed(() => (title.value === 'Кіру' ? 'Тіркелу' : 'Кіру'));

function jump2Another() {
	title.value = another.value;
}

// auth form data
const authFormData = ref({
	phone: '',
	password: '',
});

// handle auth form
function handleSubmit(values: any) {
	if (title.value === 'Кіру') {
		reqLog(values)
			.then(res => {
				console.log('vue res: ', res);
			})
			.catch(err => {
				console.log('vue err: ', err);
			});

		return;
	}

	reqReg(values)
		.then(res => {
			console.log(res);
		})
		.catch(err => {
			console.log(err);
		});
}
</script>
