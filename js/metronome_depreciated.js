let isPlaying = false;
let timer;
let audio = new Audio('../sounds/metronome-click2.wav');

document.getElementById('startStopButton').addEventListener('click', toggleMetronome);

function toggleMetronome() {
    isPlaying = !isPlaying;

    if (isPlaying) {
        const bpmInput = document.getElementById('bpmInput');
        const bpm = bpmInput.value || 110; // Default BPM is 110

        startMetronome(bpm);
    } else {
        stopMetronome();
    }
}

function startMetronome(bpm) {
    const interval = 60000 / bpm; // Calculate interval in milliseconds
    playClick(); // Play the first click immediately

    timer = setInterval(playClick, interval);
}

function stopMetronome() {
    clearInterval(timer);
}

function playClick() {
    audio.currentTime = 0; // Reset the audio to the beginning
    audio.play();
}
