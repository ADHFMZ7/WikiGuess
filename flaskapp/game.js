function SetText(json) {
    // Generate a random integer between 1 and 10
    right = document.getElementById("rightbox");
    left = document.getElementById("leftbox");
    right.style.display = "block";
    left.style.display = "block";
    if (json[rand] == 1) {
        right.innerHTML = json['wiki'];
        left.innerHTML = json['gpt'];
    } else {
        right.innerHTML = json['gpt'];
        left.innerHTML = json['wiki'];
    }

    article = document.getElementById("article");
    article.innerHTML = json['title'];

    subsection = document.getElementById("subsection");
    subsection.innerHTML = json['subsection'];
}

function ClickRight() {
    if (json[rand] == 1) {
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

function ClickLeft() {
    if (json[rand] == 0) {
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
