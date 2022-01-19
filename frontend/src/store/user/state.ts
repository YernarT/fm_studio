export interface UserState {
	username: string;
	phone: string;
	is_admin: boolean;
	birthday: Date | null;
	gender: boolean;
	avatar: string;
	create_time: Date;
}

const state: UserState = {
	username: '',
	phone: '',
	is_admin: false,
	birthday: null,
	gender: false,
	avatar: '',
	create_time: new Date(),
};

export default state;
