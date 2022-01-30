/**
 * Check the contents of localStorage are out of date or incorrect
 */

interface Conditions {
	[key: string]: any;
}

export default function getLatestState<T extends Conditions>(
	dataFromStorage: T,
	defaultData: T,
): [boolean, T] {
	let fromStorageKeys = Object.keys(dataFromStorage);
	let defaultKeys = Object.keys(defaultData);

	if (fromStorageKeys.length !== defaultKeys.length) {
		return [false, defaultData];
	}

	fromStorageKeys.forEach(key => {
		if (!defaultKeys.includes(key)) {
			return [false, defaultData];
		}
	});

	return [true, dataFromStorage];
}
