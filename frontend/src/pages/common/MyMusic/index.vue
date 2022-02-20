<template>
	<div class="my-music">
		<a-list
			:gridProps="{ gutter: [24, 48], span: middle ? 24 : 12 }"
			:bordered="false"
		>
			<a-list-item>
				<a-list>
					<template #header>
						<span class="list-header">Музыкалар</span>
					</template>
					<a-list-item v-for="music in musics">
						<a-card hoverable :key="music.id">
							<div class="music">
								<img :src="music.author.avatar" alt="author" class="author" />
								<div class="info">
									<h1 class="name">{{ music.name }}</h1>
									<span class="create-time">{{ music.createTime }}</span>
								</div>
								<icon-play-circle-fill class="play-btn" />
							</div>
						</a-card>
					</a-list-item>
				</a-list>
			</a-list-item>
			<a-list-item>
				<a-list>
					<template #header>
						<span class="list-header">Таңдаулар</span>
					</template>
					<a-list-item v-for="music in favorites">
						<a-card hoverable :key="music.id">
							<div class="music">
								<img :src="music.author.avatar" alt="author" class="author" />
								<div class="info">
									<h1 class="name">{{ music.name }}</h1>
									<span class="create-time">{{ music.createTime }}</span>
								</div>
								<icon-play-circle-fill class="play-btn" />
							</div>
						</a-card>
					</a-list-item>
				</a-list>
			</a-list-item>
			<a-list-item>
				<a-list>
					<template #header>
						<span class="list-header">Альбумдар</span>
					</template>
					<a-list-item v-for="music in albums">
						<a-card hoverable :key="music.id">
							<div class="music">
								<img :src="music.author.avatar" alt="author" class="author" />
								<div class="info">
									<h1 class="name">{{ music.name }}</h1>
									<span class="create-time">{{ music.createTime }}</span>
								</div>
								<icon-play-circle-fill class="play-btn" />
							</div>
						</a-card>
					</a-list-item>
				</a-list>
			</a-list-item>
		</a-list>
	</div>
</template>

<script setup lang="ts">
import type { UserStateProperties } from '#/global-shared-state';

import { inject, ref, reactive, shallowRef } from 'vue';
import { useRouter } from 'vue-router';
import { useBreakpoints } from '@vueuse/core';
import { localStorage } from '@/utils';
import { reqEdit, reqEditAvatar } from '@/api/user-api';
import { Message } from '@arco-design/web-vue';

const breakpoints = useBreakpoints({
	middle: 880,
});

const middle = breakpoints.smaller('middle');

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

const musics = [
	{
		id: 1,
		name: 'Rap God',
		createTime: '2001-10-03',
		author: user,
	},
	{
		id: 2,
		name: 'Rap God Remix',
		createTime: '2010-06-11',
		author: user,
	},
	{
		id: 3,
		name: 'Godzilla',
		createTime: '2019-03-17',
		author: user,
	},
];

const favorites = musics;
const albums = musics;
</script>

<style scoped lang="less">
.my-music {
	.list-header {
		color: #fff;
		font-size: 1.36rem;
	}

	.arco-list-content {
		.arco-list-item {
			padding: 0;
		}
	}

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

		.play-btn {
			width: 36px;
			height: 36px;
			cursor: pointer;

			margin-left: auto;

			display: flex;
			justify-content: center;
			align-items: center;
		}
	}
}
</style>
