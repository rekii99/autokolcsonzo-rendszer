from models.auto import Auto


class Teherauto(Auto):
    """
    Teherautó osztály.
    Az Auto osztályból származik.
    """

    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    @property
    def teherbiras(self):
        return self._teherbiras

    def info(self):
        return (
            f"Teherautó | Rendszám: {self.rendszam} | "
            f"Típus: {self.tipus} | Díj: {self.berleti_dij} Ft/nap | "
            f"Teherbírás: {self.teherbiras} kg"
        )