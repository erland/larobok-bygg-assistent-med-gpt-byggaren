# 7. Från experiment till riktig assistent

Du har nu gått från en idé till en GPT som går att prova, förbättra och fortsätta utveckla.

Nästa fråga är inte främst teknisk:

> **Hur ska assistenten faktiskt användas och förvaltas?**

En GPT kan vara allt från ett personligt experiment till ett arbetsverktyg som används av många personer. Ju viktigare assistenten blir, desto mer behöver du tänka på distribution, versionshantering, ansvar och hur förändringar görs.

Det betyder inte att varje GPT måste bli ett stort IT-projekt. Tvärtom är en av styrkorna med arbetssättet att du kan börja litet och höja ambitionsnivån först när behovet finns.

## Börja med det enklaste som fungerar

Det är lätt att tänka att en "riktig" GPT måste publiceras, integreras och automatiseras.

Så behöver det inte vara.

Om du har byggt en assistent för ett begränsat användningsfall och den fungerar bra i en vanlig ChatGPT-konversation kan **Chat ZIP** vara fullt tillräckligt.

Arbetsflödet kan då vara:

1. användaren startar en ny ChatGPT-konversation,
2. bifogar Chat ZIP-filen,
3. ber ChatGPT använda den som assistent,
4. genomför sitt arbete,
5. startar en ny konversation nästa gång det behövs.

Det är enkelt, portabelt och kräver ingen separat installation av en Custom GPT.

För en assistent som främst används av dig själv eller av ett mindre antal personer kan detta vara en mycket rimlig slutpunkt.

> **Välj inte en mer avancerad distributionsform bara för att den finns. Välj den när den löser ett verkligt problem.**

## När Chat ZIP passar bra

Chat ZIP är särskilt användbar när du vill kunna bära med dig assistentens instruktioner och stödmaterial som en fil.

Den passar ofta bra när:

- assistenten används av ett mindre antal personer,
- användaren kan starta arbetet genom att bifoga en ZIP-fil,
- projektet innehåller många filer eller rik runtime-struktur,
- du vill kunna prova nya versioner utan att ändra en publicerad GPT,
- du vill ha en portabel distribution som går att använda i nya konversationer.

Chat ZIP är också ett bra format under utveckling. Du kan bygga en version, använda den på riktiga uppgifter och sedan återvända till GPT Byggaren med dina observationer.

Det gör gränsen mellan experiment och användbart arbetsverktyg mindre dramatisk. Samma distributionsform kan fungera i båda lägena.

## När Custom GPT kan vara bättre

En **Custom GPT** kan vara lämpligare när du vill att användaren ska kunna öppna en färdig assistent direkt i ChatGPT utan att först bifoga en Chat ZIP.

Det kan exempelvis vara värdefullt när:

- många personer ska använda samma assistent,
- du vill göra starten så enkel som möjligt,
- assistenten ska ha ett tydligt namn och en tydlig ingång,
- användarna inte behöver se eller hantera projektfiler,
- den funktionalitet som behövs ryms inom Custom GPT-plattformens möjligheter och begränsningar.

Det betyder inte att Custom GPT alltid är "bättre" än Chat ZIP.

De är två olika sätt att distribuera samma grundidé.

För en liten GPT kan de vara nästan likvärdiga. För en mer omfattande assistent kan Chat ZIP ibland bära mer runtime-material än vad som är praktiskt eller möjligt att lägga i en Custom GPT.

GPT Byggaren är gjord för att hjälpa till med den bedömningen. Du behöver alltså inte bestämma distributionsform innan du ens vet hur GPT:n kommer att se ut.

## Projekt-ZIP:en finns kvar bakom distributionen

Oavsett om användarna arbetar med Chat ZIP eller Custom GPT är **projekt-ZIP:en** fortfarande viktig.

Den är utvecklingsprojektet bakom den version som används.

En användare behöver kanske aldrig se den. Men den behövs när du vill:

- rätta ett problem,
- lägga till Knowledge,
- ändra ett arbetsflöde,
- förbättra tester,
- bygga en ny version,
- skapa en ny distribution.

Det är samma skillnad som mellan en färdig applikation och dess källkod.

Användaren arbetar med den distribuerade produkten. Den som förvaltar produkten behöver utvecklingsprojektet.

## När versionshantering börjar bli värdefull

Så länge du experimenterar själv kan det räcka att spara den senaste projekt-ZIP:en med ett tydligt filnamn.

Men när assistenten börjar användas på riktigt uppstår snabbt frågor som:

- Vilken version använder vi?
- Vad ändrades sedan förra versionen?
- Kan vi gå tillbaka om en förändring blev dålig?
- Vilken ZIP hör till vilken release?
- Är den version vi testar samma som den vi har distribuerat?

Då blir versionshantering värdefull.

Nya GPT Byggaren-projekt har normalt GitHub-stöd från början, med bland annat README samt arbetsflöden för CI och release. Det går att välja bort för uttryckligen lokala eller GitHub-fria projekt. Med GitHub kan projektet exempelvis få:

- historik över förändringar,
- pull requests för granskning,
- automatiska tester vid förändringar,
- versionsmärkta releaser där versionen kan härledas från release-taggen,
- automatiskt byggda distributionsfiler.

Du behöver inte införa allt detta för din första GPT.

Men när fler människor blir beroende av assistenten är det bra att kunna svara på en enkel fråga:

> **Vilken version är det egentligen vi använder?**

## En enkel mognadstrappa

Du kan se utvecklingen som några naturliga nivåer.

### 1. Idé

Du har identifierat en återkommande uppgift som kanske lämpar sig för en specialiserad assistent.

### 2. Experiment

Du bygger en första version med GPT Byggaren och provar den själv.

Målet är lärande, inte perfektion.

### 3. Användbar assistent

GPT:n fungerar tillräckligt bra för verkliga uppgifter. Du känner till dess viktigaste begränsningar och har provat typiska användningsfall.

Chat ZIP kan mycket väl vara rätt distributionsform här.

### 4. Förvaltat arbetsverktyg

Fler personer använder assistenten eller den börjar få större betydelse. Versioner, tester, förändringshistorik och tydligt ansvar blir viktigare.

Här kan Custom GPT, Git och GitHub bli relevanta beroende på situationen.

### 5. Integrerad AI-lösning

Till sist kan behovet växa bortom vad en GPT är bäst lämpad för.

Du kanske behöver:

- integration med verksamhetssystem,
- automatisk behandling av stora mängder ärenden,
- strikt behörighetsstyrning,
- egna datalager,
- transaktioner och säkra uppdateringar i andra system,
- avancerad övervakning,
- garanterade svarstider eller andra driftkrav.

Då börjar frågan handla mindre om att konfigurera en GPT och mer om att bygga ett eget AI-baserat system.

Det är inte ett misslyckande för GPT:n. Tvärtom kan GPT-experimentet ha hjälpt dig förstå behovet innan du investerar i en större lösning.

## När ska du inte bygga vidare på GPT:n?

Det är lika viktigt att kunna stanna.

En specialiserad GPT är särskilt bra när uppgiften handlar om språk, analys, sammanställning, vägledning och arbete med dokument eller information.

Men den är inte automatiskt rätt lösning på varje problem.

Var vaksam om användningsfallet börjar kräva att assistenten självständigt ska:

- fatta beslut med stora konsekvenser,
- garantera att varje svar är korrekt,
- ersätta obligatorisk mänsklig kontroll,
- hålla permanent verksamhetskritisk status utan lämpligt systemstöd,
- fungera som ett transaktionssystem,
- utföra uppgifter där fel inte kan tolereras eller fångas upp.

I sådana fall kan GPT:n fortfarande vara ett stöd, men den bör inte ensam bära hela processen.

## Vem ansvarar för assistenten?

När en GPT går från personligt experiment till gemensamt arbetsverktyg behöver någon äga frågan:

> Vem avgör vad assistenten ska göra och när den ska ändras?

Det behöver inte vara en formell förvaltningsorganisation för en liten GPT. Men det bör vara tydligt vem som:

- tar emot förbättringsförslag,
- bedömer förändringar i uppdraget,
- håller Knowledge aktuell,
- beslutar när en ny version ska tas i bruk,
- följer upp problem som användarna hittar.

GPT Byggaren kan hjälpa till att genomföra förändringarna. Den kan inte ersätta verksamhetens ansvar för vad assistenten ska användas till.

## Ett praktiskt vägval

Anta att remissassistenten från tidigare kapitel nu fungerar bra.

Du använder den själv några gånger i månaden och vill framför allt kunna utveckla den vidare när du upptäcker förbättringar.

Då kan en rimlig lösning vara:

> **Behåll projekt-ZIP:en för utveckling och använd Chat ZIP i det dagliga arbetet.**

Några månader senare börjar tio kollegor använda samma assistent. De vill slippa bifoga en ZIP varje gång och ni behöver kunna säga vilken version som är den aktuella.

Då kan nästa steg vara:

> **Bygg en Custom GPT för användarna och lägg utvecklingsprojektet i GitHub med versionsmärkta releaser.**

Senare kanske organisationen vill att remisser automatiskt ska hämtas från ett ärendehanteringssystem, analyseras och kopplas tillbaka till rätt ärende.

Då har behovet förändrats igen.

> **Nu kan en integrerad AI-lösning vara mer lämplig än att fortsätta pressa in allt i själva GPT:n.**

Poängen är att tekniken får följa behovet, inte tvärtom.

## Din assistent behöver inte nå sista nivån

Mognadstrappan är inte en tävling.

En personlig Chat ZIP som löser ett verkligt problem kan vara en helt färdig lösning.

En Custom GPT som används av ett arbetslag behöver inte bli ett separat IT-system.

Och ett experiment som visar att idén inte ger tillräcklig nytta kan också vara ett bra resultat.

Det viktiga är att välja **minsta ambitionsnivå som ger den nytta du faktiskt behöver**.

## Det viktigaste från kapitlet

När en GPT fungerar behöver du inte automatiskt göra den mer avancerad.

Tänk i stället i tre frågor:

1. **Hur ska den användas?** – räcker Chat ZIP eller blir Custom GPT enklare för användarna?
2. **Hur viktig har den blivit?** – behöver projektet versionshantering, tydligare tester och en förvaltare?
3. **Har behovet vuxit bortom en GPT?** – är det dags för en integrerad AI-lösning i stället?

GPT Byggaren gör det möjligt att börja enkelt och utveckla lösningen stegvis.

Det sammanfattar också bokens huvudidé: börja med **problemet, användaren och ett bra resultat**, och låt tekniken växa först när behovet kräver det.

> **idé → analys → plan → projekt → prova → förbättra → distribuera**

Det är skillnaden mellan en bra prompt för stunden och en AI-assistent som går att använda och vidareutveckla.
