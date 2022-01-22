<template>
	<div class="container navbar">
		<a-menu
			class="navbar__menu"
			mode="horizontal"
			theme="dark"
			:default-selected-keys="['0']"
		>
			<a-menu-item class="menu__item" key="0">Музыкалар</a-menu-item>
			<a-menu-item class="menu__item" key="1">Менің музыкам</a-menu-item>
			<a-menu-item class="menu__item" key="2">Көшбасшылар тақтасы</a-menu-item>
		</a-menu>

		<div class="navbar__tools">
			<a-input-search class="desktop-search" placeholder="Іздеу" />
			<a-button class="auth-btn" type="text" size="medium"
				>Кіру / Тіркелу</a-button
			>
		</div>

		<a-input-search class="mobile-search" placeholder="Іздеу" />
	</div>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const pathname = router.currentRoute.value.path;

function cd(path: string): void {
	router.push(path);
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
