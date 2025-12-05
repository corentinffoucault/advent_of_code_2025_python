class RangeAnalyser:

    @staticmethod
    def sum_duplicated_sequence_fast(start: int, end: int) -> int:
        sum_of_invalid = 0

        min_len = len(str(start))
        if min_len % 2 != 0:
            min_len += 1

        max_len = len(str(end))
        if max_len % 2 != 0:
            max_len -= 1

        for length in range(min_len, max_len + 1, 2):
            half_len = length // 2
            start_half = 10**(half_len - 1) if half_len > 1 else 0
            end_half = 10**half_len
            for half in range(start_half, end_half+1):
                n = int(str(half) * 2)
                if start <= n <= end:
                    sum_of_invalid += n
        return sum_of_invalid

    @staticmethod
    def sum_repeated_sequence_fast(start: int, end: int) -> int:

        min_len = len(str(start))
        max_len = len(str(end))

        invalids_values = set()

        for length in range(min_len, max_len + 1):
            for pattern_len in range(1, length//2+1):
                if length % pattern_len != 0:
                    continue
                start_pattern = 10**(pattern_len - 1)
                end_pattern = 10**pattern_len
                for pattern in range(start_pattern, end_pattern):
                    invalid_value = int(str(pattern)*(length//pattern_len))
                    if start <= invalid_value <= end:
                        invalids_values.add(invalid_value)
        return sum(invalids_values)