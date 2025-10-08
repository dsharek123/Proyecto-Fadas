let timeLeft = 30 * 60;
let timerInterval = null;
let isRunning = false;

const timerDisplay = document.getElementById('timer');
const startpause = document.getElementById('startpause');
const reset = document.getElementById('reset');

function updateDisplay() {
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;
    timerDisplay.textContent = 
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startPauseTimer() {
    if (!isRunning) {
        isRunning = true;
        startpause.textContent = "Pausar";
        timerInterval = setInterval(() => {
            if (timeLeft > 0) {
                timeLeft--;
                updateDisplay();
            } else {
                clearInterval(timerInterval);
                isRunning = false;
                alert("⏰ ¡Tiempo terminado!");
                startpause.textContent = "Iniciar";
            }
        }, 1000);
    } else {
        clearInterval(timerInterval);
        isRunning = false;
        startpause.textContent = "Reanudar";
    }
}

function resetTimer() {
    clearInterval(timerInterval);
    isRunning = false;
    timeLeft = 30 * 60;
    updateDisplay();
    startpause.textContent = "Iniciar";
}

if (startpause && reset) {
    startpause.addEventListener('click', startPauseTimer);
    reset.addEventListener('click', resetTimer);
    updateDisplay();
}
