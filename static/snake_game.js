let snake, food, direction;

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
    snake = [{ x: 10, y: 10 }];
    food = { x: 15, y: 15 };
    direction = 'right';

    // Start the game loop
    gameLoop();
}

function gameLoop() {
    update();
    draw();
    setTimeout(gameLoop, 100); // Adjust speed as needed
}

function update() {
    // Update snake position
    const head = { ...snake[0] };
    switch (direction) {
        case 'up': head.y--; break;
        case 'down': head.y++; break;
        case 'left': head.x--; break;
        case 'right': head.x++; break;
    }
    snake.unshift(head);

    // Check for collision with food
    if (head.x === food.x && head.y === food.y) {
        // Generate new food
        food = {
            x: Math.floor(Math.random() * 20),
            y: Math.floor(Math.random() * 20)
        };
    } else {
        snake.pop();
    }

    // Check for collision with walls or self
    if (head.x < 0 || head.x >= 20 || head.y < 0 || head.y >= 20 || snake.slice(1).some(segment => segment.x === head.x && segment.y === head.y)) {
        // Game over
        snake = [{ x: 10, y: 10 }];
        direction = 'right';
    }
}

function draw() {
    const canvas = document.getElementById('snakeCanvas');
    const ctx = canvas.getContext('2d');
    const cellSize = canvas.width / 20;

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw snake
    ctx.fillStyle = 'green';
    snake.forEach(segment => {
        ctx.fillRect(segment.x * cellSize, segment.y * cellSize, cellSize, cellSize);
    });

    // Draw food
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x * cellSize, food.y * cellSize, cellSize, cellSize);
}

// Expose the changeDirection function globally
window.changeSnakeDirection = function(newDirection) {
    const opposites = { 'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left' };
    if (newDirection !== opposites[direction]) {
        direction = newDirection;
    }
}

// Initialize the game when the script loads
initGame();