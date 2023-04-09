var score = 0;
var g_json;

function SetText(json) {
    console.log("PRINTING STUFF NOW PRINTING")
    // Generate a random integer between 1 and 10
    let right = document.getElementById("rightBox");
    let left = document.getElementById("leftBox");
    let middle = document.getElementById("middleBox");

    let hs = document.getElementById("hs");
    hs.innerHTML = "Highscore: " + g_json['highscore'];

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

    let subsection = document.getElementById("subhead");
    //subsection.innerHTML = json['subsection'];

    //let score = document.getElementById("score");
    subsection.innerHTML = "Score: " + score;
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
      document.getElementById("subhead").className = "fadeIn";
    }, 1850);
    setTimeout(function() {
      document.getElementById("leftBox").className = "fadeIn";
    }, 1900);
    setTimeout(function() {
      document.getElementById("rightBox").className = "fadeIn";
    }, 1850);
    


    start_game().then(data => {
        g_json = data;
        SetText(data);
  
    }).catch(error => {
      console.error(error);
    });
  });
 
  document.getElementById('leftBox').addEventListener('click', function() {
    if (g_json['randNum'] == 0) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score++;
        //alert("correct!!");
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
        alert("Incorrect!!");
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
    if (g_json['randNum'] == 1) {
        //load correct animation
        //get new json
        //SetText()
        //update score
        score++;
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
        alert("Incorrect!!");
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

  
