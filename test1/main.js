

function init() {


document.getElementById("bouton1").onclick = function(event) {
	let request = new XMLHttpRequest();
	request.open("GET", "http://localhost:8000/bouton1");
	request.send();
	request.onload = () => {
		let jsonresponse = JSON.parse(request.response);
		$("#bouton1").text(jsonresponse.bouton1.content + " (" + jsonresponse.bouton1.clicks + ")");
	}
}

document.getElementById("bouton2").onclick = function(event) {
	let request = new XMLHttpRequest();
	request.open("GET", "http://localhost:8000/bouton2");
	request.send();
	request.onload = () => {
		let jsonresponse = JSON.parse(request.response);
		$("#bouton2").text(jsonresponse.bouton2.content + " (" + jsonresponse.bouton2.clicks + ")");
	}
}
// SOME JQUERY CODE FOR THE BUTTONS HERE...

// URL FOR BUTTON1 : /bouton1
// URL FOR BUTTON2 : /bouton2

// BUTTON1 WHEN CLICKED WILL BECOME : Voici le Bouton 1 (1)
// BUTTON1 WHEN CLICKED AGAIN WILL BECOME : Voici le Bouton 1 (2)
// AND SO ON... ie: BUTTON1 WHEN CLICKED number of clicks TIMES WILL BECOME : Voici le Bouton 1 (number of clicks)

// BUTTON2 WHEN CLICKED WILL BECOME : Et ceci est le Bouton 2 (1)
// BUTTON2 WHEN CLICKED AGAIN WILL BECOME : Et ceci est le Bouton 2 (2)
// AND SO ON... ie: BUTTON2 WHEN CLICKED number of clicks TIMES WILL BECOME : Et ceci est le Bouton 2 (number of clicks)

}

