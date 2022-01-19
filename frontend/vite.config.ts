import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { resolve } from 'path';

const pathResolve = (dir: string) => resolve(__dirname, dir);

// https://vitejs.dev/config/
export default defineConfig({
	server: {
		host: '0.0.0.0',
		open: true,
	},
	plugins: [vue()],
	resolve: {
		alias: {
			'@': pathResolve('./src'),
			'pages': pathResolve('./src/pages'),
			'components': pathResolve('./src/components'),
			'assets': pathResolve('./src/assets'),
			'store': pathResolve('./src/store'),
			'configs': pathResolve('./src/configs'),
		},
	},
	css: {
		preprocessorOptions: {
			less: {
				javascriptEnabled: true,
				additionalData: `@import "${pathResolve(
					'src/assets/style/variables.less',
				)}";`,
			},
		},
	},
});
