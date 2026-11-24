# Rezultāti manis veidotajam modelim

1. Kas ir šie dati un no kurienes tie nāk?
> Dati nāk no www.kaggle.com, tā ir datukopa, kurā ir skolēnu eksāmenu rezultāti un dažādas kolonnas, kas rezultātus var ietekmēt.

2. Kas ar datiem bija nepareizi un ko tu ar tiem izdarīji? Norādi skaitļus: cik rindu izmesti
un kāpēc!
> Bija neaizpildīti lauki pie skolotāju kvalitātes, vecāku izglītības līmeņā un attāluma no mājām. Kā arī 1 rinda, kurā bija nederīgs eksāmena rezultāts. 
>  Lai likvidētu šīs vērtības kā vecāku izglītība un attālums no mājām es izlēmu, ka šie dati nav būtiski modelim un noņēmu šīs kolonnas. Skolotāju kvalitāte, manuprāt bija svarīga, tāpēc nolēmu ņemt vidējo vērtību no kopas un ievietot to tukšajās vietās.

3. Ko modelis prognozē un cik labi? Salīdzini ar bāzes līniju un pasaki, vai starpība ir vērā
ņemama!

> Modelis prognozē vai skolēns eksāmenu nokārtos ar nokārtošanas līniju 70 p, jo zemākie rezultāti bija 55. Manuprāt, ka šī prognoze ir diezgan vienkārša, tāpēc nevaru teikt, ka modelis to prognozē viennozīmīgi labi. Bāzes līnija ir 73.83%, modeļa precizitāte 82.98%. Manuprāt, ka šī starpība nav īpaši liela un nav vērā ņemama, jo bāzes līnija ir ļoti tuvu modeļa precizitātei.

4. Kuras divas kolonnas izrādījās svarīgākās un vai tas ir loģiski? Ja nav loģiski, uzraksti,
kāpēc tas tā varētu būt!

> Svarīgākās kolonnas izrādijās apmeklējums un mācību stundas, kas ir loģiski, taču mans pirmais pieņēmums bija, ka tām svarīgākākajām kolonnām būtu jābūt iepriekšējiem rezultātiem un apmeklējumam.

5. Atrodi vienu konkrētu rindu, kurā modelis kļūdās! Ieraksti to un paskaidro, kāpēc,
tavuprāt, tieši tur tas kļūdījās.

> Modelis ir kļūdijies 3 rindā, manuprāt, viņš ielika, ka skolēns nokārtos šo eksāmenu, jo apmeklējums šim ierakstam ir 98 un tākā tā bija vissvarīgākā kolonna, tas noteikti tas ietekmēja rezultātu.

6. Ko ar šo modeli NEDRĪKST darīt? Nosauc vienu konkrētu lietojumu un iemeslu, kāpēc
tam tas neder.

> Modelis nevar lemt vai skolēns tiešām ir nokārtojis eksāmenu, jo, lai gan viņam ir precizitāte 82.98%, tas kļūdās, tādēļ viņam šo darbu nevar uzticēt.