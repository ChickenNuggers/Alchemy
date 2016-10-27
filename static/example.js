let interval; // vim:set noet sts=0 sw=4 ts=4:
var snackbarContainer = document.querySelector("#ex-snackbar")

function make_it_do_thing() {
	$.getJSON("/example").then( (data)=> {
		for (key in data) {
			$("#" + data[key].label_safe).css(
				'width', data[key].value + "%");
			$("#content-" + data[key].label_safe).html(
				data[key].value + "%");
			if ($("#ex-has-fail").css("display") == "block") {
				$("#ex-has-fail").css("display", "none");
			}
		}
	}).fail(()=>{
		clearInterval(interval);
		$("#ex-has-fail").css("display", "block");
		snackbarContainer.MaterialSnackbar.showSnackbar({
			message: "Unable to connect for module: example",
			timeout: 5000,
			actionHandler: (()=> window.location.reload()),
			actionText: "Reload"
		});
	});
}

var ex_refresh = ()=> {
	interval = setInterval(make_it_do_thing, 5000);
	make_it_do_thing();
}

ex_refresh();
