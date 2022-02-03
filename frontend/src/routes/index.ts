import type { RouteRecordRaw } from 'vue-router';

import { createRouter, createWebHistory } from 'vue-router';
import { Message } from '@arco-design/web-vue';
import { user } from '@/providers';

const routes: Array<RouteRecordRaw> = [
	{
		path: '/',
		name: 'Home',
		component: () =>
			import(/* webpackChunkName: "Home" */ '@/pages/common/Home/index.vue'),
	},
	{
		path: '/my-music',
		name: 'MyMusic',
		component: () =>
			import(
				/* webpackChunkName: "MyMusic" */ '@/pages/common/MyMusic/index.vue'
			),
		beforeEnter: (_, __, next) => {
			if (!user.token) {
				Message.warning('авторизация қажет етеді');
				return;
			}
			next();
		},
	},
	{
		path: '/leaderboard',
		name: 'Leaderboard',
		component: () =>
			import(
				/* webpackChunkName: "Leaderboard" */ '@/pages/common/Leaderboard/index.vue'
			),
	},
	{
		path: '/profile',
		name: 'Profile',
		component: () =>
			import(
				/* webpackChunkName: "Profile" */ '@/pages/common/Profile/index.vue'
			),
		beforeEnter: (_, __, next) => {
			if (!user.token) {
				Message.warning('авторизация қажет етеді');
				return;
			}
			next();
		},
	},
	{
		path: '/404',
		name: 'PageNotFound',
		component: () =>
			import(
				/* webpackChunkName: "Profile" */ '@/pages/common/PageNotFound/index.vue'
			),
	},
	{
		path: '/:pathMatch(.*)',
		redirect: '/404',
	},
];

export const authorizationRequiredPaths: Array<string> = [
	'/my-music',
	'/profile',
];

const router = createRouter({
	history: createWebHistory('/'),
	routes,
});

export default router;
