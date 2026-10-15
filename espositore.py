class Espositore:
    def __init__(self, codice, nome, cognome):
        self._codice = str(codice).strip()
        self._nome = str(nome).strip()
        self._cognome = str(cognome).strip()
        self._stand_assegnato = None  # contiene l'oggetto Stand associato (oppure None)

    def __eq__(self, other):
        """due espositori sono uguali se hanno lo stesso codice"""
        if isinstance(other, Espositore):
            return self._codice == other._codice
        return False

    def __str__(self):
        if self._stand_assegnato is not None:
            return f"{self._codice} - {self._nome} {self._cognome} -> stand: {self._stand_assegnato._codice}"
        return f"{self._codice} - {self._nome} {self._cognome} -> nessuno stand assegnato"