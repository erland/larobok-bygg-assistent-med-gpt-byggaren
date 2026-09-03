# 3. GPT Byggaren

I förra kapitlet formulerade vi en GPT-idé utifrån målgrupp, uppgift, indata, utdata och gränser.

Det är ungefär där GPT Byggaren tar vid.

Tanken är att du inte ska behöva översätta verksamhetsbehovet till en fullständig teknisk konstruktion på egen hand. Du beskriver främst **vad assistenten ska hjälpa till med**. GPT Byggaren hjälper sedan till att avgöra **hur projektet bör byggas**.

Det betyder inte att du lämnar över alla beslut. Men arbetsfördelningen blir tydligare.

> **Du ansvarar för behovet och för att bedöma om resultatet blir användbart. GPT Byggaren ansvarar för mycket av konstruktionen, strukturen och kvalitetssäkringen.**

## Från idé till utvecklingsprojekt

Anta att du ger GPT Byggaren idén från förra kapitlet:

> Jag vill bygga en GPT som hjälper personer i min organisation att analysera remisser. Den ska läsa ett bifogat dokument, identifiera sådant som kan påverka organisationen och ge en kort strukturerad sammanfattning av konsekvenser och frågor som behöver utredas vidare. Den ska vara tydlig med osäkerheter och inte fatta beslut åt användaren.

GPT Byggarens uppgift är då inte bara att skriva en lång instruktionstext.

Den behöver först förstå vad som faktiskt krävs.

Den kan exempelvis behöva bedöma:

- vilken målgrupp assistenten är gjord för,
- vilket arbetsflöde den ska följa,
- vilka typer av dokument den behöver kunna hantera,
- om särskild Knowledge behövs,
- om webbsökning eller andra capabilities behövs,
- hur resultatet ska struktureras,
- vilka risker eller gränser som behöver byggas in,
- hur beteendet bör testas,
- hur assistenten bör paketeras för användning.

Du behöver alltså inte börja med frågor som "ska jag ha ett schema?" eller "hur ska projektstrukturen se ut?".

GPT Byggaren kan ta många sådana tekniska beslut utifrån användningsfallet.

## Vad behöver du själv bestämma?

Det finns ändå beslut som ett byggverktyg inte bör gissa sig till.

Om GPT Byggaren frågar:

> Ska analysen vara en första orientering eller en formell juridisk bedömning?

är det ett verksamhetsbeslut. Svaret påverkar vad assistenten får göra och hur försiktigt den måste uttrycka sig.

Samma sak gäller frågor som:

- Vem är den egentliga användaren?
- Vad är ett godkänt resultat?
- Vilka källor får användas?
- Vilka uppgifter är känsliga?
- När ska assistenten stanna och be en människa ta över?
- Vad ska uttryckligen ligga utanför GPT:ns uppdrag?

Däremot behöver du normalt inte bestämma sådant som projektets interna filstruktur eller exakt hur en automatisk kontroll ska implementeras.

En användbar tumregel är:

> **Beslut om syfte, ansvar, kvalitet och gränser är dina. Beslut om teknisk realisering kan GPT Byggaren ofta hjälpa till med.**

## Först analys, sedan plan

GPT Byggaren arbetar stegvis.

Efter att du beskrivit vad du vill bygga analyserar den behovet. När det är tillräckligt tydligt tar den fram en utvecklingsplan anpassad till just projektet.

Planen kan exempelvis innehålla steg för att:

1. definiera assistentens uppdrag,
2. strukturera instruktionerna,
3. lägga till nödvändig Knowledge,
4. definiera viktiga arbetsflöden,
5. skapa tester och evals,
6. validera projektet,
7. bygga distributionspaket.

Det viktiga är att planen inte ska ses som en stel checklista.

Om ett test senare visar att något behöver rättas kan GPT Byggaren lägga in ett korrigeringssteg. Om ett planerat steg visar sig onödigt kan det hoppas över eller slås ihop med något annat.

Det gör utvecklingsplanen till en **riktning för arbetet**, inte ett kontrakt som måste följas mekaniskt.

## Projekt-ZIP: utvecklingsprojektet

När GPT Byggaren börjar genomföra planen skapas normalt en **projekt-ZIP**.

Det är den viktigaste filen under själva utvecklingen.

Projekt-ZIP:en innehåller inte bara den färdiga GPT:n. Den innehåller hela utvecklingsprojektet: instruktioner, Knowledge, status, tester, dokumentation, byggstöd och andra filer som behövs för att fortsätta arbetet.

Du kan tänka på den som:

> **arbetsmappen för GPT-projektet, paketerad som en enda fil**

Det är projekt-ZIP:en du sparar när du vill fortsätta utveckla assistenten senare.

Den gör också att projektet inte behöver vara beroende av en enda lång ChatGPT-konversation. Om du börjar i en ny konversation kan du bifoga den senaste projekt-ZIP:en och be GPT Byggaren fortsätta där projektet befinner sig.

Projektstatusen ligger alltså i själva projektet, inte bara i chathistoriken.

## Chat ZIP: assistenten i en vanlig konversation

När projektet börjar bli användbart kan GPT Byggaren skapa en **Chat ZIP**.

Det är en runtime-version av assistenten som är avsedd att bifogas i en vanlig ChatGPT-konversation.

Arbetsmodellen är enkel:

1. Starta en ny konversation.
2. Bifoga Chat ZIP-filen.
3. Be ChatGPT använda ZIP-filen som den aktuella GPT-kontexten.
4. Börja använda den specialiserade assistenten.

Detta är bokens huvudspår.

En fördel är att samma grundidé som vi använder för GPT Byggaren också kan användas för GPT:n vi bygger: en ZIP-fil kan bära med sig instruktioner, Knowledge och annan struktur som gör en vanlig konversation till en mer specialiserad arbetsmiljö.

För dig som användare är det viktigaste att skilja Chat ZIP från projekt-ZIP:

**Projekt-ZIP** använder du för att **utveckla** GPT:n.

**Chat ZIP** använder du för att **köra** GPT:n i en konversation.

## Custom GPT ZIP: material för GPT Builder

GPT Byggaren kan också skapa en **Custom GPT ZIP**.

Den innehåller material som är anpassat för att skapa eller uppdatera en Custom GPT i ChatGPT:s GPT Builder.

Det är alltså ytterligare ett sätt att distribuera samma grundläggande assistentidé.

En Custom GPT och en Chat ZIP behöver inte alltid vara tekniskt identiska. Plattformarna kan ha olika begränsningar för exempelvis hur mycket material som får plats eller hur olika funktioner kan användas.

GPT Byggaren försöker därför utgå från samma grundläggande beteende och sedan anpassa distributionen till respektive körsätt.

I den här boken behöver vi inte gå djupare än så ännu. Huvudspåret är Chat ZIP eftersom det gör hela kedjan enkel att förstå och prova.

## Tre ZIP-filer – tre olika syften

De tre paketen är lätta att blanda ihop. Följande modell räcker långt:

| Paket | Används till | Tänk på det som |
|---|---|---|
| Projekt-ZIP | fortsatt utveckling | hela arbetsprojektet |
| Chat ZIP | köra GPT:n i en vanlig ChatGPT-konversation | den körbara chatversionen |
| Custom GPT ZIP | skapa eller uppdatera en Custom GPT | distributionsunderlag för GPT Builder |

För den praktiska processen i den här boken räcker det nästan att komma ihåg två saker:

> **Utveckla med projekt-ZIP. Använd i chatten med Chat ZIP.**

Custom GPT återkommer kort senare när vi diskuterar hur en färdig assistent kan distribueras.

## Det stegvisa arbetssättet

En viktig egenskap hos GPT Byggaren är att du inte behöver försöka skapa hela GPT:n i ett enda jättestort uppdrag.

Efter att utvecklingsplanen finns kan arbetet fortsätta stegvis.

En typisk instruktion kan vara:

> Gör nästa steg och ge mig en uppdaterad zip.

GPT Byggaren läser då projektets aktuella status, avgör vilket steg som bör genomföras, gör arbetet, uppdaterar status och lämnar tillbaka en ny komplett projekt-ZIP.

Nästa gång utgår du från den nya filen.

Arbetssättet liknar därför mer vanlig iterativ utveckling än att försöka skriva "den perfekta prompten" vid första försöket.

Det ger också en viktig trygghet: när en senare ändring behövs fortsätter du från ett faktiskt projekt i stället för att försöka återskapa allt från minnet.

## GPT Byggaren ersätter inte ditt omdöme

Det kan vara lockande att tänka att byggverktyget nu löser hela problemet automatiskt.

Så fungerar det inte.

GPT Byggaren kan hjälpa till att skapa en välstrukturerad lösning, men du behöver fortfarande bedöma om lösningen passar det verkliga arbetet.

När du granskar resultatet är några enkla frågor viktigare än att förstå varje teknisk fil:

- Har GPT Byggaren förstått uppgiften rätt?
- Är målgruppen rätt beskriven?
- Saknas något viktigt underlag?
- Är resultatet tänkt att se ut på rätt sätt?
- Finns de viktigaste gränserna med?
- Verkar planen bygga rätt assistent, inte bara en tekniskt avancerad assistent?

Det är här din verksamhetskunskap har störst värde.

## En mental modell för hela processen

Nu kan vi sätta ihop flödet från förra kapitlet med GPT Byggaren:

> **Problem → GPT-idé → analys → utvecklingsplan → projekt-ZIP → stegvis utveckling → testad GPT → Chat ZIP eller Custom GPT**

Det är i praktiken bokens huvudflöde.

Du behöver förstå vad som händer i varje del, men du behöver inte manuellt konstruera varje teknisk komponent.

I nästa kapitel gör vi detta på riktigt. Då startar vi GPT Byggaren i Chat-läge, beskriver en GPT-idé, granskar planen och börjar bygga den första versionen.

## Reflektion

Titta på GPT-kortet du gjorde i förra kapitlet.

Markera vilka delar som tydligt är **dina verksamhetsbeslut**. Det kan exempelvis vara målgrupp, syfte, kvalitetskrav och gränser.

Fundera sedan på vilka frågor du gärna skulle låta GPT Byggaren hjälpa dig med. Det kan exempelvis vara hur instruktionerna ska struktureras, vilken Knowledge som behövs och hur assistenten bör testas.

Om uppdelningen känns tydlig har du förstått den viktigaste idén med GPT Byggaren.

## Kort sammanfattning

GPT Byggaren hjälper dig gå från en beskriven GPT-idé till ett strukturerat, testbart och distribuerbart GPT-projekt. Du ansvarar för behovet och bedömningen av nyttan; GPT Byggaren tar ett större ansvar för den tekniska realiseringen.

Nästa steg är att använda arbetsflödet praktiskt och bygga den första GPT:n.
