import { createRouter, createWebHistory } from 'vue-router';

const routes = [
	{
		path: '/',
		name: 'Home',
		auth: false,
		component: () =>
			import(/* webpackChunkName: "Home" */ '@/pages/user/Home/index.vue'),
		// beforeEnter: (to, from, next) => {
		// 	next();
		// },
	},
	{
		path: '/my-music',
		name: 'MyMusic',
		auth: true,
		component: () =>
			import(/* webpackChunkName: "MyMusic" */ '@/pages/user/MyMusic/index.vue'),
		// beforeEnter: (to, from, next) => {
		// 	next();
		// },
	},
	{
		path: '/leaderboard',
		name: 'Leaderboard',
		auth: false,
		component: () =>
			import(
				/* webpackChunkName: "Leaderboard" */ '@/pages/user/Leaderboard/index.vue'
			),
		// beforeEnter: (to, from, next) => {
		// 	next();
		// },
	},
	{
		path: '/profile',
		name: 'Profile',
		auth: true,
		component: () =>
			import(/* webpackChunkName: "Profile" */ '@/pages/user/Profile/index.vue'),
		// beforeEnter: (to, from, next) => {
		// 	next();
		// },
	},
];

const router = createRouter({
	history: createWebHistory('/'),
	routes,
});

export default router;
