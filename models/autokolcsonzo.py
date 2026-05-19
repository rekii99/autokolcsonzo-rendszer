from datetime import datetime
from models.berles import Berles


class Autokolcsonzo:
    """
    Az autókölcsönző osztály.
    Tárolja az autókat, a bérléseket és a kölcsönző nevét.
    """

    def __init__(self, nev):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    @property
    def nev(self):
        return self._nev

    def auto_hozzaadasa(self, auto):
        self._autok.append(auto)

    def berles_hozzaadasa(self, berles):
        self._berlesek.append(berles)

    def autok_listazasa(self):
        if not self._autok:
            print("Nincs autó a rendszerben.")
        else:
            print("\nElérhető autók:")
            print("-" * 80)
            for auto in self._autok:
                print(auto.info())

    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincs aktuális bérlés.")
        else:
            print("\nAktuális bérlések:")
            print("-" * 80)
            for index, berles in enumerate(self._berlesek, start=1):
                print(f"{index}. {berles.info()}")

    def auto_keresese(self, rendszam):
        for auto in self._autok:
            if auto.rendszam.lower() == rendszam.lower():
                return auto
        return None

    def datum_ervenyes(self, datum):
        """
        Ellenőrzi, hogy a dátum formátuma helyes-e,
        és nem múltbeli dátum-e.
        """

        try:
            megadott_datum = datetime.strptime(datum, "%Y-%m-%d").date()
            mai_datum = datetime.today().date()

            if megadott_datum < mai_datum:
                raise ValueError("Múltbeli dátumra nem lehet autót bérelni.")

            return True

        except ValueError as hiba:
            if "Múltbeli" in str(hiba):
                raise hiba
            raise ValueError("Érvénytelen dátumformátum. Helyes forma: ÉÉÉÉ-HH-NN")

    def auto_elerheto(self, rendszam, datum):
        """
        Ellenőrzi, hogy az adott autó az adott napon szabad-e.
        """

        for berles in self._berlesek:
            if berles.auto.rendszam.lower() == rendszam.lower() and berles.datum == datum:
                return False
        return True

    def auto_berlese(self, rendszam, datum):
        """
        Autó bérlése egy adott napra.
        Sikeres bérlés esetén visszaadja a bérleti díjat.
        """

        self.datum_ervenyes(datum)

        auto = self.auto_keresese(rendszam)

        if auto is None:
            raise ValueError("Nincs ilyen rendszámú autó.")

        if not self.auto_elerheto(rendszam, datum):
            raise ValueError("Ez az autó ezen a napon már foglalt.")

        uj_berles = Berles(auto, datum)
        self._berlesek.append(uj_berles)

        return auto.berleti_dij

    def berles_lemondasa(self, rendszam, datum):
        """
        Meglévő bérlés lemondása.
        Csak létező bérlést lehet lemondani.
        """

        for berles in self._berlesek:
            if berles.auto.rendszam.lower() == rendszam.lower() and berles.datum == datum:
                self._berlesek.remove(berles)
                return True

        return False