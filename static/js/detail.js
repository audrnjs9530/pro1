(function () {
    const audio = document.getElementById('native-audio');
    const playBtn = document.getElementById('play-btn');
    const iconPlay = document.getElementById('icon-play');
    const iconPause = document.getElementById('icon-pause');
    const progressFill = document.getElementById('progress-fill');
    const progressWrap = document.getElementById('progress-wrap');
    const timeCurrent = document.getElementById('time-current');
    const timeTotal = document.getElementById('time-total');
    const volumeSlider = document.getElementById('volume-slider');

    if (!audio || !playBtn) {
        return;
    }

    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
    }

    audio.addEventListener('loadedmetadata', () => {
        timeTotal.textContent = formatTime(audio.duration);
    });

    audio.addEventListener('timeupdate', () => {
        if (!audio.duration) {
            return;
        }

        const percent = (audio.currentTime / audio.duration) * 100;
        progressFill.style.width = `${percent}%`;
        timeCurrent.textContent = formatTime(audio.currentTime);
    });

    playBtn.addEventListener('click', () => {
        if (audio.paused) {
            audio.play();
            iconPlay.style.display = 'none';
            iconPause.style.display = '';
            return;
        }

        audio.pause();
        iconPlay.style.display = '';
        iconPause.style.display = 'none';
    });

    audio.addEventListener('ended', () => {
        iconPlay.style.display = '';
        iconPause.style.display = 'none';
        progressFill.style.width = '0%';
    });

    progressWrap.addEventListener('click', (event) => {
        if (!audio.duration) {
            return;
        }

        const rect = progressWrap.getBoundingClientRect();
        const ratio = (event.clientX - rect.left) / rect.width;
        audio.currentTime = ratio * audio.duration;
    });

    volumeSlider.addEventListener('input', () => {
        audio.volume = volumeSlider.value;
    });
})();
