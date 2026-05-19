from models.szemelyauto import Szemelyauto
from models.teherauto import Teherauto
from models.berles import Berles
from models.autokolcsonzo import Autokolcsonzo


def adatok_betoltese():
    """
    A rendszer 3 autóval és 4 bérléssel indul.
    """

    kolcsonzo = Autokolcsonzo("Réka Autókölcsönző")

    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 15000, 5)
    auto2 = Szemelyauto("DEF-456", "Suzuki Swift", 12000, 5)
    auto3 = Teherauto("GHI-789", "Ford Transit", 25000, 1200)

    kolcsonzo.auto_hozzaadasa(auto1)
    kolcsonzo.auto_hozzaadasa(auto2)
    kolcsonzo.auto_hozzaadasa(auto3)

    kolcsonzo.berles_hozzaadasa(Berles(auto1, "2026-05-20"))
    kolcsonzo.berles_hozzaadasa(Berles(auto2, "2026-05-21"))
    kolcsonzo.berles_hozzaadasa(Berles(auto3, "2026-05-22"))
    kolcsonzo.berles_hozzaadasa(Berles(auto1, "2026-05-23"))

    return kolcsonzo


def menu():
    """
    Egyszerű konzolos felhasználói felület.
    Innen érhetők el a program fő funkciói.
    """

    kolcsonzo = adatok_betoltese()

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("5. Kilépés")

        valasztas = input("Válassz egy menüpontot: ")

        if valasztas == "1":
            kolcsonzo.autok_listazasa()

        elif valasztas == "2":
            rendszam = input("Add meg az autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ")

            try:
                ar = kolcsonzo.auto_berlese(rendszam, datum)
                print(f"Sikeres bérlés! Fizetendő összeg: {ar} Ft")
            except ValueError as hiba:
                print(f"Hiba: {hiba}")

        elif valasztas == "3":
            rendszam = input("Add meg a lemondandó autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ")

            if kolcsonzo.berles_lemondasa(rendszam, datum):
                print("A bérlés sikeresen lemondva.")
            else:
                print("Nem található ilyen bérlés.")

        elif valasztas == "4":
            kolcsonzo.berlesek_listazasa()

        elif valasztas == "5":
            print("Kilépés a programból...")
            break

        else:
            print("Érvénytelen választás, próbáld újra.")


if __name__ == "__main__":
    menu()