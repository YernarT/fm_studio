<template>
	<div class="container navbar">
		<a-menu
			class="navbar__menu"
			mode="horizontal"
			theme="dark"
			:selected-keys="selectedKeys"
			@menu-item-click="handleMenuItemClick"
		>
			<a-menu-item class="menu__item" key="/">Музыкалар</a-menu-item>
			<a-menu-item class="menu__item" key="/my-music">
				Менің музыкам
			</a-menu-item>
			<a-menu-item class="menu__item" key="/leaderboard">
				Көшбасшылар тақтасы
			</a-menu-item>
		</a-menu>

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
			<a-dropdown v-if="user.token" class="user-menu" @select="handle">
				<a-button>
					<img :src="user.avatar" alt="avatar" class="avatar" />
					<icon-down
				/></a-button>
				<template #content>
					<a-doption>
						<template #icon>
							<icon-user />
						</template>
						<template #default>Жеке кабинет</template>
					</a-doption>
					<a-doption>
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

let selectedKeys = [router.currentRoute.value.path];

function handleMenuItemClick(key: string) {
	router.push(key);
}

function handle(v: any) {
	console.log(v);
}
</script>

<style lang="less" scoped>
.navbar {
	user-select: none;

	display: flex;
	align-items: center;

	&__menu {
		background-color: @backgroundColor;
		.menu__item {
			background-color: @backgroundColor;
		}
	}

	&__tools {
		display: flex;
		align-items: center;

		@media screen and (max-width: 840px) {
			margin-top: 20px;
			margin-left: 40px;
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

		.avatar {
			width: 40px;
			height: 40px;
			object-fit: cover;

			border-radius: 50%;
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
		align-items: flex-start;
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
