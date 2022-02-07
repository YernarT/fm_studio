<template>
	<div class="profile">
		<a-avatar class="avatar-wrap" :size="80" @click="avatarRef.click()">
			<img :src="user.avatar" alt="avatar" />
			<template #trigger-icon>
				<IconEdit />
			</template>
		</a-avatar>
		<input
			ref="avatarRef"
			type="file"
			name="avatar"
			accept="image/png, image/jpeg"
			class="avatar-input"
			@change="handleChangeAvatar"
		/>

		<a-button
			v-show="editAvatarBtnVisible"
			type="primary"
			:loading="editAvatarBtnLoading"
			:disabled="editAvatarBtnLoading"
			@click="handleEditAvatar"
			>Өзгерту</a-button
		>
		<a-divider v-show="editAvatarBtnVisible" />

		<a-form
			class="edit-form"
			layout="vertical"
			:model="editFormData"
			@submit-success="handleEdit"
		>
			<a-form-item
				field="phone"
				label="Телефон нөмер"
				validate-trigger="input"
				:rules="[
					{ required: false },
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
				<a-input v-model="editFormData.phone" />
			</a-form-item>

			<a-form-item
				field="username"
				label="Атау"
				validate-trigger="input"
				:rules="[
					{ required: false },
					{
						minLength: 2,
						message: '2 орыннан аз болмау керек',
					},
					{
						maxLength: 24,
						message: '24 орыннан көп болмау керек',
					},
				]"
			>
				<a-input v-model="editFormData.username" />
			</a-form-item>

			<a-form-item
				field="password"
				label="Құпия сөз"
				validate-trigger="input"
				:rules="[
					{ required: false },
					{
						minLength: 4,
						message: '4 орыннан аз болмау керек',
					},
					{
						maxLength: 60,
						message: '60 орыннан көп болмау керек',
					},
				]"
			>
				<a-input-password v-model="editFormData.password" />
			</a-form-item>

			<a-form-item
				field="birthday"
				label="Туған күн"
				validate-trigger="input"
				:rules="[{ required: false }]"
			>
				<a-date-picker v-model="editFormData.birthday" />
			</a-form-item>

			<a-form-item field="gender" label="Жыныс">
				<a-radio-group v-model="editFormData.gender">
					<a-radio :value="false">Қыз</a-radio>
					<a-radio :value="true">Ұл</a-radio>
				</a-radio-group>
			</a-form-item>

			<a-form-item>
				<a-button
					type="primary"
					html-type="submit"
					long
					:loading="editBtnLoading"
					:disabled="editBtnLoading"
					>Өзгерту</a-button
				>
			</a-form-item>
		</a-form>

		<a-divider />

		<a-typography-text class="create-time">
			Тіркелген уақыт:
			<a-typography-text code> {{ user.create_time }} </a-typography-text>
		</a-typography-text>

		<a-button
			@click="handleLogout"
			class="logout-btn"
			type="primary"
			status="danger"
			>Шығу</a-button
		>
	</div>
</template>

<script setup lang="ts">
import type { UserStateProperties } from '#/global-shared-state';

import { inject, ref, reactive, shallowRef } from 'vue';
import { useRouter } from 'vue-router';
import { localStorage } from '@/utils';
import { reqEdit, reqEditAvatar } from '@/api/user-api';
import { Message } from '@arco-design/web-vue';

const router = useRouter();
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

const avatarRef = ref();
const editAvatarBtnVisible = shallowRef(false);
const editAvatarBtnLoading = shallowRef(false);
function handleChangeAvatar() {
	if (avatarRef.value.files[0].size >= 500000) {
		Message.warning('сурет пішімі 60kb-дан артық болмау керек');
		return;
	}

	editAvatarBtnVisible.value = true;
}

function handleEditAvatar() {
	editAvatarBtnLoading.value = true;
	const data = new FormData();
	data.append('avatar', avatarRef.value.files[0]);

	reqEditAvatar(data)
		.then(res => {
			let {
				data: { message, user: _user },
			} = res;

			user.avatar = _user.avatar;
			Message.success(message);
			editAvatarBtnLoading.value = false;
		})
		.catch(err => {
			Message.error(err.message);
			editAvatarBtnLoading.value = false;
		});
}

const editFormData = reactive({
	phone: user.phone,
	username: user.username,
	password: '',
	birthday: user.birthday,
	gender: user.gender,
});
const editBtnLoading = shallowRef(false);
function handleEdit() {
	editBtnLoading.value = true;

	let reqData = Object.fromEntries(
		Object.entries(editFormData).filter(
			([key, value]) => Boolean(value) || key === 'gender',
		),
	);

	reqEdit(reqData)
		.then(res => {
			let {
				data: { user: _user, message },
			} = res;

			user.username = _user.username;
			user.phone = _user.phone;
			user.birthday = _user.birthday;
			user.gender = _user.gender;

			editBtnLoading.value = false;
			Message.success(message);
		})
		.catch(err => {
			editBtnLoading.value = false;
			Message.error(err.message);
		});
}

function handleLogout() {
	user.username = '';
	user.phone = '';
	user.is_admin = false;
	user.birthday = null;
	user.gender = false;
	user.avatar = '';
	user.create_time = null;
	user.token = '';
	localStorage.set('user', user);

	router.push('/');
}
</script>

<style scoped lang="less">
.profile {
	max-width: 520px;
	margin: auto;
	height: 100%;
	overflow: inherit;
	display: flex;
	flex-direction: column;

	.avatar-wrap {
		align-self: center;
		margin-bottom: 20px;
	}

	.avatar-input {
		display: none;
	}

	.create-time {
		color: #f2f3f5;
		margin-bottom: 20px;
	}

	.logout-btn {
		margin-bottom: 20px;
	}
}
</style>

<style lang="less">
.avatar-wrap {
	.arco-avatar-trigger-icon-button {
		width: 30px;
		height: 30px;
		line-height: 30px;
	}
}

.avatar-wrap {
	.arco-avatar-trigger-icon-button {
		svg {
			font-size: 14px;
		}
	}
}

.edit-form {
	.arco-form-item-label,
	.arco-radio-label {
		color: #f2f3f5;
	}

	.arco-picker {
		width: 100%;
	}
}
</style>
