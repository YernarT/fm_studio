export interface UserStateProperties {
	username: string;
	phone: string;
	is_admin: boolean;
	birthday: Date | null;
	gender: boolean;
	avatar: string;
	create_time: Date | null;
}

export interface PageStateProperties {
	authModalVisible: boolean;
}
