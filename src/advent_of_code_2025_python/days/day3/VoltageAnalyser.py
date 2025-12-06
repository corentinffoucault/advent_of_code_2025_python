class VoltageAnalyser:
    def __init__(self, nb_vol_to_get: int):
        self._nb_vol_to_get = nb_vol_to_get

    def top_n_in_order(self, bank: str) -> int:
        voltage = []

        for c in bank[:1-self._nb_vol_to_get]:
            x = int(c)
            for index, value in enumerate(voltage):
                if x > value:
                    voltage[index] = x
                    voltage = voltage[:index+1]
                    break
            else:
                if len(voltage) < self._nb_vol_to_get:
                    voltage.append(x)

        size_bank = len(bank)
        for index in range(size_bank-self._nb_vol_to_get+1, size_bank):
            voltage = self._add_last_volt(index, bank, size_bank, voltage)

        return int("".join(map(str, voltage)))

    def _add_last_volt(self, index: int, bank: str, size_bank: int, voltage: list[int]) -> list[int]:
        x = int(bank[index])
        start = self._nb_vol_to_get - (size_bank - index)

        for index, value in enumerate(voltage[start:]):
            if x > value:
                voltage[index+start] = x
                voltage = voltage[:index+start+1]
                break
        else:
            if len(voltage) < self._nb_vol_to_get:
               voltage.append(x)

        return voltage
