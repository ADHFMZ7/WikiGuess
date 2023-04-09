

function start_game() {

	fetch('/game')
	.then(response=> {
		console.log(response.json());
		return response.json();
	})

}
