
document.getElementById('start-btn').addEventListener('click', function() {
  start_game().then(data => {

    SetText(data);

  }).catch(error => {
    console.error(error);
  });
});

function start_game() {
  return fetch('/game')
    .then(response => {
      console.log(response);
      return response.json();
    })
    .then(data => {
      console.log(data);
      return data;
    })
    .catch(error => {
      console.error(error);
    });
}
