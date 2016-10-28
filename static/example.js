"use strict";
var snackbarContainer = document.querySelector("#ex-snackbar");
let ws = new WebSocket('ws://' + window.location.host + '/example');

ws.onmessage = function(message) {
	data = JSON.parse(message.data);
	for (key in data) {
		$("#" + data[key].label_safe).css(
			'width', data[key].value + "%");
		$("#content-" + data[key].label_safe).html(
			data[key].value + "%");
		if ($("#ex-has-fail").css("display") == "block") {
			$("#ex-has-fail").css("display", "none");
		}
	}
}

function fail() {
	$("#ex-has-fail").css("display", "block");
	snackbarContainer.MaterialSnackbar.showSnackbar({
		message: "Unable to connect for module: example",
		timeout: 5000,
		actionHandler: (()=> window.location.reload()),
		actionText: "Reload"
	});
}

ws.onerror = fail;
ws.onclose = fail;
