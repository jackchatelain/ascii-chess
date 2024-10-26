fileNums = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}

def index_for_move(file_letter, rank):
    # Convert column letter to number
    column = int(fileNums.get(file_letter))
    row_index = int(rank)
    index = ((8 - row_index) * 8) + column + 1
    print(f"{file_letter}{rank}={index}")
    return index
