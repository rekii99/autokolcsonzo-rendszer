class Berles:
    """
    Egy autóbérlést tárol.
    Egy bérlés egy autóra és egy adott napra vonatkozik.
    """

    def __init__(self, auto, datum):
        self._auto = auto
        self._datum = datum

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum

    def info(self):
        return (
            f"Rendszám: {self.auto.rendszam} | "
            f"Típus: {self.auto.tipus} | "
            f"Dátum: {self.datum} | "
            f"Ár: {self.auto.berleti_dij} Ft"
        )