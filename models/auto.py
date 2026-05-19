from abc import ABC, abstractmethod


class Auto(ABC):
    """
    Absztrakt Auto osztály.
    Ez tartalmazza az autók közös attribútumait.
    """

    def __init__(self, rendszam, tipus, berleti_dij):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij

    @property
    def rendszam(self):
        return self._rendszam

    @property
    def tipus(self):
        return self._tipus

    @property
    def berleti_dij(self):
        return self._berleti_dij

    @abstractmethod
    def info(self):
        """
        Az autó adatainak szöveges megjelenítése.
        Ezt a leszármazott osztályok valósítják meg.
        """
        pass