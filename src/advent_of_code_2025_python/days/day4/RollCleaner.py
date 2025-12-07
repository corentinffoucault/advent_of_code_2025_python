class RollCleaner:

    _roll_char_ = "@"
    _replace_char_ = "."
    _neighbors_ = (
        (-1, -1), (-1, 0), (-1, +1),
        (0, -1),            (0, +1),
        (+1, -1), (+1, 0), (+1, +1)
    )

    def __init__(self):
        pass


    def _count_neighbors(self, map_of_roll, line_index, col_index, size_line, map_height):
        size_line = len(map_of_roll[0])
        map_height = len(map_of_roll)
        nb_roll_around = 0

        for neighbor in self._neighbors_:
            index_in_line = line_index + neighbor[0]
            index_in_col = col_index + neighbor[1]
            if 0 <= index_in_line < map_height and 0 <= index_in_col < size_line:
                if map_of_roll[index_in_line][index_in_col] == self._roll_char_:
                    nb_roll_around += 1

        return nb_roll_around

    def count_deletable_roll(self, map_of_roll: list[list[str]]) -> int:
        nb_deletable_roll = 0
        size_line = len(map_of_roll[0])
        map_height = len(map_of_roll)


        for line_index, line in enumerate(map_of_roll):
            for col_index, char in enumerate(line):
                if char != self._roll_char_:
                    continue
                nb_roll_around = self._count_neighbors(map_of_roll, line_index= line_index, col_index= col_index, size_line=size_line, map_height=map_height)

                if nb_roll_around < 4:
                    nb_deletable_roll += 1

        return nb_deletable_roll

    def count_deletable_roll_with_replace(self, map_of_roll: list[list[str]]) -> tuple[int, list[list[str]]]:
        nb_deletable_roll = 0
        size_line = len(map_of_roll[0])
        map_height = len(map_of_roll)

        for line_index, line in enumerate(map_of_roll):
            for col_index, char in enumerate(line):
                if char != self._roll_char_:
                    continue

                nb_roll_around = self._count_neighbors(map_of_roll, line_index= line_index, col_index= col_index, size_line=size_line, map_height=map_height)

                if nb_roll_around < 4:
                    nb_deletable_roll += 1
                    map_of_roll[line_index][col_index] = self._replace_char_


        return nb_deletable_roll, map_of_roll
