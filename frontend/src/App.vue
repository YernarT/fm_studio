<template>
	<BaseLayout>
		<a-config-provider :locale="enUS">
			<router-view></router-view>
		</a-config-provider>
	</BaseLayout>
</template>

<script setup lang="ts">
import { reactive, provide } from 'vue';
import { useEventListener } from '@vueuse/core';
// For initialization only
import { user, page } from '@/providers';
import { localStorage } from '@/utils';
import BaseLayout from '@/components/common/BaseLayout/index.vue';
import enUS from '@arco-design/web-vue/es/locale/lang/en-us';

// Provides global shared state
provide('$user', reactive(user));
provide('$page', reactive(page));

// Save data to LocalStorage
useEventListener(window, 'beforeunload', () => {
	localStorage.set('user', user);
});
</script>
