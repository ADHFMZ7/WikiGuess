function SetText(json) {
    // Generate a random integer between 1 and 10
    console.log(json["gpt"])
    let right = document.getElementById("rightbox");
    let left = document.getElementById("leftbox");
    right.style.display = "block";
    left.style.display = "block";
    if (json['rand'] == 1) {
        right.innerHTML = json['wiki'];
        left.innerHTML = json['gpt'];
    } else {
        right.innerHTML = json['gpt'];
        left.innerHTML = json['wiki'];
    }

    let article = document.getElementById("article");
    article.innerHTML = json['title'];

    let subsection = document.getElementById("subsection");
    subsection.innerHTML = json['subsection'];
}

function ClickRight(json) {
    if (json['rand'] == 1) {
        //load correct animation
        //get new json
        //SetText()
        //update score
    } else {
        //load wrong animations
        //show restart button
        //update highscore
    }
}

function ClickLeft(json) {
    if (json['rand'] == 0) {
        //load correct animation
        //get new json
        //SetText()
        //update score
    } else {
        //load wrong animations
        //show restart button
        //update highscore
    }
}

document.getElementById('start-btn').addEventListener('click', function() {
    document.getElementById("button_animate").className = "animate slideUp animate--slow";
    document.getElementById("start-btn").id = "";
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
  
