<template>
	<ul class="bottom-navigation-bar">
		<li
			:class="{ item: true, 'item-active': pathname === '/' }"
			@click="cd('/')"
		>
			<icon-compass class="icon" />
			<span class="name">Музыкалар</span>
		</li>
		<li
			:class="{ item: true, 'item-active': pathname === '/my-music' }"
			@click="cd('/my-music')"
		>
			<icon-music class="icon" />
			<span class="name">Менің музыкам</span>
		</li>
		<li
			:class="{ item: true, 'item-active': pathname === '/leaderboard' }"
			@click="cd('/leaderboard')"
		>
			<icon-trophy class="icon" />
			<span class="name">Көшбасшылар тақтасы</span>
		</li>
		<li
			:class="{ item: true, 'item-active': pathname === '/profile' }"
			@click="cdProfile"
		>
			<icon-user class="icon" />
			<span class="name">Жеке кабинет</span>
		</li>
	</ul>
</template>

<script lang="ts" setup>
import type {
	UserStateProperties,
	PageStateProperties,
} from '#/global-shared-state';

import { inject } from 'vue';
import { useRouter } from 'vue-router';

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
const page: PageStateProperties = inject('$page', { authModalVisible: false });
const pathname = router.currentRoute.value.path;

function cd(path: string) {
	router.push(path);
}

function cdProfile() {
	if (user.token) {
		cd('/profile');
		return;
	}

	page.authModalVisible = true;
}
</script>

<style lang="less" scoped>
.bottom-navigation-bar {
	display: none;
	height: 54px;
	padding: 0 10px;
	background-color: darken(@backgroundColor, -2%);

	.item {
		display: flex;
		flex-direction: column;
		align-items: center;

		width: calc(100% / 4 - 15px);
		padding: 5px;

		.icon,
		.name {
			color: @primaryColor;
		}

		.icon {
			font-size: 1.5rem;
		}
		.name {
			font-size: 12px;
			width: 100%;
			white-space: nowrap;
			overflow: hidden;
			text-overflow: ellipsis;
			text-align: center;
		}
	}

	.item-active {
		.icon,
		.name {
			color: rgba(255, 255, 255, 0.6);
		}
	}

	@media screen and (max-width: 540px) {
		display: flex;
		justify-content: space-evenly;
		align-items: center;
	}
}
</style>
