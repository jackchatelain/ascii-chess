from helpers import index_for_move
import pytest

# def test_a1():
#     assert index_for_move("a", "1") == 57
# def test_h8():
#     assert index_for_move("h", "8") == 8

# def test_e2():
#     assert index_for_move("e", "2") == 53
# def test_e4():
#     assert index_for_move("e", "4") == 37

# def test_e5():
#     assert index_for_move("e", "5") == 30
# def test_e7():
#     assert index_for_move("e", "7") == 14

# def test_g1():
#     assert index_for_move("g", "1") == 62
# def test_f3():
#     assert index_for_move("f", "3") == 45


@pytest.mark.parametrize("rank, file, expected", [
    ("a", "8", 1),
    ("b", "8", 2),
    ("c", "8", 3),
    ("d", "8", 4),
    ("e", "8", 5),
    ("f", "8", 6),
    ("g", "8", 7),
    ("h", "8", 8),

    ("a", "7", 9),
    ("b", "7", 10),
    ("c", "7", 11),
    ("d", "7", 12),
    ("e", "7", 13),
    ("f", "7", 14),
    ("g", "7", 15),
    ("h", "7", 16),

    ("a", "6", 17),
    ("b", "6", 18),
    ("c", "6", 19),
    ("d", "6", 20),
    ("e", "6", 21),
    ("f", "6", 22),
    ("g", "6", 23),
    ("h", "6", 24),

    ("a", "5", 25),
    ("b", "5", 26),
    ("c", "5", 27),
    ("d", "5", 28),
    ("e", "5", 29),
    ("f", "5", 30),
    ("g", "5", 31),
    ("h", "5", 32),

    ("a", "4", 33),
    ("b", "4", 34),
    ("c", "4", 35),
    ("d", "4", 36),
    ("e", "4", 37),
    ("f", "4", 38),
    ("g", "4", 39),
    ("h", "4", 40),

    ("a", "3", 41),
    ("b", "3", 42),
    ("c", "3", 43),
    ("d", "3", 44),
    ("e", "3", 45),
    ("f", "3", 46),
    ("g", "3", 47),
    ("h", "3", 48),

    ("a", "2", 49),
    ("b", "2", 50),
    ("c", "2", 51),
    ("d", "2", 52),
    ("e", "2", 53),
    ("f", "2", 54),
    ("g", "2", 55),
    ("h", "2", 56),

    ("a", "1", 57),
    ("b", "1", 58),
    ("c", "1", 59),
    ("d", "1", 60),
    ("e", "1", 61),
    ("f", "1", 62),
    ("g", "1", 63),
    ("h", "1", 64),

])
def test(rank, file, expected):
    assert index_for_move(rank, file) == expected
