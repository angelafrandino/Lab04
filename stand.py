class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self._codice = codice
        self._superficie = float(superficie)
        self._padiglione = padiglione
        self._prezzo_base = float(prezzo_base)
        self._disponibile = True
        self._espositore = None

    def calcola_prezzo(self):
        return float(self._prezzo_base)

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self._codice == other._codice
        return False

    def __lt__(self, other):
        if isinstance(other, Stand):
            return self.calcola_prezzo() < other.calcola_prezzo()
        return False

    def __str__(self):
        return (f"{self._codice}: standard | {self._superficie:.0f} mq - "
                f"padiglione {self._padiglione} - prezzo {self.calcola_prezzo():.2f}€")


class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, num_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self._num_prese = int(num_prese)

    def calcola_prezzo(self):
        return self._prezzo_base * (1 + 0.07 * self._num_prese)

    def __str__(self):
        return (f"{self._codice}: superficie {self._superficie:.0f} mq - "
                f"padiglione {self._padiglione} - prezzo {self.calcola_prezzo():.2f}€ - "
                f"prese aggiuntive {self._num_prese}")

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self._posizione = posizione

    def calcola_prezzo(self):
        return self._prezzo_base * 1.30

    def __str__(self):
        return (f"{self._codice}: superficie {self._superficie:.0f} mq - "
                f"padiglione {self._padiglione} - prezzo {self.calcola_prezzo():.2f}€ -"
                f"premium ({self._posizione})")