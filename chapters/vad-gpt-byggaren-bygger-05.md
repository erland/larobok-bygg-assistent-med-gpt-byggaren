# 5. Vad GPT Byggaren bygger åt dig

I förra kapitlet byggde vi en första GPT utan att behöva förstå projektets alla tekniska delar. Det är en av poängerna med GPT Byggaren: du ska kunna börja i verksamhetsbehovet och låta verktyget ta ansvar för en stor del av konstruktionen.

Men det är ändå värdefullt att förstå **vad som faktiskt byggs**.

Inte för att du ska börja redigera varje fil manuellt, utan för att du ska kunna bedöma om assistenten har rätt beteende, rätt kunskap och rätt gränser.

Ett enkelt sätt att se på en GPT är att den består av flera delar:

> **uppdrag + instruktioner + kunskap + förmågor + arbetsflöden + kvalitetskontroller + distribution**

GPT Byggaren hjälper dig att omsätta din idé till dessa delar och hålla dem samordnade.

## Instruktionerna styr hur assistenten arbetar

Instruktionerna beskriver hur GPT:n ska bete sig.

För vår dokumentanalys-GPT kan instruktionerna till exempel säga att den ska:

- identifiera sådant som kan påverka organisationen,
- skilja fakta i dokumentet från egna slutsatser,
- markera osäkerheter,
- prioritera viktig påverkan framför detaljer,
- inte fatta beslut åt användaren.

Detta är mer än en startprompt.

Instruktionerna fungerar som assistentens återkommande arbetssätt. När en ny användare startar en ny konversation ska samma grundläggande beteende fortfarande gälla.

Det är därför en bra GPT inte bara är en samling smarta formuleringar. Instruktionerna behöver tillsammans bilda ett begripligt och konsekvent arbetssätt.

### Beteende är inte samma sak som kunskap

En viktig skillnad är mellan **hur GPT:n ska arbeta** och **vad den behöver känna till**.

Anta att dokumentanalys-GPT:n ska analysera material utifrån en organisations interna principer.

Då kan följande vara en instruktion:

> Jämför dokumentets innehåll med organisationens styrande principer och lyft möjliga konflikter.

Själva principerna hör däremot normalt hemma som kunskapsunderlag.

Det ger en enkel tumregel:

> **Instruktioner beskriver beteendet. Knowledge beskriver sådant assistenten behöver veta.**

Gränsen är inte alltid perfekt, men den är mycket användbar när du bedömer ett projekt.

## Knowledge ger assistenten specialiserad kunskap

En generell språkmodell kan mycket, men den känner inte automatiskt till allt som är specifikt för din organisation, metod eller uppgift.

Därför kan en GPT få särskilt **Knowledge-material**.

Det kan exempelvis vara:

- interna riktlinjer,
- metodbeskrivningar,
- begreppslistor,
- mallar,
- exempel på önskat resultat,
- offentliga regelverk eller andra stabila referensdokument.

I dokumentanalys-exemplet skulle vi kunna ge assistenten en kort beskrivning av organisationens uppdrag, vilka områden den ansvarar för och vilka typer av konsekvenser som är särskilt viktiga att uppmärksamma.

Då behöver vi inte pressa in all denna information i huvudinstruktionen.

### Knowledge ska ha ett tydligt syfte

Mer material är inte automatiskt bättre.

Om du lägger in stora mängder dokument utan tydligt syfte blir det svårare att förstå vilken information GPT:n faktiskt förväntas använda.

Fråga därför för varje kunskapskälla:

- Vad ska GPT:n använda denna information till?
- I vilka situationer är den relevant?
- Är informationen stabil nog att ligga i projektet?
- Riskerar den att bli inaktuell?

GPT Byggaren kan hjälpa till att strukturera materialet, men du behöver kunna bedöma om kunskapen verkligen är rätt för verksamhetsuppgiften.

## Capabilities avgör vad assistenten kan göra

En GPT behöver ibland mer än bara instruktioner och statisk kunskap.

Den kan exempelvis behöva kunna:

- läsa bifogade filer,
- söka på webben,
- analysera strukturerad information,
- skapa filer,
- köra beräkningar eller scripts,
- använda andra tillgängliga verktyg.

I GPT-projekt kallas sådana förmågor ofta **capabilities**.

För dokumentanalys-GPT:n är filhantering central. Om användaren inte kan ge assistenten dokumentet som ska analyseras faller hela användningsfallet.

En annan GPT kanske främst behöver webbsökning. En tredje behöver ingen extern förmåga alls.

Det viktiga är därför inte att aktivera så mycket som möjligt, utan att fråga:

> **Vilka förmågor krävs för att lösa den faktiska uppgiften?**

GPT Byggaren ska hjälpa dig göra denna bedömning från användningsfallet i stället för att du först behöver lära dig alla tekniska alternativ.

## Arbetsflödet binder ihop delarna

Instruktioner, Knowledge och capabilities räcker inte alltid var för sig.

För mer avancerade uppgifter behöver assistenten också ett tydligt **arbetsflöde**.

För dokumentanalys-GPT:n kan det förenklat vara:

1. förstå vad dokumentet handlar om,
2. identifiera relevanta delar,
3. bedöma möjlig påverkan,
4. skilja säkra observationer från osäkerheter,
5. prioritera det viktigaste,
6. presentera resultatet i en återkommande struktur.

Ett sådant arbetsflöde gör beteendet mer förutsägbart.

Det betyder inte att GPT:n måste följa ett stelt program där varje fråga alltid behandlas exakt likadant. Men den får en tydligare metod att utgå från.

Det är särskilt värdefullt när uppgiften består av flera moment och när resultatet ska bli konsekvent mellan olika användningar.

## Tester kontrollerar sådant som går att kontrollera automatiskt

När GPT Byggaren skapar ett riktigt projekt kan det också innehålla tester.

Det kan först kännas överdrivet. En GPT är ju inte ett traditionellt program där samma indata alltid måste ge exakt samma text.

Men mycket går ändå att kontrollera.

Tester kan exempelvis upptäcka att:

- en obligatorisk projektfil saknas,
- en konfigurationsfil har fel format,
- ett script eller en transformation ger fel resultat,
- en distribution inte går att bygga eller saknar obligatoriska filer,
- en distribution inte kan starta med sina viktigaste resurser,
- ett förväntat projektkontrakt inte längre uppfylls.

Grundprincipen är enkel: **sådant som har ett exakt kontrollerbart svar bör testas deterministiskt**. Det kan gälla projektstruktur, scheman, byggsteg, distribution och vissa egenskaper i körningen.

De kontrollerna gör att tekniska och strukturella fel kan upptäckas tidigt i stället för först när någon försöker använda eller distribuera GPT:n.

## Evals provar assistentens beteende

För en AI-assistent räcker strukturella tester inte hela vägen.

Vi vill också veta hur GPT:n beter sig i realistiska situationer.

Där kommer **evals** in.

En eval är förenklat ett scenario där vi provar om assistenten beter sig som avsett.

För vårt exempel skulle scenarier kunna vara:

- ett dokument med tydlig påverkan på organisationen,
- ett dokument där påverkan är osäker,
- ett dokument som i praktiken inte berör organisationen,
- ett dokument där användaren försöker få GPT:n att dra en säkrare slutsats än underlaget medger.

Det viktiga är inte att svaret har exakt samma formulering varje gång.

Det viktiga är att centrala egenskaper håller:

- relevant påverkan identifieras,
- osäkerhet markeras,
- irrelevant innehåll får inte dominera,
- assistenten överskrider inte sin roll.

### Automatisk kvalitet och mänsklig kvalitet kompletterar varandra

Tester och evals är värdefulla, men de kan inte ensamma avgöra om en GPT är bra.

En assistent kan passera alla automatiska kontroller och ändå vara frustrerande att använda.

Därför behöver du fortfarande prova den med verkliga eller realistiska uppgifter.

Tänk på kvalitet i två lager:

> **Automatiska kontroller skyddar projektet mot kända fel.**  
> **Mänsklig användning visar om assistenten faktiskt är hjälpsam.**

Det ena ersätter inte det andra.

## Projektstatus håller ihop utvecklingen

Ett GPT-projekt behöver också veta **var i utvecklingen det befinner sig**. Därför lagrar GPT Byggaren projektets syfte, viktiga beslut, genomförda steg och nästa rekommenderade arbete i projektet.

Det är det som gör projekt-ZIP:en återupptagningsbar. När du fortsätter senare behöver GPT Byggaren inte förlita sig på att hela den gamla chatthistoriken finns kvar.

När assistenten ska användas byggs i stället en distribution, exempelvis Chat ZIP eller Custom GPT. Skillnaden mellan dessa gick vi igenom tidigare; här räcker det att komma ihåg att **projektet är utvecklingsunderlaget och distributionen är det användaren kör**.

## Från en önskan till flera projektdelar

Nu kan vi följa ett konkret önskemål genom projektet.

Anta att du säger:

> Jag vill att GPT:n alltid markerar när den är osäker på om dokumentet faktiskt påverkar organisationen.

Det kan påverka flera delar samtidigt.

**Instruktionen** kan behöva beskriva hur osäkerheten ska hanteras.

**Arbetsflödet** kan behöva lägga in ett uttryckligt steg där säkerheten i bedömningen värderas.

**Resultatformatet** kan behöva få en markering för osäker påverkan.

**Evals** kan behöva innehålla ett scenario där kopplingen till organisationen är oklar.

Det är här GPT Byggaren gör stor nytta: ett verksamhetskrav behöver ofta bli flera samordnade delar i projektet.

Som användare behöver du inte själv känna till exakt vilka filer som ska ändras.

Men du bör kunna kontrollera att resultatet motsvarar önskemålet.

## Vad behöver du egentligen förstå?

Efter detta kapitel behöver du inte kunna bygga projektstrukturen för hand.

Det viktiga är att du kan skilja på följande:

| Del | Frågan den besvarar |
|---|---|
| Uppdrag | Vad ska assistenten hjälpa till med? |
| Instruktioner | Hur ska den bete sig? |
| Knowledge | Vad behöver den känna till? |
| Capabilities | Vad behöver den kunna göra? |
| Arbetsflöde | Hur ska en mer sammansatt uppgift genomföras? |
| Tester | Är projektets struktur och kontrakt fortfarande hela? |
| Evals | Beter sig assistenten rätt i viktiga scenarier? |
| Projektstatus | Var befinner sig utvecklingen och vad händer härnäst? |
| Distribution | Hur paketeras assistenten för faktisk användning? |

Den modellen räcker långt när du granskar vad GPT Byggaren producerar.

## Praktisk reflektion: beteende eller kunskap?

Tänk på din egen GPT-idé från kapitel 2.

Skriv ner två saker:

1. Något GPT:n **alltid ska göra på ett visst sätt**.
2. Något GPT:n **behöver känna till för att kunna göra ett bra jobb**.

Den första punkten hör sannolikt hemma i beteendet och instruktionerna.

Den andra hör sannolikt hemma i Knowledge eller i en informationskälla som GPT:n kan använda.

Exempel från vår dokumentanalys-GPT:

**Beteende:**

> Markera tydligt när kopplingen mellan dokumentets innehåll och organisationen är osäker.

**Kunskap:**

> Organisationens uppdrag, ansvarsområden och centrala styrande principer.

Den enkla skillnaden hjälper dig upptäcka många designproblem tidigt.

## När behöver du öppna motorhuven?

Ibland behöver du titta djupare i projektet.

Det kan vara motiverat när:

- GPT:n beter sig fel trots flera vanliga förbättringsförsök,
- samma problem återkommer efter ändringar,
- du behöver förstå exakt vilken kunskap en slutsats bygger på,
- en distribution fungerar annorlunda än en annan,
- tester eller validering rapporterar ett tekniskt problem,
- projektet ska lämnas över till någon som ska förvalta det.

Men börja inte där.

För de flesta ändringar är det bättre att först beskriva **vilket beteende som är fel eller vilket behov som saknas** och låta GPT Byggaren avgöra vilka interna delar som behöver ändras.

Det håller fokus på problemet i stället för implementationen.

## Sammanfattning

GPT Byggaren skapar mer än en lång prompt.

Den hjälper till att bygga ett sammanhängande GPT-projekt där:

- instruktioner styr beteendet,
- Knowledge ger specialiserad kunskap,
- capabilities ger nödvändiga förmågor,
- arbetsflöden strukturerar sammansatta uppgifter,
- tester skyddar projektets tekniska kontrakt,
- evals provar viktiga beteenden,
- projektstatus gör utvecklingen återupptagningsbar,
- distributioner gör assistenten användbar i rätt miljö.

Du behöver förstå vad delarna **är till för**, men du behöver inte konstruera dem manuellt.

I nästa kapitel använder vi denna förståelse för något viktigare: att **testa assistenten i realistiska situationer och förbättra den utan att börja om från början**.
