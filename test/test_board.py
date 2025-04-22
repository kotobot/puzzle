import sys

sys.path.append("src")

import pytest
from model import Board

class TestBoard:
    
    def test_board_initialization(self):
        """Test that boards can be created with different dimensions."""
        # Default initialization
        default_board = Board()
        assert default_board is not None
        assert len(default_board.tiles) == 4
        assert len(default_board.tiles[0]) == 4

    def test_board_is_solved(self):
        """Test that the board is solved when in the correct order."""
        board = Board()
        board.is_solved() == True

        # It's not solved after shuffling
        board.shuffle()
        assert board.is_solved() == False

        # Set the board to a solved state
        board.set_grid([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
        assert board.empty_pos == (3, 3)
        assert board.is_solved() == True

        # Move a tile back and forth and check if it's still solved
        board.move_tile((3, 2))
        assert board.is_solved() == False
        board.move_tile((3, 3))
        assert board.is_solved() == True

    def test_illegal_moves(self):
        board = Board()
        board.set_grid([[1, 2, 3, 4],
                                [5, 6, 7, 8],
                                [9, 10, 11, 12],
                                [13, 14, 15, 0]])
        assert board.empty_pos == (3, 3)

        # Attempt to move a tile that is not adjacent to the empty space
        assert board.move_tile((0, 0)) == False
        assert board.empty_pos == (3, 3)

        # Attempt to move a tile that is adjacent to the empty space
        assert board.move_tile((3, 2)) == True
        assert board.empty_pos == (3, 2)

        # Attempt to move the tile out of bounds
        with pytest.raises(IndexError):
            board.move_tile((4, 2))
