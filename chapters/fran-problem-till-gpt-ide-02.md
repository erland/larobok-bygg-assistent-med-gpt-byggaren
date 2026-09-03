# 2. Från problem till GPT-idé

Det är lätt att börja i fel ände när man vill skapa en egen GPT.

Man börjar fundera på instruktioner, filer, webbsökning eller vilka verktyg assistenten behöver. Men innan något av det är viktigt behöver en enklare fråga vara besvarad:

**Vilket återkommande problem ska assistenten hjälpa till att lösa?**

En bra GPT börjar sällan med teknik. Den börjar med ett arbete som någon vill göra enklare, snabbare eller mer konsekvent.

I det här kapitlet går vi från ett löst behov till en tillräckligt tydlig GPT-idé för att GPT Byggaren ska kunna ta över mycket av resten.

## Börja med arbetet, inte med GPT:n

Anta att du ofta får dokument som behöver läsas igenom för att avgöra om de påverkar din organisation.

En första idé kan vara:

> Jag vill ha en GPT som analyserar dokument.

Det är en start, men fortfarande ganska otydligt. Nästan alla typer av dokument kan analyseras på många olika sätt.

En bättre beskrivning är:

> Jag vill ha en GPT som hjälper mig läsa remisser och andra styrande dokument, identifierar sådant som kan påverka min organisation och sammanfattar de viktigaste konsekvenserna.

Nu börjar det bli möjligt att förstå uppgiften.

Det viktiga är inte att formuleringen är perfekt. Det viktiga är att den beskriver **arbetet och det önskade resultatet**.

## Fem frågor räcker långt

För de flesta första GPT-idéer kommer du långt genom att svara på fem frågor.

### 1. Vem ska använda assistenten?

En GPT som är gjord för en jurist behöver kanske resonera annorlunda än en som är gjord för en chef eller en kundtjänstmedarbetare.

Frågan behöver inte besvaras med en exakt yrkestitel. Det kan räcka med:

- jag själv,
- personer i mitt team,
- handläggare,
- utvecklare,
- chefer,
- kunder.

För vårt exempel kan målgruppen vara:

> Personer som behöver göra en första strukturerad bedömning av hur ett dokument påverkar organisationen.

### 2. Vilken uppgift ska den hjälpa till med?

Beskriv uppgiften som ett arbete, inte som en teknisk funktion.

Mindre bra:

> GPT:n ska använda filer och skapa Markdown.

Bättre:

> GPT:n ska läsa ett dokument, identifiera relevanta delar och sammanfatta vad organisationen behöver uppmärksamma.

Den senare formuleringen säger vad användaren vill få gjort. Hur det sedan implementeras kan GPT Byggaren hjälpa till att avgöra.

### 3. Vilket underlag får den?

Tänk på vad användaren faktiskt kommer att ge assistenten.

Det kan till exempel vara:

- ett PDF-dokument,
- text inklistrad i chatten,
- en webbsida,
- en kalkylfil,
- källkod,
- flera dokument som ska jämföras,
- interna riktlinjer som ska användas som referens.

I vårt exempel kan svaret vara:

> Användaren bifogar ett dokument som ska analyseras. Assistenten kan också behöva känna till några fasta beskrivningar av organisationens uppdrag och ansvarsområden.

Den formuleringen börjar redan ge ledtrådar om att GPT:n kan behöva både filhantering och särskild Knowledge. Du behöver ändå inte bestämma den tekniska lösningen själv.

### 4. Hur ska resultatet se ut?

Det är ofta lättare att beskriva ett bra resultat än att beskriva hur assistenten ska arbeta.

Exempel:

> Jag vill ha en kort sammanfattning, de viktigaste konsekvenserna, vilka områden som berörs och vilka frågor som behöver utredas vidare.

Detta är mycket mer användbart än att bara säga att GPT:n ska "analysera noggrant".

Ett tydligt önskat resultat hjälper både GPT Byggaren och den färdiga assistenten att förstå vad som faktiskt är viktigt.

### 5. Vad ska assistenten inte göra?

Avgränsningar är minst lika viktiga som funktioner.

I dokumentexemplet kan en viktig gräns vara:

> Assistenten ska inte presentera osäkra slutsatser som fakta och ska inte fatta beslut åt användaren.

Andra vanliga gränser kan vara:

- inte lämna juridiska slutbedömningar,
- inte ändra filer utan uttryckligt uppdrag,
- inte använda externa källor när endast bifogat material ska bedömas,
- inte försöka göra flera olika arbetsuppgifter som egentligen borde vara separata.

Gränser gör GPT-idén tydligare och minskar risken att projektet växer åt alla håll.

## Ett enkelt GPT-kort

Du behöver inte skriva en lång kravspecifikation. Ett litet "GPT-kort" räcker ofta för att komma vidare.

För vårt exempel kan det se ut så här:

**Målgrupp:** personer som gör en första bedömning av dokument som kan påverka organisationen.

**Uppgift:** läsa dokument och identifiera relevanta delar, konsekvenser och frågor för fortsatt analys.

**Indata:** främst bifogade dokument, ibland kompletterat med fast bakgrundskunskap om organisationen.

**Utdata:** en kort strukturerad sammanfattning med viktigaste påverkan, berörda områden och öppna frågor.

**Gränser:** inte fatta beslut åt användaren och inte framställa osäkra slutsatser som säkra fakta.

Det är redan tillräckligt bra för att börja arbeta med GPT Byggaren.

## Du behöver inte lösa konstruktionen själv

När du har formulerat användningsfallet är det frestande att fortsätta med frågor som:

- Behöver jag Knowledge-filer?
- Ska den kunna söka på webben?
- Hur långa ska instruktionerna vara?
- Behöver jag schemas?
- Hur ska den testas?
- Ska den bli en Custom GPT eller användas som Chat ZIP?

Det är relevanta frågor, men de behöver inte vara dina första frågor.

GPT Byggaren är till för att hjälpa till med just den översättningen: från **vad du vill åstadkomma** till **hur GPT-projektet bör utformas**.

Du behöver därför framför allt kunna bedöma om GPT Byggaren har förstått verksamhetsbehovet rätt.

Det är en viktig arbetsfördelning:

> Du beskriver problemet och bedömer om lösningen passar behovet. GPT Byggaren hjälper till att konstruera lösningen.

## Undvik att göra GPT:n för bred

En vanlig första idé låter ungefär så här:

> Jag vill ha en GPT som hjälper mig med allt i mitt arbete.

Det låter attraktivt, men ger ofta en sämre assistent.

Ju fler olika arbetsuppgifter som blandas ihop, desto svårare blir det att:

- ge tydliga instruktioner,
- veta vilket resultat som är rätt,
- välja relevant Knowledge,
- testa beteendet,
- förbättra assistenten när något fungerar dåligt.

En bättre start är ofta att välja **ett återkommande arbetsflöde**.

Exempelvis:

- analysera en remiss,
- granska ett kodprojekt,
- jämföra produkter,
- sammanfatta en viss typ av rapport,
- skapa ett första utkast enligt en bestämd struktur.

När den assistenten fungerar kan den utvecklas vidare, eller kompletteras med andra specialiserade assistenter.

## Tänk i arbetsflöden

Ett bra sätt att pröva om en GPT-idé är tillräckligt konkret är att föreställa sig ett normalt användningstillfälle.

För dokumentanalysen kan arbetsflödet vara:

1. Användaren bifogar ett dokument.
2. Assistenten identifierar vilken typ av dokument det är.
3. Den läser efter sådant som är relevant för organisationen.
4. Den skiljer tydliga fakta från egna bedömningar.
5. Den sammanfattar påverkan i en återkommande struktur.
6. Den pekar ut sådant som behöver granskas vidare av en människa.

Det här är fortfarande inte en teknisk specifikation. Men det beskriver hur arbetet bör kännas för användaren.

Det är ofta precis lagom mycket information för nästa steg.

## När är idén tillräckligt bra?

Du behöver inte vänta tills alla detaljer är lösta.

Din GPT-idé är vanligtvis tillräckligt tydlig när du kan beskriva:

- vem som ska använda den,
- vilken återkommande uppgift den ska hjälpa till med,
- vilket underlag den normalt får,
- vilket resultat användaren behöver,
- några viktiga gränser.

Om något fortfarande är oklart kan GPT Byggaren hjälpa dig upptäcka det under analysen.

Målet är alltså inte att skriva den perfekta prompten innan du börjar. Målet är att ge GPT Byggaren **ett begripligt problem att arbeta vidare med**.

## Praktiskt moment: formulera din första idé

Ta uppgiften du funderade på i slutet av förra kapitlet och fyll i följande fem rader:

**Målgrupp:**

**Uppgift:**

**Indata:**

**Utdata:**

**Gränser:**

Försök hålla varje svar till en eller två meningar.

Skriv sedan en enkel startprompt utifrån dem. Den behöver inte innehålla alla detaljer ordagrant.

Till exempel:

> Jag vill bygga en GPT som hjälper personer i min organisation att analysera remisser. Den ska läsa ett bifogat dokument, identifiera sådant som kan påverka organisationen och ge en kort strukturerad sammanfattning av konsekvenser och frågor som behöver utredas vidare. Den ska vara tydlig med osäkerheter och inte fatta beslut åt användaren.

Det är en fullt rimlig startpunkt.

## Kort sammanfattning

En bra GPT-idé börjar med ett återkommande problem, inte med teknik.

Du kommer långt genom att beskriva fem saker: **målgrupp, uppgift, indata, utdata och gränser**. Det behöver inte bli en fullständig kravspecifikation.

När användningsfallet är tillräckligt tydligt kan GPT Byggaren hjälpa till att avgöra hur assistenten bör struktureras, vilken kunskap och vilka capabilities som behövs och hur projektet bör utvecklas.

I nästa kapitel tittar vi därför närmare på GPT Byggaren själv och på hur arbetsfördelningen mellan dig och byggverktyget fungerar.
