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
];

const router = createRouter({
	history: createWebHistory('/'),
	routes,
});

export default router;
