<template>
	<div class="container navbar">
		<a-menu mode="horizontal" theme="dark" :default-selected-keys="['0']">
			<a-menu-item key="0">Музыкалар</a-menu-item>
			<a-menu-item key="1">Менің музыкам</a-menu-item>
			<a-menu-item key="2">Көшбасшылар тақтасы</a-menu-item>
		</a-menu>

		<a-input-search placeholder="Іздеу" />
		<a-button type="text" size="medium">Кіру / Тіркелу</a-button>
	</div>
</template>

<script setup lang="ts"></script>

<style lang="less" scoped>
.navbar {
	user-select: none;

	display: flex;
	align-items: center;

	.arco-menu,
	.arco-menu-item {
		background-color: @backgroundColor;
	}

	.arco-input-wrapper {
		width: 200px;
		height: max-content;

		margin-right: 10px;
	}
}
</style>
