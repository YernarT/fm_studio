<template>
	<div class="container navbar">
		<nav class="navbar__menu">
			<li
				:class="{
					menu__item: true,
					'menu__item--active': router.currentRoute.value.path === '/',
				}"
				@click="handleNavItemClick('/')"
			>
				Музыкалар
			</li>
			<li
				:class="{
					menu__item: true,
					'menu__item--active': router.currentRoute.value.path === '/my-music',
				}"
				@click="handleNavItemClick('/my-music')"
			>
				Менің музыкам
			</li>
			<li
				:class="{
					menu__item: true,
					'menu__item--active':
						router.currentRoute.value.path === '/leaderboard',
				}"
				@click="handleNavItemClick('/leaderboard')"
			>
				Көшбасшылар тақтасы
			</li>
		</nav>

		<div class="navbar__tools">
			<a-input-search class="desktop-search" placeholder="Іздеу" allow-clear />
			<a-button
				v-if="!user.token"
				class="auth-btn"
				@click="page.authModalVisible = true"
				type="text"
				size="medium"
			>
				Кіру / Тіркелу
			</a-button>
			<a-dropdown v-if="user.token" @select="handleUserAction" trigger="hover">
				<a-button class="user-actions">
					<img :src="user.avatar" alt="avatar" class="avatar" />
				</a-button>
				<template #content>
					<a-doption value="profile">
						<template #icon>
							<icon-user />
						</template>
						<template #default>Жеке кабинет</template>
					</a-doption>
					<a-doption value="logout">
						<template #icon>
							<icon-export />
						</template>
						<template #default>Шығу</template>
					</a-doption>
				</template>
			</a-dropdown>
		</div>

		<a-input-search class="mobile-search" placeholder="Іздеу" allow-clear />
	</div>
</template>

<script lang="ts" setup>
import type {
	UserStateProperties,
	PageStateProperties,
} from '#/global-shared-state';

import { inject } from 'vue';
import { useRouter } from 'vue-router';
import { authorizationRequiredPaths } from '@/routes';
import { localStorage } from '@/utils';

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

function handleNavItemClick(to: string) {
	router.push(to);
}

function handleUserAction(v: string) {
	switch (v) {
		case 'profile':
			router.push('/profile');
			break;
		case 'logout':
			user.username = '';
			user.phone = '';
			user.is_admin = false;
			user.birthday = null;
			user.gender = false;
			user.avatar = '';
			user.create_time = null;
			user.token = '';
			localStorage.set('user', user);

			authorizationRequiredPaths.forEach(path => {
				if (router.currentRoute.value.path === path) {
					router.push('/');
					return;
				}
			});
			break;
		default:
			return;
	}
}
</script>

<style lang="less" scoped>
.navbar {
	user-select: none;

	display: flex;
	align-items: center;
	padding-top: 10px;
	padding-bottom: 10px;

	&__menu {
		background-color: @backgroundColor;

		display: flex;
		align-items: center;
		gap: 20px;

		.menu__item {
			color: rgba(255, 255, 255, 0.4);
			background-color: @backgroundColor;

			display: flex;
			justify-content: center;
			align-items: center;

			position: relative;
			cursor: pointer;
			padding: 10px 0;

			transition: color 0.35s ease;

			&::after {
				content: '';
				position: absolute;
				bottom: 0;
				left: 50%;
				transform: translateX(-50%);

				width: 0;
				height: 3px;
				background-color: rgb(var(--primary-6));
				transition: width 0.35s ease;
			}

			&:hover,
			&--active {
				color: #fff;

				&::after {
					width: 100%;
				}
			}
		}
	}

	&__tools {
		margin-left: auto;
		display: flex;
		align-items: center;

		@media screen and (max-width: 840px) {
			margin-top: 20px;
			margin-left: 0;
		}

		.desktop-search {
			width: 160px;

			@media screen and (max-width: 840px) {
				width: 295px;
			}
		}

		.auth-btn {
			background-color: transparent;
		}

		.user-actions {
			height: 100%;
			background-color: transparent;

			.avatar {
				width: 36px;
				height: 36px;
				object-fit: cover;

				border-radius: 50%;
			}
		}
	}

	.mobile-search {
		display: none;

		@media screen and (max-width: 540px) {
			display: flex;
		}
	}

	@media screen and (max-width: 840px) {
		flex-direction: column;
		align-items: center;
	}

	@media screen and (max-width: 540px) {
		padding: 10px;

		&__menu,
		&__tools {
			display: none;
		}
	}
}
</style>
