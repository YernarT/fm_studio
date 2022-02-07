<template>
	<div class="base-layout">
		<Navbar />
		<AuthModal />

		<main class="container content">
			<slot>
				<div>Page</div>
			</slot>
		</main>

		<!-- <MusicPlayer /> -->
		<BottomNavigationBar />
	</div>
</template>

<script setup lang="ts">
import Navbar from '@/components/common/Navbar/index.vue';
import BottomNavigationBar from '@/components/common/BottomNavigationBar/index.vue';
import AuthModal from '@/components/auth/AuthModal/index.vue';
// import MusicPlayer from '@/components/common/MusicPlayer/index.vue';
</script>

<style lang="less" scoped>
.base-layout {
	width: 100%;
	height: 100vh;
	overflow: hidden;
	background-color: @backgroundColor;

	display: flex;
	flex-direction: column;

	.content {
		flex: 100% 1 1;
		overflow: hidden auto;
		margin-top: 24px;

		@media screen and (max-width: 840px) {
			margin-top: 16px;
		}

		@media screen and (max-width: 540px) {
			margin-top: 10px;
		}
	}
}
</style>

<style>
.container {
	margin: auto;
	width: 100%;
}

@media screen and (max-width: 1080px) {
	.container {
		padding: 0 50px;
	}
}

@media screen and (min-width: 980px) {
	.container {
		width: 980px;
	}
}

@media screen and (max-width: 540px) {
	.container {
		padding: 0 10px;
	}
}
</style>
