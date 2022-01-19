<template>
	<div class="layout-container">
		<router-view></router-view>
	</div>
</template>

<script setup lang="ts"></script>

<!-- private style -->
<style scoped lang="less">
.layout-container {
	width: 100%;
	height: 100vh;
	overflow: hidden;
	background-color: @backgroundColor;
}
</style>

<!-- public style -->
<style lang="less">
.container {
	margin: auto;
	width: 100%;

	@media screen and (min-width: 980px) {
		width: 980px;
	}
}
</style>
