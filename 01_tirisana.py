from pathlib import Path
import pandas as pd

OUTPUT_FILE = Path(__file__).parent / "tirs.csv"

# Iegūstam neiztīrīto datu kopu
df = pd.read_csv('dati/StudentPerformanceFactors.csv')
sakuma_rindas = len(df)

# Apskatām csv faila struktūru
print('Rindas, kolonnas:', df.shape)
print("\nPirmās rindas:\n", df.head())

# Pārtulkojam kolonnu nosaukumus 
df = df.rename(columns={
    "Hours_Studied": "Mācību_stundas",
    "Attendance": "Apmeklējums",
    "Parental_Involvement": "Vecāku_iesaiste",
    "Access_to_Resources": "Piekļuve_resursiem",
    "Extracurricular_Activities": "Pulciņi",
    "Sleep_Hours": "Gulētās_stundas",
    "Previous_Scores": "Iepriekšējie_rezultāti",
    "Motivation_Level": "Motivācijas_līmenis",
    "Internet_Access": "Piekļuve_internetam",
    "Tutoring_Sessions": "Privātstundas",
    "Family_Income": "Ģimenes_budžets",
    "Teacher_Quality": "Skolotāju_kvalitāte",
    "School_Type": "Skolas_tips",
    "Peer_Influence" : "Draugu_ietekme",
    "Physical_Activity": "Fiziskās_aktivitātes",
    "Learning_Disabilities" : "Macību_grūtības",
    "Parental_Education_Level": "Vecāku_izglītības_līmenis",
    "Distance_from_Home" : "Attālums_no_mājām",
    "Gender": "Dzimums",
    "Exam_Score": "Eksāmenu_rezultāti"
})

# Kolonnu vērtību tūlkojums
df["Vecāku_iesaiste"] = df["Vecāku_iesaiste"].replace({"Low": "Zema", "Medium": "Vidēja", "High": "Augsta"})
df["Piekļuve_resursiem"] = df["Piekļuve_resursiem"].replace({"Low": "Zema", "Medium": "Vidēja", "High": "Augsta"})
df["Pulciņi"] = df["Pulciņi"].replace({"Yes": "Ir", "No": "Nav"})
df["Motivācijas_līmenis"] = df["Motivācijas_līmenis"].replace({"Low": "Zema", "Medium": "Vidēja", "High": "Augsta"})
df["Piekļuve_internetam"] = df["Piekļuve_internetam"].replace({"Yes": "Ir", "No": "Nav"})
df["Ģimenes_budžets"] = df["Ģimenes_budžets"].replace({"Low": "Zems", "Medium": "Vidējs", "High": "Augsts"})
df["Skolotāju_kvalitāte"] = df["Skolotāju_kvalitāte"].replace({"Low": "Zema", "Medium": "Vidēja", "High": "Augsta"})
df["Skolas_tips"] = df["Skolas_tips"].replace({"Public": "Publiskā skola", "Private": "Privātā skola"})
df["Draugu_ietekme"] = df["Draugu_ietekme"].replace({"Positive": "Pozitīva", "Neutral": "Neitrāla", "Negative": "Negatīva"})
df["Macību_grūtības"] = df["Macību_grūtības"].replace({"Yes": "Ir", "No": "Nav"})
df["Vecāku_izglītības_līmenis"] = df["Vecāku_izglītības_līmenis"].replace({"High School": "Vidusskola", "College": "Kolazas līmeņa", "Postgraduate": "Augstākā izglītība"})
df["Attālums_no_mājām"] = df["Attālums_no_mājām"].replace({"Near": "Tuvu", "Moderate": "Vidēji tālu", "Far": "Tālu"})
df["Dzimums"] = df["Dzimums"].replace({"Male": "Vīrietis", "Female": "Sieviete"})

print("Rindas, kolonnas:", df.shape)
print("\nPirmās rindas:\n", df.head())

# Iegūstam trūkstošo vērtību skaitu katrā kolonnā.
print("\nTrūkstošās vērtības katrā kolonnā:\n", df.isnull().sum())

# Iegūstam cik ir dublētu rindu un dzēšam tās, ja tādas eksistē
print("Dublētās rindas:", df.duplicated().sum())
df = df.drop_duplicates()

# Noņemam nevajadzīgās kolonnas, kas neietekmē eksāmena rezultātus
df = df.drop(columns=["Ģimenes_budžets", "Vecāku_izglītības_līmenis", "Attālums_no_mājām", "Dzimums"])

# Pievienojam trūkstošās vērtības, aizpildot tas ar visbiežāk sastopamo vērtību Skolotāju_kvalitātē
df["Skolotāju_kvalitāte"] = df["Skolotāju_kvalitāte"].fillna(df["Skolotāju_kvalitāte"].mode()[0])

# Pārveidojam teksta vērtības uz skaitļiem
df = pd.get_dummies(df, columns=["Vecāku_iesaiste", 
                                 "Piekļuve_resursiem", 
                                 "Pulciņi", 
                                 "Motivācijas_līmenis", 
                                 "Piekļuve_internetam",
                                 "Skolotāju_kvalitāte",
                                 "Skolas_tips",
                                 "Draugu_ietekme",
                                 "Macību_grūtības"], dtype=int)


# Pārbaudām vai nav palikušas trūkstošas vērtības
print("\nTrūkstošās vērtības katrā kolonnā:\n", df.isnull().sum())


print("\nRindas pirms tīrīšanas:", sakuma_rindas)
print("\nRindas pēc tīrīšanas:", len(df))
print("\nDzēstās rindas:", sakuma_rindas - len(df))

# Sablabājam attīrītos datus tirs.csv failā
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
print(f"\nSaglabāts failā {OUTPUT_FILE} (rindu skaits: {len(df)}):\n", df.head())








