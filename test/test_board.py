import sys

sys.path.append("src")

import pytest
from model import Board

class TestBoard:
    @pytest.fixture
    def empty_board(self):
        """Create an empty 3x3 board for testing."""
        return Board(width=3, height=3)
    
    @pytest.fixture
    def filled_board(self):
        """Create a 3x3 board filled with test data."""
        board = Board(width=3, height=3)
        for i in range(3):
            for j in range(3):
                board.set_cell(i, j, f"{i},{j}")
        return board
    
    def test_board_initialization(self):
        """Test that boards can be created with different dimensions."""
        # Default initialization
        default_board = Board()
        assert default_board is not None
