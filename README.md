# Skolēnu eksāmenu rezultātu prognozēšana
Šī projekta mērķis ir izveidot mašīnmācīšanās modeli, kas prognozē, vai skolēns nokārtos eksāmenu, balstoties uz dažādiem faktoriem, piemēram, mācību stundām, apmeklējumu, gulēšanas stundām, motivāciju un citiem datiem.

Projektā tiek izmantots lēmumu koka (`DecisionTreeClassifier`) algoritms no `scikit-learn` bibliotēkas.

Eksāmena nokārtošanas robeža ir 70 punkti:
- **0** – eksāmens nav nokārtots (mazāk par 70 punktiem).
- **1** – eksāmens ir nokārtots (70 vai vairāk punktu).

## Nepieciešamās Python bibliotēkas

- `pandas` – datu nolasīšanai un apstrādei.
- `scikit-learn` – mašīnmācīšanās modeļa izveidei un novērtēšanai.

## Projekta palaišana

1. Instalēt bibliotēkas:
   `pip install pandas scikit-learn`

2. Datu tīrīšanu:
   `python tīrīšana.py`

3. Palaid modeli:
   `python modelis.py`