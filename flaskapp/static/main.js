var score = 0;


function SetText(json) {
    // Generate a random integer between 1 and 10
    let right = document.getElementById("rightBox");
    let left = document.getElementById("leftBox");
    let middle = document.getElementById("middleBox");

    // make middle h1 title
    // make middle h2 header
    // make middle h2 score
    

    right.style.display = "block";
    left.style.display = "block";
    if (json['rand'] == 1) {
        right.innerHTML = json['wiki'];
        left.innerHTML = json['gpt'];
    } else {
        right.innerHTML = json['gpt'];
        left.innerHTML = json['wiki'];
    }

    let article = document.getElementById("titlez");
    article.innerHTML = json['title'];

   //let subsection = document.getElementById("subsection");
    //subsection.innerHTML = json['subsection'];
}

function ClickRight(json) {
    if (json['rand'] == 1) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score++;
        json = start_game();
    } else {
        //load wrong animations
        //show restart button
        //update highscore
        post_score(score);
        score = 0;
        json = start_game();
    }
}

function ClickLeft(json) {
    if (json['rand'] == 0) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score++;
        json = start_game()
    } else {
        //load wrong animations
        //show restart button
        //update highscore
        post_score(score)
        score = 0;
        json = start_game()
    }
}

document.getElementById('start-btn').addEventListener('click', function() {
    document.getElementById("button_animate").className = "animate slideUp animate--slow";
    //document.getElementById("start-btn").id = "";
    document.getElementById("start-btn").style.display = "none";
    document.getElementById("titlez").className = "title";
    document.getElementById("titlez").style.display = "true";


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


function post_score(num) {
  return fetch('/game', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({score: num})
  })
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

  
