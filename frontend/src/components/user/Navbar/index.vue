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
				class="auth-btn"
				@click="page.authModalVisible = true"
				type="text"
				size="medium"
			>
				Кіру / Тіркелу
			</a-button>
		</div>

		<a-input-search class="mobile-search" placeholder="Іздеу" allow-clear />
	</div>
</template>

<script lang="ts" setup>
import { inject } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const page = inject('$page', { authModalVisible: false });

let selectedKeys = [router.currentRoute.value.path];

function handleMenuItemClick(key: string) {
	router.push(key);
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
