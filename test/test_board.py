import pytest
from puzzle import Board

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
    
    def test_get_set_cell(self, empty_board):
        """Test getting and setting values on the board."""
        empty_board.set_cell(1, 1, "X")
        assert empty_board.get_cell(1, 1) == "X"
        assert empty_board.get_cell(0, 0) is None
    
    def test_board_bounds(self, empty_board):
        """Test that the board enforces its boundaries."""
        with pytest.raises(IndexError):
            empty_board.set_cell(3, 3, "X")
        
        with pytest.raises(IndexError):
            empty_board.get_cell(-1, 0)
    
    def test_is_full(self, empty_board, filled_board):
        """Test checking if board is full."""
        assert not empty_board.is_full()
        assert filled_board.is_full()
    
    def test_to_string(self, filled_board):
        """Test string representation of the board."""
        board_str = str(filled_board)
        assert isinstance(board_str, str)
        assert "0,0" in board_str