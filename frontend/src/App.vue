<template>
	<div class="layout-container">
		<router-view></router-view>
	</div>
</template>

<script setup lang="ts">
import { reactive, provide } from 'vue';

const page = reactive({ authModalVisible: false });
provide('$page', page);
</script>

<!-- private style -->
<style scoped lang="less">
.layout-container {
	width: 100%;
	height: 100vh;
	overflow: hidden;
	background-color: @backgroundColor;

	display: flex;
	flex-direction: column;
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
