<template>
	<div class="profile">
		<a-avatar class="avatar-wrap" :size="80">
			<img :src="user.avatar" alt="avatar" />
			<template #trigger-icon>
				<IconEdit />
			</template>
		</a-avatar>
	</div>
</template>

<script setup lang="ts">
import type { UserStateProperties } from '#/global-shared-state';

import { inject } from 'vue';

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
</script>

<style scoped lang="less">
.profile {
	height: 100%;
	display: flex;
	flex-direction: column;

	.avatar-wrap {
		align-self: center;
	}
}
</style>

<style>
.avatar-wrap .arco-avatar-trigger-icon-button {
	width: 30px;
	height: 30px;
	line-height: 30px;
}

.avatar-wrap .arco-avatar-trigger-icon-button svg {
	font-size: 14px;
}
</style>
