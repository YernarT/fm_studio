<template>
	<Navbar />
	<div class="container home-page">
		<div class="page-content">
			<h1>我的音乐</h1>
		</div>
	</div>
	<!-- <MusicPlayer /> -->
	<BottomNavigationBar />
</template>

<script setup lang="ts">
import Navbar from 'components/user/Navbar/index.vue';
import BottomNavigationBar from 'components/user/BottomNavigationBar/index.vue';
import MusicPlayer from 'components/user/MusicPlayer/index.vue';
</script>

<style scoped lang="less">
.home-page {
	padding: 20px 10px 0 40px;
	height: 100%;

	@media screen and (max-width: 540px) {
		padding: 0 10px;
		height: calc(100% - 54px);
	}

	.page-content {
		height: 100%;
	}
}
</style>
