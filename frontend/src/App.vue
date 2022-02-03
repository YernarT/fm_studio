<template>
	<BaseLayout>
		<router-view></router-view>
	</BaseLayout>
</template>

<script setup lang="ts">
import { reactive, provide } from 'vue';
import { useEventListener } from '@vueuse/core';
// For initialization only
import { user, page } from '@/providers';
import { localStorage } from '@/utils';
import BaseLayout from '@/components/common/BaseLayout/index.vue';

// Provides global shared state
provide('$user', reactive(user));
provide('$page', reactive(page));

// Save data to LocalStorage
useEventListener(window, 'beforeunload', () => {
	localStorage.set('user', user);
});
</script>
