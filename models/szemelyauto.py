from models.auto import Auto


class Szemelyauto(Auto):
    """
    Személyautó osztály.
    Az Auto osztályból származik.
    """

    def __init__(self, rendszam, tipus, berleti_dij, ferohelyek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ferohelyek_szama = ferohelyek_szama

    @property
    def ferohelyek_szama(self):
        return self._ferohelyek_szama

    def info(self):
        return (
            f"Személyautó | Rendszám: {self.rendszam} | "
            f"Típus: {self.tipus} | Díj: {self.berleti_dij} Ft/nap | "
            f"Férőhelyek száma: {self.ferohelyek_szama}"
        )