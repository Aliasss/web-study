// 사용변수
const GAME_TIME = 9;
let score = 0;   //변경이 가능하도록. 그리고 0으로 초기화
let time = GAME_TIME;
let isPlaying = false;
let timeInterval;
let words = [];
let checkInterval;

const wordInput = document.querySelector('.word-input');
const wordDisplay = document.querySelector('.word-display');
const scoreDisplay = document.querySelector('.score');
const timeDisplay = document.querySelector('.time');
const button = document.querySelector('.button');
// clg : console.log()   snippet

// 화면이 랜더링 됐을 때 바로 선언해주는 게 좋음
init();

function init() {
    buttonChange("게임로딩중...");  // 데이터를 다 받아오면 '게임시작'으로 버튼 바뀜
    getWords();
    wordInput.addEventListener('input', checkMatch)
}

// 게임 실행
function run() {
    if (isPlaying) {
        return;      // 게임이 실행되지 않음
    }
    isPlaying = true;
    time = GAME_TIME;
    wordInput.focus();
    scoreDisplay.innerText = 0;
    timeInterval = setInterval(countDown, 1000);
    checkInterval = setInterval(checkStatus, 50);  // 50microseconds마다 cehckStatus 실행
    buttonChange('게임중')
}

function checkStatus() {
    if (!isPlaying && time === 0) {  // isPlaying이 아니고(게임 중이 아니면) 시간이 0초라면 
        buttonChange("게임시작")
        clearInterval(checkInterval)
    }
}
// 단어 불러오기
function getWords() {
    // Make a request for a user with a given ID
    axios.get('https://random-word-api.herokuapp.com/word?number=200')
        .then(function (response) {
            // 너무 긴 단어는 걸러내기
            response.data.forEach((word)=>{
                if(word.length < 10) {
                    words.push(word);
                }
            })
            buttonChange('게임시작');
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
}

// 단어 일치 체크
function checkMatch() {
    if (wordInput.value.toLowerCase() === wordDisplay.innerText.toLowerCase()) {
        wordInput.value = "";   // 입력창 초기화
        if (!isPlaying) {
            return;     // 점수 올라가면 안됨. return을 주면 밑에 있는 내용은 실행 안되고 함수 종료됨
        }
        score++;
        scoreDisplay.innerText = score;
        time = GAME_TIME;
        const randomIndex = Math.floor(Math.random() * words.length);
        wordDisplay.innerText = words[randomIndex];

    }
}


function countDown() {
    time > 0 ? time-- : isPlaying = false;  // time이 0보다 작거나 같을 경우 게임이 종료가 됨
    if (!isPlaying) {
        clearInterval(timeInterval);   //clearInterval 실행
    }
    timeDisplay.innerText = time;
}

function buttonChange(text) {
    button.innerText = text;
    text === '게임시작' ? button.classList.remove('loading') : button.classList.add('loading')
}