snake_html = """
<style>
    #snakeCanvas {
        border: 1px solid white;
        margin: 0 auto;
        display: block;
    }
    #gameMessage {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 24px;
        color: white;
        text-align: center;
    }
</style>
<div style="position: relative;">
    <canvas id="snakeCanvas" width="400" height="400"></canvas>
    <div id="gameMessage">Click to start</div>
</div>
<p style='text-align: center;'>Use arrow keys to control the snake. Eat the red fruit to grow!</p>
<script>
    const canvas = document.getElementById('snakeCanvas');
    const ctx = canvas.getContext('2d');
    const scale = 20;
    const rows = canvas.height / scale;
    const columns = canvas.width / scale;
    const gameMessage = document.getElementById('gameMessage');

    let snake;
    let fruit;
    let gameOver = false;
    let gameStarted = false;
    let gameInterval;

    function setup() {
        snake = new Snake();
        fruit = new Fruit();
        fruit.pickLocation();
        gameOver = false;
        gameStarted = true;
        gameMessage.style.display = 'none';
        
        if (gameInterval) {
            clearInterval(gameInterval);
        }
        
        gameInterval = setInterval(() => {
            if (!gameOver) {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                fruit.draw();
                snake.update();
                snake.draw();

                if (snake.eat(fruit)) {
                    fruit.pickLocation();
                }

                gameOver = snake.checkCollision();
                if (gameOver) {
                    gameMessage.innerHTML = 'Game Over!<br>Click to restart';
                    gameMessage.style.display = 'block';
                    clearInterval(gameInterval);
                }
            }
        }, 250);
    }

    window.addEventListener('keydown', ((evt) => {
        if (gameStarted && !gameOver && ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(evt.key)) {
            evt.preventDefault();
            const direction = evt.key.replace('Arrow', '');
            snake.changeDirection(direction);
        }
    }));

    canvas.addEventListener('click', () => {
        if (!gameStarted || gameOver) {
            setup();
        }
    });

    function Snake() {
        this.x = 0;
        this.y = 0;
        this.xSpeed = scale * 1;
        this.ySpeed = 0;
        this.total = 0;
        this.tail = [];

        this.draw = function() {
            ctx.fillStyle = "#FFFFFF";
            for (let i=0; i<this.tail.length; i++) {
                ctx.fillRect(this.tail[i].x, this.tail[i].y, scale, scale);
            }
            ctx.fillRect(this.x, this.y, scale, scale);
        }

        this.update = function() {
            for (let i=0; i<this.tail.length - 1; i++) {
                this.tail[i] = this.tail[i+1];
            }

            this.tail[this.total - 1] = { x: this.x, y: this.y };

            this.x += this.xSpeed;
            this.y += this.ySpeed;

            // Wrap around the canvas
            if (this.x < 0) {
                this.x = canvas.width - scale;
            } else if (this.x >= canvas.width) {
                this.x = 0;
            }
            if (this.y < 0) {
                this.y = canvas.height - scale;
            } else if (this.y >= canvas.height) {
                this.y = 0;
            }
        }

        this.changeDirection = function(direction) {
            switch(direction) {
                case 'Up':
                    if (this.ySpeed === 0) {
                        this.xSpeed = 0;
                        this.ySpeed = -scale;
                    }
                    break;
                case 'Down':
                    if (this.ySpeed === 0) {
                        this.xSpeed = 0;
                        this.ySpeed = scale;
                    }
                    break;
                case 'Left':
                    if (this.xSpeed === 0) {
                        this.xSpeed = -scale;
                        this.ySpeed = 0;
                    }
                    break;
                case 'Right':
                    if (this.xSpeed === 0) {
                        this.xSpeed = scale;
                        this.ySpeed = 0;
                    }
                    break;
            }
        }

        this.eat = function(fruit) {
            if (this.x === fruit.x && this.y === fruit.y) {
                this.total++;
                return true;
            }
            return false;
        }

        this.checkCollision = function() {
            for (let i=0; i<this.tail.length; i++) {
                if (this.x === this.tail[i].x && this.y === this.tail[i].y) {
                    return true;
                }
            }
            return false;
        }
    }

    function Fruit() {
        this.x;
        this.y;

        this.pickLocation = function() {
            this.x = (Math.floor(Math.random() * columns - 1) + 1) * scale;
            this.y = (Math.floor(Math.random() * rows - 1) + 1) * scale;
        }

        this.draw = function() {
            ctx.fillStyle = "#FF0000";
            ctx.fillRect(this.x, this.y, scale, scale)
        }
    }

    // Initial setup to show "Click to start" message
    ctx.fillStyle = "#000000";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
</script>
"""
