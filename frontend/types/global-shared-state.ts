export interface UserStateProperties {
	username: string;
	phone: string;
	is_admin: boolean;
	birthday: string | null;
	gender: boolean;
	avatar: string;
	create_time: string | null;
	token: '';
}

export interface PageStateProperties {
	authModalVisible: boolean;
}
