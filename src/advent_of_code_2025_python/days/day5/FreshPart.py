class FreshPart:

    def __init__(self, start: int, end: int):
        self._start = start
        self._end = end

    @property
    def start(self):
        """lowest limit"""
        return self._start

    @property
    def end(self):
        """highest limit"""
        return self._end

    def contains(self, id_to_check: int) -> bool:
        return self._start <= id_to_check <= self._end

    def nb_elements(self) -> int:
        return self._end - self._start + 1

    def mergeable(self, fresh_part: "FreshPart") -> bool:
        return self.contains(fresh_part.start) or self.contains(fresh_part.end) or fresh_part.contains(self.start) or fresh_part.contains(self.end)

    def merge(self, fresh_part: "FreshPart"):
        self._start = min(self.start, fresh_part.start)
        self._end = max(self.end, fresh_part.end)
