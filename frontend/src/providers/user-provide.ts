import type { UserStateProperties } from '#/global-shared-state';

import { getLatestState, localStorage } from '@/utils';

// Get data from LocalStorage
const defaultUser: UserStateProperties = {
	username: '',
	phone: '',
	is_admin: false,
	birthday: null,
	gender: false,
	avatar: '',
	create_time: null,
};

// Check data
const [isValid, user] = getLatestState(
	localStorage.get('user', defaultUser),
	defaultUser,
);

if (!isValid) {
	localStorage.set('user', user);
}

export default user;
