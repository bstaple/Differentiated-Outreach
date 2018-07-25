window.onload = document_ready;

function send_request(destinationUrl, callbackFunction, parameters) {
    let xmlHttp = new XMLHttpRequest();
    console.log("sending_request");
    xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState === 4) {
                let result = JSON.parse(xmlHttp.responseText);
                display_data(result);
            }
        };
    xmlHttp.open("POST", "/hostpage");
    xmlHttp.send();

}

function handleload(){
	sendRequest("/messages", function(result){
		var messageText = '';
		for(var i = 0; i < result.messages.length; i++){
			messageText += '<div class="message">';
			messageText += '<span class="messageemail">' + result.messages[i].email;
			messageText += " said ";
			messageText += '<span class="messagetext">' + result.messages[i].text;
			messageText += '</div>';
		}
		console.log("code works");
		document.getElementById("messagearea").innerHTML = messageText;
	}, new Object());
}

function handlesend(){
		var parameters = new Object();
	parameters["text"] = document.getElementById("textfield").value;
	sendRequest("/add", function(result){
		document.getElementById("textfield").value = "";
		handleload();
	}, parameters);

	setInterval(handleload, 1000);

}
