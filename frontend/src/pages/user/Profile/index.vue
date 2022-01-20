<template>
	<Navbar />
	<div class="container profile-page">
		<div class="page-content">
			<h1>profile page</h1>
		</div>
	</div>
</template>

<script setup lang="ts">
import Navbar from 'components/user/Navbar/index.vue';
</script>

<style scoped lang="less">
.profile-page {
	padding: 20px 40px;
	padding-right: 10px;
	height: 100%;

	.page-content {
		background-color: darkblue;
		height: 100%;
	}
}
</style>
