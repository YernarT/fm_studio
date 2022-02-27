import { apiServerInstance } from './ajax';

export interface EditFormData {
	phone?: string;
	username?: string;
	password?: string;
	birthday?: string;
	gender?: string;
}

// Edit
export const reqEdit = (data: EditFormData) =>
	apiServerInstance.put('/api/user/edit/', data);

// Edit Avatar
export const reqEditAvatar = (data: FormData) =>
	apiServerInstance.post('/api/user/edit/avatar/', data, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
	});
