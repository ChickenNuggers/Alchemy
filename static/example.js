setInterval(function() {
	$.getJSON("/example").then( (data)=> {
		for (key in data) {
			$("#" + data[key].label_safe).css(
				'width', data[key].value + "%");
			$("#content-" + data[key].label_safe).html(
				data[key].value + "%");
		}
	});
}, 5000);
