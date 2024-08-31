function initGame() {
    const canvas = document.getElementById('snakeCanvas');
    const ctx = canvas.getContext('2d');

    // Make canvas responsive
    function resizeCanvas() {
        const maxWidth = window.innerWidth;
        const maxHeight = window.innerHeight * 0.8;
        const size = Math.min(maxWidth, maxHeight);
        canvas.width = size;
        canvas.height = size;
        // You may need to adjust your game's grid size here
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Initialize your game here
    // ...
}