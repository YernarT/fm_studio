import { createApp } from 'vue';

// Arco UI
import ArcoVue from '@arco-design/web-vue';
import '@arco-design/web-vue/dist/arco.css';

import App from './App.vue';
import router from './routes';
import store from 'store/index';

// Common style
import 'assets/style/reset.css';
import 'assets/style/customize.less';

const app = createApp(App);

app.use(ArcoVue).use(store).use(router);

app.mount('#app');
