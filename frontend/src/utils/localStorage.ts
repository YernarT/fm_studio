/**
 * Serving for localized storage
 */
import type {
	UserStateProperties,
	PageStateProperties,
} from '#/global-shared-state';

export default {
	get<T extends UserStateProperties | PageStateProperties>(
		key: 'user' | 'page',
		defaultValue: T,
	): T {
		return JSON.parse(
			window.localStorage.getItem(key) || JSON.stringify(defaultValue),
		);
	},

	set<T extends UserStateProperties | PageStateProperties>(
		key: 'user' | 'page',
		value: T,
	): void {
		window.localStorage.setItem(key, JSON.stringify(value));
	},

	clear(): void {
		window.localStorage.clear();
	},
};
