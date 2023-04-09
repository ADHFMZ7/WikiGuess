var score = 0;
var g_json;

function SetText(json) {
    console.log("PRINTING STUFF NOW PRINTING")
    // Generate a random integer between 1 and 10
    let right = document.getElementById("rightBox");
    let left = document.getElementById("leftBox");
    let middle = document.getElementById("middleBox");

    // make middle h1 title
    // make middle h2 header
    // make middle h2 score
    

    right.style.display = "block";
    left.style.display = "block";
    if (g_json['rand'] == 1) {
        right.innerHTML = g_json['wiki'];
        left.innerHTML = g_json['gpt'];
    } else {
        right.innerHTML = g_json['gpt'];
        left.innerHTML = g_json['wiki'];
    }

    let article = document.getElementById("titlez");
    article.innerHTML = g_json['title'];

   //let subsection = document.getElementById("subsection");
    //subsection.innerHTML = json['subsection'];

    //let score = document.getElementById("score");
    //score.innerHTML = "Score: " + score;
}

function ClickRight() {
    console.log("CLICKED RIGHT");
    if (g_json['rand'] == 1) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score = score + 1;
        post_score(score);
        g_json = start_game();
        g_json.then(data => {
            SetText(data);
        });
    } else {
        //load wrong animations
        //show restart button
        //update highscore
        post_score(score);
        score = 0;
        g_json = start_game();
    }
}

document.getElementById('start-btn').addEventListener('click', function() {
    document.getElementById("button_animate").className = "animate slideUp animate--slow";
    //document.getElementById("rightBox_").id="rightBox";
    //document.getElementById("leftBox_").id="leftBox";
    //document.getElementById("start-btn").id = "";
    document.getElementById("start-btn").style.display = "none";
    setTimeout(function() {
      document.getElementById("titlez").className = "title";
    }, 1200);
    setTimeout(function() {
      document.getElementById("leftBox").className = "fadeIn";
    }, 1700);
    setTimeout(function() {
      document.getElementById("rightBox").className = "fadeIn";
    }, 1650);
    


    start_game().then(data => {
        g_json = data;
        SetText(data);
  
    }).catch(error => {
      console.error(error);
    });
  });
 
  document.getElementById('leftBox').addEventListener('click', function() {
    if (g_json['rand'] == 0) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score = score + 1;
        post_score(score)
            start_game().then(data => {
        g_json = data;
        SetText(data);
  
    }).catch(error => {
      console.error(error);
    });

    } else {
        //load wrong animations
        //show restart button
        //update highscore
        post_score(score)
        score = 0;
        start_game().then(data => {
            g_json = data;
            SetText(data);
      
        }).catch(error => {
          console.error(error);
        });
    }

  });

  document.getElementById('rightBox').addEventListener('click', function() {
    console.log("CLICKED RIGHT");
    if (g_json['rand'] == 1) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score = score + 1;
        post_score(score);
        start_game().then(data => {
            g_json = data;
            SetText(data);
      
        }).catch(error => {
          console.error(error);
        });
    } else {
        //load wrong animations
        //show restart button
        //update highscore
        post_score(score);
        score = 0;
        start_game().then(data => {
            g_json = data;
            SetText(data);
      
        }).catch(error => {
          console.error(error);
        });
    }


    
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
    body: JSON.stringify({'score': num})
  })
  .then(data => {
    console.log(data);
    return data;
  })
  .catch(error => {
    console.error(error);
  });
}

  
