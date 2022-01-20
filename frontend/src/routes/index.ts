import { createRouter, createWebHistory } from 'vue-router';

const routes: Array<any> = [
	{
		path: '/',
		name: 'Home',
		auth: false,
		component: () =>
			import(/* webpackChunkName: "Home" */ 'pages/user/Home/index.vue'),
		beforeEnter: (to: object, from: object, next: Function): any => {
			console.log(to, from);
			next();
		},
	},
	{
		path: '/my-music',
		name: 'MyMusic',
		auth: true,
		component: () =>
			import(/* webpackChunkName: "MyMusic" */ 'pages/user/MyMusic/index.vue'),
		beforeEnter: (to: object, from: object, next: Function): any => {
			console.log(to, from);
			next();
		},
	},
	{
		path: '/leaderboard',
		name: 'Leaderboard',
		auth: false,
		component: () =>
			import(
				/* webpackChunkName: "Leaderboard" */ 'pages/user/Leaderboard/index.vue'
			),
		beforeEnter: (to: object, from: object, next: Function): any => {
			console.log(to, from);
			next();
		},
	},
	{
		path: '/profile',
		name: 'Profile',
		auth: true,
		component: () =>
			import(/* webpackChunkName: "Profile" */ 'pages/user/Profile/index.vue'),
		beforeEnter: (to: object, from: object, next: Function): any => {
			console.log(to, from);
			next();
		},
	},
];

const router = createRouter({
	history: createWebHistory('/'),
	routes,
});

export default router;
