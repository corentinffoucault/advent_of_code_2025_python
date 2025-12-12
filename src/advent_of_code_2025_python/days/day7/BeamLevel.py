class BeamLevel:
    _START_BEAM_CHAR = "S"
    _SPLIT_BEAM_CHAR = "^"

    def __init__(self, level: str):
        self._level = level

    def get_new_beam_position(self, previous_beam_position: set[int]) -> tuple[set[int], int]:
        indexes = [index for index, ch in enumerate(self._level) if ch == BeamLevel._START_BEAM_CHAR]
        next_beam_position = set(indexes)
        size_level = len(self._level)
        nb_split = 0
        for index in previous_beam_position:
            if self._level[index] == self._SPLIT_BEAM_CHAR:
                nb_split += 1
                if index > 0:
                    next_beam_position.add(index-1)
                if index < size_level-1:
                    next_beam_position.add(index+1)
            else :
                next_beam_position.add(index)
        return next_beam_position, nb_split

    def get_all_beam_path(self, previous_beam_position: dict[int, int]) -> dict[int, int]:
        indexes = {index: 1 for index, ch in enumerate(self._level) if ch == BeamLevel._START_BEAM_CHAR}
        next_beam_position = indexes
        size_level = len(self._level)
        for index, nb_path in previous_beam_position.items():
            if self._level[index] == self._SPLIT_BEAM_CHAR:
                if index > 0:
                    new_index = index-1
                    if new_index not in next_beam_position:
                        next_beam_position[new_index] = 0
                    next_beam_position[new_index] += nb_path
                if index < size_level-1:
                    new_index = index+1
                    if new_index not in next_beam_position:
                        next_beam_position[new_index] = 0
                    next_beam_position[new_index] += nb_path
            else :
                if index not in next_beam_position:
                    next_beam_position[index] = 0
                next_beam_position[index] += nb_path
        return next_beam_position