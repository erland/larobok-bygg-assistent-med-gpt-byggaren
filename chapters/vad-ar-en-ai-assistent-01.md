# 1. Vad är egentligen en AI-assistent?

När du använder ChatGPT i en vanlig konversation möter du en generell AI. Den kan hjälpa till med många olika saker: förklara ett begrepp, sammanfatta en text, skriva ett utkast, analysera ett problem eller hjälpa dig med kod.

Det är en av styrkorna med ChatGPT. Du behöver inte bestämma i förväg exakt vilken sorts arbete du ska göra.

Men samma generalitet har också en baksida. Om du återkommer till samma arbetsuppgift behöver du ofta förklara samma saker igen:

- vilken roll AI:n ska ta,
- vilken typ av underlag den ska använda,
- vad den ska leta efter,
- hur resultatet ska struktureras,
- vad den ska undvika,
- vilka kvalitetskrav som gäller.

En specialiserad AI-assistent är ett sätt att göra mycket av detta återanvändbart.

## Från generell AI till specialiserad assistent

Tänk dig att du regelbundet behöver läsa längre dokument och identifiera sådant som kan påverka din organisation.

Med vanlig ChatGPT kanske du varje gång skriver något i stil med:

> Läs dokumentet. Identifiera sådant som kan påverka vår organisation. Sammanfatta de viktigaste punkterna, förklara varför de är relevanta och skilj tydligt mellan sådant som står i dokumentet och dina egna slutsatser.

Det kan fungera bra. Men nästa gång behöver du komma ihåg instruktionen igen. Kanske formulerar du den lite annorlunda och får ett annat resultat. En kollega kanske använder en helt annan instruktion.

En specialiserad dokumentanalys-GPT kan i stället redan vara utformad för uppgiften.

Du kan då ge den dokumentet och skriva något mycket enklare:

> Analysera detta dokument.

Assistenten känner redan till sitt uppdrag, hur analysen ska göras och hur resultatet ska presenteras.

Det är den viktigaste skillnaden.

**En vanlig ChatGPT-konversation formas huvudsakligen av det du säger just nu. En specialiserad GPT har dessutom ett återanvändbart arbetssätt som har utformats i förväg.**

## Du tränar normalt inte en ny AI-modell

Ordet GPT kan lätt ge intrycket att du skapar eller tränar en egen AI-modell. Det är normalt inte det som händer.

När vi i den här boken talar om att "bygga en GPT" menar vi att vi specialiserar hur en generell AI ska arbeta.

En förenklad mental modell är:

> **AI-modell + instruktioner + kunskap + verktyg + arbetsflöde = specialiserad AI-assistent**

Alla assistenter behöver inte alla delarna. En enkel GPT kanske nästan bara består av bra instruktioner. En mer avancerad GPT kan behöva särskilt kunskapsmaterial, kunna läsa filer, söka på webben eller arbeta enligt ett tydligt flerstegsflöde.

Vi går igenom delarna närmare senare. Just nu räcker det att förstå vad de bidrar med.

## Grundmodellen står för den generella förmågan

Den underliggande AI-modellen står för sådant som språkförståelse, resonemang och förmågan att skapa text.

Det är därför du inte behöver lära en dokumentanalys-GPT vad en sammanfattning är eller hur svenska meningar byggs upp. Den generella modellen har redan breda sådana förmågor.

Det du tillför är i stället specialiseringen.

Det kan jämföras med att anlita en erfaren generalist och ge personen ett tydligt uppdrag, arbetsinstruktioner, relevant material och rätt verktyg. Du behöver inte lära personen läsa från början. Du behöver få arbetet att utföras på rätt sätt i just din situation.

## Instruktionerna beskriver hur assistenten ska arbeta

Instruktionerna kan till exempel ange att dokumentanalys-GPT:n ska:

- börja med att identifiera dokumentets syfte,
- skilja fakta från egna slutsatser,
- fokusera på konsekvenser för organisationen,
- markera osäkerheter,
- presentera resultatet kort och strukturerat.

Bra instruktioner handlar alltså inte bara om tonfall. De beskriver ofta **arbetsmetoden**.

Det är också här en specialiserad GPT blir mer konsekvent än en serie lösa promptar. Samma grundläggande arbetssätt kan användas gång på gång.

## Knowledge ger assistenten relevant specialkunskap

I vissa användningsfall behöver assistenten känna till sådant som den generella modellen inte bör förväntas känna till tillräckligt väl.

Det kan exempelvis vara:

- interna begrepp,
- en metodbeskrivning,
- en produktkatalog,
- en klassificeringsmodell,
- organisationens riktlinjer,
- mallar för hur ett resultat ska se ut.

Sådant material kan ingå som **Knowledge**.

Det är viktigt att skilja Knowledge från instruktioner.

Instruktionen säger exempelvis:

> Bedöm vilka verksamhetsområden som påverkas.

Knowledge kan innehålla:

> Här är organisationens verksamhetsområden och hur de definieras.

Den ena delen beskriver **vad assistenten ska göra**. Den andra ger **material som hjälper den att göra det**.

## Capabilities ger assistenten möjligheter

En assistent kan också behöva vissa funktionella förmågor, eller **capabilities**.

Om den bara ska diskutera text som du skriver i chatten krävs inte mycket mer än språkmodellen själv.

Men andra uppgifter kan kräva att assistenten kan:

- läsa bifogade filer,
- söka efter aktuell information på webben,
- analysera strukturerad data,
- skapa filer,
- använda andra tillgängliga verktyg.

Vilka capabilities som behövs beror alltså på arbetsuppgiften.

En vanlig fallgrop när man börjar tänka på GPT:er är att välja tekniska funktioner först och användningsfall sedan. Det är oftast bättre att göra tvärtom:

1. Vad behöver användaren få gjort?
2. Vilka underlag behövs?
3. Vilka funktioner krävs för att genomföra arbetet?

Det är också så vi kommer att arbeta med GPT Byggaren.

## Arbetsflödet skapar struktur

Vissa uppgifter kan lösas i ett enda steg. Andra blir bättre om assistenten arbetar i en bestämd ordning.

Vår dokumentanalytiker skulle exempelvis kunna arbeta så här:

1. Identifiera vad dokumentet handlar om.
2. Hitta delar som kan vara relevanta för organisationen.
3. Bedöm möjliga konsekvenser.
4. Markera osäkerheter och informationsluckor.
5. Skapa en kort sammanställning.

Användaren behöver inte nödvändigtvis se dessa som fem separata steg. Men assistenten kan vara konstruerad så att arbetet blir mer systematiskt.

Det är en viktig del av specialisering: inte bara **vad AI:n vet**, utan **hur den arbetar**.

## Samma fråga – olika förutsättningar

Anta att du bifogar ett nytt dokument och frågar:

> Vad är viktigt för oss här?

En generell ChatGPT behöver först tolka vad "oss" betyder, vad du anser vara viktigt och hur svaret bör struktureras. Den kan förstå mycket från konversationen, men förutsättningarna är inte nödvändigtvis stabila från gång till gång.

Den specialiserade dokumentanalys-GPT:n kan redan ha följande förutsättningar:

- den vet vilken typ av organisation analysen gäller,
- den har ett definierat analysuppdrag,
- den vet vilka perspektiv den ska kontrollera,
- den följer en bestämd resultatstruktur,
- den markerar när underlaget inte räcker för en säker slutsats.

Frågan kan därför vara kort även om arbetsuppgiften bakom den är ganska avancerad.

Det är inte den korta prompten som gör assistenten bra. Det är att mycket av arbetssättet redan finns definierat.

## Specialisering betyder inte ofelbarhet

En GPT blir inte automatiskt korrekt bara för att den är specialiserad.

Den kan fortfarande:

- misstolka ett dokument,
- dra en för stark slutsats,
- missa ett ovanligt fall,
- använda Knowledge på fel sätt,
- ge ett resultat som ser övertygande ut trots att underlaget är svagt.

Specialisering gör det däremot möjligt att ange ett bättre arbetssätt och sedan testa om assistenten följer det.

Det är därför vi längre fram kommer att behandla testning och förbättring som en naturlig del av utvecklingen, inte som något man gör först när något gått fel.

## När är en specialiserad assistent värd att bygga?

Det finns ingen exakt gräns, men några signaler är särskilt användbara.

En specialiserad assistent är intressant när du märker att du:

- gör samma typ av uppgift återkommande,
- återanvänder ungefär samma instruktioner,
- vill ha resultat i en konsekvent form,
- behöver ge AI:n samma bakgrundsmaterial flera gånger,
- vill kunna dela arbetssättet med andra,
- vill kunna testa och förbättra beteendet över tid.

Däremot behöver varje fråga inte bli en egen GPT.

Om du bara ibland vill få hjälp att formulera ett mejl eller förstå ett begrepp är vanlig ChatGPT oftast enklare. Specialisering ger störst värde när **arbetssättet återkommer**.

## En första modell att bära med sig

Du behöver ännu inte veta hur instruktioner, Knowledge, capabilities eller tester representeras i ett GPT-projekt.

Det viktiga efter det här kapitlet är att kunna se en AI-assistent som något mer konkret än "en smart chatbot".

Den är en generell AI som har fått ett särskilt uppdrag och ett mer stabilt sammanhang för hur uppdraget ska utföras.

Du kan därför tänka på konstruktionen i fyra frågor:

1. **Uppdrag:** Vad ska assistenten hjälpa till med?
2. **Arbetssätt:** Hur ska den angripa uppgiften?
3. **Underlag:** Vilken särskild kunskap eller information behöver den?
4. **Förmågor:** Vilka verktyg behöver den för att kunna göra jobbet?

Det är ungefär här GPT Byggaren kommer in. Du behöver inte själv översätta svaren på dessa frågor till en komplett teknisk GPT-struktur. I stället hjälper GPT Byggaren dig att analysera behovet och bygga projektet.

Men innan vi använder verktyget behöver vi kunna beskriva själva problemet tillräckligt tydligt.

Det är nästa steg.

## Reflektion

Tänk på hur du själv använder ChatGPT i dag.

Finns det någon uppgift där du ofta behöver förklara ungefär samma sak innan ChatGPT kan börja hjälpa dig?

Skriv gärna ner tre saker:

- vilken uppgift du återkommer till,
- vilket underlag du brukar ge ChatGPT,
- hur du helst vill att resultatet ska se ut.

Du behöver inte formulera någon perfekt GPT-idé ännu. I nästa kapitel använder vi just den typen av observationer för att gå från ett löst behov till ett tydligt användningsfall.

## Kort sammanfattning

En specialiserad GPT är normalt inte en nytränad AI-modell. Den bygger vidare på en generell AI men ger den ett tydligare och mer återanvändbart uppdrag.

Specialiseringen kan bestå av instruktioner, Knowledge, capabilities och ett definierat arbetsflöde. Det gör det möjligt att få ett mer konsekvent arbetssätt utan att behöva formulera hela uppgiften från början i varje konversation.

Nästa fråga är därför inte vilken teknik GPT:n ska använda, utan vilket problem den faktiskt ska lösa.
