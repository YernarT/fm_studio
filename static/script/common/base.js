function showAlert(message, type) {
	let wrapper = document.createElement("div");
	wrapper.innerHTML =
		'<div class="alert alert-' +
		type +
		' alert-dismissible" role="alert">' +
		message +
		'<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';

	alertMsgContainer.append(wrapper);
}

function detectionResponseCodeType(code) {
	switch (code) {
		case 0:
			return "success";
		case 1:
			return "warning";
		case 2:
			return "danger";
		default:
			return null;
	}
}
