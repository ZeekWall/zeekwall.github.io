const yn = document.querySelector(".yn");
const currentScore = document.querySelector(".current-score");

let win = null
let stros = 10;
let opp = 10;

if (win === true){
    yn.innerHTML = 'YES!'
    yn.style.color = 'green'
    currentScore.innerHTML = `${stros} to ${opp}`
}
else if (win === false){
    yn.innerHTML = 'NO'
    yn.style.color = 'red'
    currentScore.innerHTML = `${stros} to ${opp}`
}
else if (win === null){
    yn.innerHTML = 'Not playing currently...'
    yn.style.fontSize = '35px';
    currentScore.innerHTML = ``
}