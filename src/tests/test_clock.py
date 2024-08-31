import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from clock import create_clock, update_clock


class TestClock(unittest.TestCase):
    @patch("streamlit.empty")
    def test_create_clock(self, mock_empty):
        mock_placeholder = MagicMock()
        mock_empty.return_value = mock_placeholder
        result = create_clock()
        self.assertEqual(result, mock_placeholder)

    @patch("datetime.datetime")
    def test_update_clock(self, mock_datetime):
        mock_clock = MagicMock()
        mock_datetime.now.return_value = datetime(2023, 5, 1, 12, 34, 56)

        update_clock(mock_clock)

        mock_clock.markdown.assert_called_once_with(
            "<h1 style='color: white; text-align: center;'>12:34:56</h1>",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    unittest.main()
