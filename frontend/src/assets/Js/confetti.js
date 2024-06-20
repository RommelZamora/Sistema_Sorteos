document.addEventListener('DOMContentLoaded', function () {
    const logo = document.getElementById('logo');
    const confettiContainer = document.getElementById('confetti-container');
  
    logo.addEventListener('animationiteration', createConfetti);
  
    function createConfetti() {
      for (let i = 0; i < 30; i++) {
        const confetti = document.createElement('div');
        confetti.classList.add('confetti');
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
        confetti.style.animationDuration = Math.random() * 3 + 2 + 's';
        confettiContainer.appendChild(confetti);
  
        confetti.addEventListener('animationend', () => {
          confetti.remove();
        });
      }
    }
  });
  