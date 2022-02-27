import { apiServerInstance } from './ajax';

export interface AuthData {
	phone: string;
	password: string;
}

// Login
export const reqLog = (data: AuthData) =>
	apiServerInstance.post('/api/user/login/', data);

// Register
export const reqReg = (data: AuthData) =>
	apiServerInstance.post('/api/user/register/', data);
