url = 'http://127.0.0.1:5000/api/'

function send_login(type) {
	user = document.getElementById('username').value;
	pass = document.getElementById('Password').value;
	console.log(user)
	console.log(pass)
	if (user != '' && pass != '') {
		u = url + type
		d = { "username":user, "password": pass}

		$.ajax({
			url: u,
	        data: JSON.stringify(d),
	        method: "POST",
	        contentType: "application/json",
			dataType: "text",
	        success: function(result) { 
	        	warn = document.getElementById('warning');
	        	logi = document.getElementById('login');
	        	r = JSON.parse(result)
	        	console.log(r)
	        	if (r.loggedin) {
	        		logi.style.display = "block"
	        		warn.style.display = "none"
	        	} else {
	        		warn.style.display = "block"
	        		logi.style.display = "none"
	        	}
	    }, error: function(xhr) {
	    	console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText)
	    }});
	} else {
		obj = document.getElementById('warning');
		obj.style.display = "block";
	}
}

function send_create(type) {
	user = document.getElementById('username').value;
	pass = document.getElementById('Password').value;
	console.log(user)
	console.log(pass)
	if (user != '' && pass != '') {
		u = url + type
		d = { "username":user, "password": pass}

		$.ajax({
			url: u,
	        data: JSON.stringify(d),
	        method: "POST",
	        contentType: "application/json",
			dataType: "text",
	        success: function(result) { 
	        	warn = document.getElementById('warning');
	        	logi = document.getElementById('create');
	        	r = JSON.parse(result)
	        	console.log(r)
	        	if (r.created) {
	        		logi.style.display = "block"
	        		warn.style.display = "none"
	        	} else {
	        		warn.style.display = "block"
	        		logi.style.display = "none"
	        	}
	    }, error: function(xhr) {
	    	console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText)
	    }});
	} else {
		obj = document.getElementById('warning');
		obj.style.display = "block";
	}
}

function send_share(type) {
	user = document.getElementById('username').value;
	pass = document.getElementById('Password').value;
	recp = document.getElementById('recip').value;
	file = document.getElementById('file_share').value;
	console.log(user)
	console.log(pass)
	if (user != '' && pass != '' && recp != '' && file != ' ') {
		u = url + type
		d = { "username":user, "password": pass, "file": file, "recipient": recp}

		$.ajax({
			url: u,
	        data: JSON.stringify(d),
	        method: "POST",
	        contentType: "application/json",
			dataType: "text",
	        success: function(result) { 
	        	warn = document.getElementById('warning2');
	        	logi = document.getElementById('done');
	        	r = JSON.parse(result)
	        	console.log(r)
	        	if (r.status) {
	        		logi.style.display = "block"
	        		warn.style.display = "none"
	        	} else {
	        		warn.style.display = "block"
	        		logi.style.display = "none"
	        	}
	    }, error: function(xhr) {
	    	console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText)
	    }});
	} else {
		obj = document.getElementById('warning2');
		obj.style.display = "block";
	}
}


function file_upload() {
	user = document.getElementById('username').value;
	pass = document.getElementById('Password').value;
	if (user != '' && pass != '') {
		var form_data = new FormData($('#upload-file')[0]);
		u = url + 'browser_upload'

	    $.ajax({
	        type: 'POST',
	        url: u,
	        username: user, 
	        password: pass,
	        data: form_data,
	        contentType: false,
	        cache: false,
	        processData: false,
	        success: function(data) {

	            console.log('Success!');
	        },
	        error: function(data) {

	        }
	    });
	}
}

function file_download() {
	user = document.getElementById('username').value;
	pass = document.getElementById('Password').value;
	file = document.getElementById('file').value;
	if (user != '' && pass != '') {
		var form_data = new FormData($('#upload-file')[0]);
		u = url + 'browser_download'
		d = { "username":user, "password": pass, "file": file}
	    $.ajax({
			url: u,
	        data: JSON.stringify(d),
	        method: "POST",
	        contentType: "application/json",
			dataType: "text",
	        success: function(result) { 
	        	warn = document.getElementById('warning');
	        	logi = document.getElementById('login');
	        	r = JSON.parse(result)
	        	console.log(r)
	        	if (r.loggedin) {
	        		logi.style.display = "block"
	        		warn.style.display = "none"
	        	} else {
	        		warn.style.display = "block"
	        		logi.style.display = "none"
	        	}
	    }, error: function(xhr) {
	    	console.log('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText)
	    }});
	}
}