import { createApp } from 'vue';

// Arco UI
import ArcoVue from '@arco-design/web-vue';
import ArcoVueIcon from '@arco-design/web-vue/es/icon';
import '@arco-design/web-vue/dist/arco.css';

import App from './App.vue';
import router from './routes';

// Common style
import '@/assets/style/reset.css';
import '@/assets/style/customize.less';
import '@/assets/style/arco.css';

const app = createApp(App);

app.use(ArcoVue).use(ArcoVueIcon).use(router);

app.mount('#app');
