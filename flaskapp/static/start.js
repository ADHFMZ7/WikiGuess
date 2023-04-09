

function start_game() {

	fetch('/game')
	.then(response=> {
		console.log(response);
		return response.json();
	})

}
