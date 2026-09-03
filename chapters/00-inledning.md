# Inledning

ChatGPT är lätt att börja använda. Du ställer en fråga, får ett svar och fortsätter samtalet därifrån. För många uppgifter räcker det långt.

Men efter ett tag uppstår ofta ett annat behov. Du kanske återkommer till samma typ av analys, använder samma instruktioner, bifogar liknande underlag och vill ha resultatet presenterat på ungefär samma sätt varje gång. Då är det naturligt att gå från en vanlig konversation till en mer specialiserad AI-assistent.

Den här boken handlar om hur du gör det med hjälp av **GPT Byggaren**.

Målet är inte att göra dig till expert på promptdesign, scheman, testautomatisering eller intern GPT-arkitektur. Målet är att du ska förstå vad en specialiserad AI-assistent är, kunna beskriva vad du vill att den ska hjälpa till med och sedan praktiskt kunna använda GPT Byggaren för att ta fram den.

## Vad du kommer att lära dig

När du har läst boken ska du kunna:

- skilja mellan vanlig användning av ChatGPT och en specialiserad AI-assistent,
- formulera ett konkret användningsfall som lämpar sig för en GPT,
- använda GPT Byggaren för att analysera behovet och skapa en utvecklingsplan,
- bygga och vidareutveckla en GPT steg för steg i en vanlig ChatGPT-konversation,
- förstå de viktigaste delarna som GPT Byggaren skapar åt dig,
- testa och förbättra assistenten utifrån verklig användning,
- avgöra när en Chat ZIP räcker och när andra distributionsformer kan vara intressanta.

Det centrala genom hela boken är arbetsfördelningen mellan dig och GPT Byggaren.

Du behöver framför allt beskriva **vad du vill åstadkomma**. GPT Byggaren hjälper till att avgöra **hur GPT-projektet bör utformas, struktureras, testas och paketeras**.

## Vem boken är till för

Boken är skriven för dig som redan har använt ChatGPT men som inte behöver ha byggt en egen GPT tidigare.

Du förväntas kunna starta en konversation, skriva instruktioner med vanligt språk och bifoga en fil. Du behöver däremot inte kunna YAML, JSON Schema, GitHub Actions eller testautomatisering.

Tekniska begrepp introduceras först när de behövs. När vi tittar på exempelvis instruktioner, kunskapsunderlag, förmågor och tester är syftet att du ska förstå deras roll och kunna bedöma resultatet – inte att du ska behöva bygga allt manuellt.

## Bokens huvudspår: GPT Byggaren i Chat-läge

GPT Byggaren kan användas på olika sätt. I den här boken fokuserar vi främst på **Chat-läget**.

Det innebär att du använder en Chat ZIP med GPT Byggaren i en vanlig ChatGPT-konversation. Du bifogar ZIP-filen, ber ChatGPT använda den som GPT Byggaren och beskriver sedan den assistent du vill skapa.

Arbetet blir ungefär så här:

1. Du beskriver idén och problemet du vill lösa.
2. GPT Byggaren analyserar behovet.
3. Du får en utvecklingsplan.
4. GPT Byggaren skapar ett GPT-projekt.
5. Du fortsätter utvecklingen steg för steg.
6. GPT:n testas, förbättras och paketeras för användning.

En viktig poäng är att du inte behöver hålla hela projektet i huvudet eller i chatthistoriken. Projektets struktur och status lagras i projektet. Det gör att du kan spara den senaste projekt-ZIP:en och fortsätta arbetet senare, även i en ny konversation.

## Ett exempel följer med genom boken

För att göra resonemangen konkreta använder vi ett enkelt återkommande exempel.

Tänk dig att du ofta får dokument som du behöver läsa igenom för att förstå vad som är relevant för din organisation. Du vill därför skapa en assistent som kan:

- ta emot ett dokument,
- identifiera de delar som kan vara viktiga,
- sammanfatta dem kort,
- strukturera resultatet på ett konsekvent sätt.

Det är medvetet ett enkelt exempel. Syftet är inte att bygga den mest avancerade GPT:n, utan att visa hela vägen från ett återkommande problem till en fungerande och förbättringsbar assistent.

Du kan följa samma steg med en egen idé medan du läser.

## Så är boken upplagd

Vi börjar med vad en AI-assistent är och hur ett återkommande behov blir en tydlig GPT-idé. Därefter följer det praktiska huvudspåret: GPT Byggaren, utvecklingsplanen och den stegvisa utvecklingen i Chat-läge.

Först när du har sett processen i praktiken öppnar vi motorhuven och tittar på instruktioner, kunskap, förmågor och tester. Boken avslutas med förbättring, distribution och förvaltning.

## Hur du får mest nytta av boken

Läs gärna boken med ChatGPT tillgängligt bredvid dig.

När ett kapitel innehåller ett praktiskt moment kan du prova det direkt. Du behöver inte använda exakt samma exempel som i boken. Det är ofta mer lärorikt att utgå från ett verkligt problem som du själv återkommer till.

Försök samtidigt att inte börja med en alltför stor idé. En första GPT blir lättare att förstå, testa och förbättra om den har ett tydligt uppdrag.

En bra utgångspunkt är därför inte:

> Jag vill ha en AI som hjälper mig med allt i mitt arbete.

utan något i stil med:

> Jag vill ha en GPT som analyserar den här typen av dokument och hjälper mig identifiera vad jag behöver agera på.

Det är där vi börjar.
