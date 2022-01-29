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
			'#': pathResolve('./types'),
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
