import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#  Nolasa tirs.csv failu
df = pd.read_csv('tirs.csv')

# x, y dati pēc kuriem tiek prognozēti ekasāmenu rezultāti, nokārtoja ir no 70 punktiem, jo datu kopā zemākais punktu skaits ir 55
df["Nokartoja"] = (df["Eksāmenu_rezultāti"] >= 70).astype(int)

x = df.drop(columns=["Eksāmenu_rezultāti", "Nokartoja"])
y = df["Nokartoja"]

#  Sadalām datu kopu treniņdatos un testēšanas datos (8/2)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=1)

# Izveidojam lēmumu koku modeli
modelis = DecisionTreeClassifier(max_depth=3, random_state=42)

# Modeļa apmācīšana
modelis.fit(x_train, y_train)

# Prognozes testa un treniņa datiem
trenina_prognozes = modelis.predict(x_train)
testa_prognozes = modelis.predict(x_test)

# Aprēķinām modeļa precizitāti
testa_precizitate = accuracy_score(y_test, testa_prognozes)

# # Bāzes līnija
biezaka_atbilde = y_train.mode()[0]
bazes_prognozes = [biezaka_atbilde] * len(y_test)
bazes_precizitate = accuracy_score(y_test, bazes_prognozes)

# Izvadām modeļa rezultātus
print("Modeļa precizitāte:", round(testa_precizitate * 100, 2), "%")
print("Bāzes līnijas precizitāte:", round(bazes_precizitate * 100, 2), "%")


if testa_precizitate > bazes_precizitate:
    print("Modelis ir labāks par bāzes līniju!")
elif testa_precizitate == bazes_precizitate:
    print("Modelis ir tikpat precīzs kā bāzes līnija.")
else:
    print("Modelis ir sliktāks par bāzes līniju.")

# Modeļa precizitātei divas svarīgākās kolonnas
kolonnas = pd.Series(
    modelis.feature_importances_,
    index=x.columns
)

print("\nDivas svarīgākās kolonnas:")
print(kolonnas.sort_values(ascending=False).head(2))

# Reālie dati pret prognozētajiem
print("\nPirmās 20 prognozes:")
for ista_atbilde, prognoze in zip(y_test.iloc[:20], testa_prognozes[:20]):
    print("Īstā kategorija:", ista_atbilde, "| Prognozētā kategorija:", prognoze)
