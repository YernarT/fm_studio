<template lang="">
	<a-card hoverable>
		<div class="music">
			<img :src="music.author.avatar" alt="author" class="author" />
			<div class="info">
				<h1 class="name">{{ music.name }}</h1>
				<span class="create-time">{{ music.createTime }}</span>
			</div>
			<icon-plus class="add-to-favorites" />
			<icon-play-circle-fill class="play-btn" />
		</div>
	</a-card>
</template>

<script setup lang="ts">
const props = defineProps({
	music: Object,
});

console.log(props);
</script>

<style lang="less" scoped>
.music {
	display: flex;
	align-items: center;

	.author {
		width: 36px;
		height: 36px;
		object-fit: cover;

		box-shadow: 0 0 2px #000;
		border-radius: 50%;
		cursor: pointer;
	}

	.info {
		margin-left: 12px;

		display: flex;
		flex-direction: column;
		justify-content: space-between;

		.name {
			font-size: 1.12rem;
			font-weight: bold;
			color: #000;
		}

		.create-time {
			font-size: 0.8rem;
			color: rgb(107, 107, 107);
		}
	}

	.play-btn,
	.add-to-favorites {
		width: 36px;
		height: 36px;
		cursor: pointer;

		display: flex;
		justify-content: center;
		align-items: center;
	}

	.add-to-favorites {
		margin-left: auto;
		margin-right: 8px;
	}
}
</style>
