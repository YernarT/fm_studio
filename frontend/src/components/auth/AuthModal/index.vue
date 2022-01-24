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
			:model="loginFormData"
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
				<a-input v-model="loginFormData.phone" />
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
				<a-input-password v-model="loginFormData.password" />
			</a-form-item>

			<a-form-item>
				<a-button type="text" html-type="submit" long>{{ title }}</a-button>
			</a-form-item>
		</a-form>
	</a-modal>
</template>

<script setup lang="ts">
import { inject, shallowRef, ref, computed, watchEffect } from 'vue';

const page = inject('$page', { authModalVisible: false });

const title = shallowRef('Кіру');
const another = computed(() => (title.value === 'Кіру' ? 'Тіркелу' : 'Кіру'));

function jump2Another(): void {
	title.value = another.value;
}

watchEffect(() => {
	console.log(title.value);
});

// login form data
const loginFormData = ref({
	phone: '',
	password: '',
});

// handle login form
function handleSubmit(values: any) {
	console.log(values);
}
</script>
