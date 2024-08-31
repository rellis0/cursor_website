import unittest
from unittest.mock import patch, MagicMock
from snake import create_snake_game, add_snake_game


class TestSnake(unittest.TestCase):
    @patch("streamlit.components.v1.html")
    def test_create_snake_game(self, mock_html):
        create_snake_game()
        mock_html.assert_called_once()
        html_content = mock_html.call_args[0][0]
        self.assertIn("snakeCanvas", html_content)
        self.assertIn("gameOverMessage", html_content)
        self.assertIn("Game Over! Click to restart", html_content)
        self.assertEqual(mock_html.call_args[1]["height"], 450)

    @patch("snake.create_snake_game")
    def test_add_snake_game(self, mock_create_snake_game):
        add_snake_game()
        mock_create_snake_game.assert_called_once()


if __name__ == "__main__":
    unittest.main()
