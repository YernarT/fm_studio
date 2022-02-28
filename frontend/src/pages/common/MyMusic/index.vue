<template>
	<div class="my-music">
		<a-tabs default-active-key="music">
			<a-tab-pane key="music" title="Музыкалар">
				<Toolbar />

				<a-list :bordered="false">
					<a-list-item v-for="music in musics">
						<MusicCard :music="music" />
					</a-list-item>
				</a-list>
			</a-tab-pane>
			<a-tab-pane key="album" title="Альбумдар">
				<Toolbar />

				<a-list :bordered="false">
					<a-list-item v-for="music in albums">
						<MusicCard :music="music" />
					</a-list-item>
				</a-list>
			</a-tab-pane>
			<a-tab-pane key="favorties" title="Таңдаулар">
				<Toolbar />

				<a-list :bordered="false">
					<a-list-item v-for="music in favorites">
						<MusicCard :music="music" />
					</a-list-item>
				</a-list>
			</a-tab-pane>
		</a-tabs>
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
import { MusicCard } from '@/components';
import Toolbar from './ToolBar/index.vue';

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
];

const favorites = [
	...musics,
	...musics,
	...musics,
	...musics,
	...musics,
	...musics,
];
const albums = musics;
</script>

<style lang="less">
.my-music {
	.arco-list-content {
		overflow: hidden auto;
	}

	.list-wrap {
		.arco-list-content {
			overflow: hidden auto;

			flex: 1 1 300px;
		}
	}
}
</style>

<style scoped lang="less">
.my-music {
	.arco-list-content {
		.arco-list-item {
			padding: 5px;
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
}
</style>
