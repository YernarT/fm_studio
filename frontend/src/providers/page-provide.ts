import type { PageStateProperties } from '#/global-shared-state';

import { getLatestState, localStorage } from '@/utils';

// Get data from LocalStorage
const defaultPage: PageStateProperties = { authModalVisible: false };

// Check data
const [isValid, page] = getLatestState(
	localStorage.get('page', defaultPage),
	defaultPage,
);

if (!isValid) {
	localStorage.set('page', page);
}

export default page;
