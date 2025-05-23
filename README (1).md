# Laivų mūšis – OOP Kursinis darbas

## 1. Įžanga

**Darbo tikslas:** Sukurti objektinio programavimo principais pagrįstą žaidimą.

**Tema:** Laivų mūšis (Battleship game). Programa leidžia žaisti prieš AI 6×6 žaidimo lentoje, naudojant `tkinter` grafinę vartotojo sąsają.

**Kaip paleisti programą:**
1. Įsidiekite Python 3.x
2. Atsisiųskite projektą
3. Paleiskite terminale:
```bash
python main.py
```

**Kaip naudoti programą:**
- Spauskite ant pilkų langelių, kad šauti į AI laivus
- Raudona = pataikymas, mėlyna = nepataikymas
- Po kiekvieno ėjimo AI šauna automatiškai
- Visi veiksmai įrašomi į `game_log.txt` su data ir laiku

---

## 2. Analizė / Įgyvendinimas

### Objektinio programavimo principai:

#### Inkapsuliacija
Kiekviena klasė turi savo duomenis ir metodus, pvz.:
```python
class Ship:
    def __init__(self, size, positions):
        self.size = size
        self.positions = positions
        self.hits = set()
```

#### Abstrakcija
Vartotojas naudoja paprastus metodus, o visa logika paslėpta:
```python
self.player_shoot(row, col)
```

#### Polimorfizmas
Metodas `receive_attack()` veikia skirtingai skirtingiems objektams:
```python
self.player.board.receive_attack(pos)
self.ai.board.receive_attack(pos)
```

#### Paveldėjimas
Visos klasės yra savarankiškos, tačiau jeigu yra noras galima išplesti žaidimo objektų funkcionalumą
```

---

### Dizaino šablonas – Factory Method
Laivai kuriami naudojant `ShipFactory`:
```python
class ShipFactory:
    @staticmethod
    def create_ship(size, positions):
        return Ship(size, positions)
```

### Failų rašymas
Kiekvienas ėjimas įrašomas į failą:
```python
self.log(f"Player shoots at {pos} - {'HIT' if hit else 'MISS'}")
```

### Testavimas
Programos komponentai testuojami `unittest` biblioteka:
```python
def test_ship_hit_and_sunk(self):
    ship = Ship(2, [(0, 0), (0, 1)])
```

### Grafinė sąsaja (GUI)
Sukurta naudojant `tkinter`. Mygtukai keičia spalvą pagal šūvio rezultatą. Žaidimas vyksta realiu laiku.

---

## 3. Rezultatai

-  Sukurtas pilnai veikiantis žaidimas su 6x6 lenta
-  Pritaikyti visi 4 OOP principai ir Factory Pattern
- Grafinė sąsaja leidžia žaisti patogiai ir intuityviai
- Veiksmų žurnalas fiksuojamas faile
-  Iššūkis: tinkamai sudėti laivus be persidengimo ir su tarpu tarp jų

---

## 4. Išvados

- Sukurtas veikiantis OOP pagrindu paremtas žaidimas
- Parodytas sugebėjimas naudoti OOP, GUI ir testavimo technikas
- Programa įgyvendina funkcinius reikalavimus
- Projektas gali būti toliau plečiamas:
  - 2 žaidėjų režimas
  - Sunkumo lygiai AI
  - Laivų išdėstymo pasirinkimas vartotojui
