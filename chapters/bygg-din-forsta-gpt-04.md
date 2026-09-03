# 4. Bygg din första GPT

Nu har vi tillräckligt med bakgrund för att göra det praktiskt.

I det här kapitlet använder vi GPT Byggaren i **Chat-läge** för att gå från en idé till ett faktiskt GPT-projekt. Du behöver inte förstå projektets alla tekniska delar. Fokus ligger på arbetsflödet: vad du gör, vad GPT Byggaren gör och vad du behöver kontrollera på vägen.

Vi fortsätter med samma exempel som tidigare: en GPT som hjälper användaren analysera dokument och lyfta fram sådant som kan påverka organisationen.

## Steg 1 – Starta GPT Byggaren

Börja med att hämta den senaste **Chat ZIP-versionen** av GPT Byggaren från projektets GitHub Releases. Filnamnet följer normalt mönstret `gpt-byggaren-chat-<version>.zip`.

Starta sedan en ny ChatGPT-konversation och bifoga ZIP-filen.

Skriv exempelvis:

> Använd denna zip som GPT i denna konversation.

ChatGPT får då tillgång till GPT Byggarens instruktioner och det övriga material som behövs för att använda verktyget.

Det är en viktig detalj: du installerar inte ett program på datorn. Du ger i stället den aktuella ChatGPT-konversationen den kontext som behövs för att agera som GPT Byggaren.

När detta är gjort kan du börja beskriva den GPT du själv vill skapa.

## Steg 2 – Beskriv vad du vill bygga

Du behöver inte börja med en teknisk specifikation.

För vårt exempel kan startprompten vara:

> Jag vill bygga en GPT som hjälper personer i min organisation att analysera remisser och andra dokument. Den ska läsa ett bifogat dokument, identifiera sådant som kan påverka organisationen och ge en kort strukturerad sammanfattning av konsekvenser och frågor som behöver utredas vidare. Den ska vara tydlig med osäkerheter och inte fatta beslut åt användaren.

Detta räcker långt.

Du har beskrivit:

- vem assistenten är till för,
- vilken uppgift den ska hjälpa till med,
- vilken typ av indata den får,
- vilket resultat du vill ha,
- en viktig gräns.

GPT Byggaren kan sedan analysera vad som behövs för att göra idén till en fungerande assistent.

## Steg 3 – Svara på verksamhetsfrågor, inte teknikfrågor

GPT Byggaren kan ibland behöva ställa följdfrågor.

Det viktiga är att skilja mellan två typer av frågor.

Den första typen gäller verksamheten:

- Ska GPT:n ge en orienterande analys eller en formell bedömning?
- Vilka dokumenttyper ska omfattas?
- Vilka användare ska resultatet vara begripligt för?
- Vilka källor får användas?
- Vad får GPT:n absolut inte göra?

Sådana frågor behöver du besvara.

Den andra typen gäller teknisk konstruktion:

- Hur ska projektets interna struktur se ut?
- Behövs schemas?
- Hur ska tester organiseras?
- Hur ska distributionspaketen byggas?

Sådant ska GPT Byggaren normalt hjälpa till att avgöra.

Du behöver alltså inte bli teknisk projektledare bara för att du använder GPT Byggaren.

## Steg 4 – Granska analysen

Innan utvecklingen börjar bör GPT Byggaren sammanfatta hur den har förstått behovet.

Läs denna del noggrant.

Kontrollera framför allt:

- Har den förstått rätt användare?
- Har den förstått huvuduppgiften?
- Har den lagt till funktioner du inte behöver?
- Saknas någon viktig begränsning?
- Är resultatet tänkt att bli användbart i det verkliga arbetet?

Det är lätt att fastna i tekniska formuleringar, men den viktigaste kvalitetskontrollen är mycket enklare:

> **Bygger planen rätt assistent för rätt problem?**

Om svaret är nej bör du korrigera förståelsen innan utvecklingen går vidare.

## Steg 5 – Granska utvecklingsplanen

När behovet är tillräckligt tydligt skapar GPT Byggaren en utvecklingsplan.

Planen kan till exempel innehålla steg för att:

1. definiera assistentens uppdrag,
2. skapa grundinstruktioner,
3. lägga till nödvändig Knowledge,
4. definiera arbetsflödet för dokumentanalys,
5. skapa tester och evals,
6. validera projektet,
7. bygga Chat ZIP och andra distributioner.

Du behöver inte bedöma om varje tekniskt steg är exakt rätt utfört. Däremot bör du kontrollera att planen verkar leda mot den assistent du faktiskt vill ha.

Fråga dig:

- Täcker planen huvuduppgiften?
- Finns testning med?
- Finns de viktigaste riskerna och gränserna med?
- Verkar projektet onödigt avancerat?
- Saknas något som användaren verkligen behöver?

Om planen ser rimlig ut kan utvecklingen börja.

## Steg 6 – Skapa första projekt-ZIP:en

Be GPT Byggaren genomföra första steget.

Du kan skriva:

> Gör första steget och ge mig resultatet som en zip.

När projektet har skapats får du en **projekt-ZIP**.

Spara den.

Det här är nu den viktigaste filen i utvecklingsarbetet. Projekt-ZIP:en innehåller projektets aktuella tillstånd och används som grund för nästa utvecklingssteg.

Du behöver normalt inte packa upp ZIP-filen och börja redigera dess innehåll manuellt. Den viktigaste uppgiften för dig är att hålla reda på den senaste versionen.

## Steg 7 – Fortsätt med nästa steg

När du vill fortsätta kan instruktionen vara mycket enkel:

> Gör nästa steg och ge mig en uppdaterad zip.

GPT Byggaren ska då läsa projektets aktuella status och avgöra vilket arbete som är nästa rimliga steg.

Efter genomfört arbete får du en ny projekt-ZIP.

Arbetsmönstret blir därför:

> **senaste projekt-ZIP → nästa steg → kontroll → ny projekt-ZIP**

Du behöver inte själv hålla reda på att exempelvis "steg 7 måste följas av steg 8". Om ett test visar ett problem kan GPT Byggaren behöva göra ett korrigeringssteg först.

Det är en av styrkorna med att projektstatus finns i själva projektet.

## Steg 8 – Läs vad som faktiskt förändrades

Även om du inte behöver förstå varje teknisk fil bör du läsa sammanfattningen efter varje större steg.

Titta särskilt efter:

- vad som har lagts till,
- vad som har ändrats,
- vilka antaganden som gjorts,
- om något fortfarande är öppet,
- vilket nästa steg rekommenderas.

Det gör att du kan ingripa tidigt om projektet börjar utvecklas i fel riktning.

Ett bra arbetssätt är att inte bara svara "fortsätt" reflexmässigt. När något viktigt för verksamheten förändras bör du bedöma om det fortfarande stämmer med ditt mål.

## Steg 9 – Prova den första användbara versionen

Efter några utvecklingssteg kommer projektet till en punkt där det går att prova assistenten som användare.

Då är det dags att bygga eller använda en **Chat ZIP** för den GPT som projektet skapar.

Starta en ny ChatGPT-konversation, bifoga Chat ZIP-filen och be ChatGPT använda den som GPT-kontext.

Testa sedan med ett realistiskt dokument.

För vårt exempel kan du kontrollera:

- hittar assistenten de viktigaste delarna?
- sammanfattar den på rätt detaljnivå?
- skiljer den fakta från bedömning?
- lyfter den osäkerheter?
- blir resultatet faktiskt användbart för målgruppen?

Detta är viktigare än att bara fråga om projektets automatiska tester är gröna.

Automatiska tester kan kontrollera många egenskaper, men bara en verklig användare kan avgöra om assistenten hjälper till med det verkliga arbetet.

## Steg 10 – Ge återkoppling som beskriver problemet

Om något inte fungerar behöver du inte alltid tala om exakt hur det ska lösas.

Skriv vad du observerar.

Exempel:

> Analysen blir för lång. Jag vill att den viktigaste påverkan ska komma först och att detaljer bara tas med när de behövs för att förstå slutsatsen.

Eller:

> GPT:n verkar ibland anta att en formulering i dokumentet påverkar organisationen trots att kopplingen är osäker. Jag vill att sådana fall markeras tydligt som något som behöver verifieras.

Detta är ofta bättre än att själv försöka skriva om de tekniska instruktionerna.

Du beskriver **beteendet som behöver förbättras**. GPT Byggaren kan sedan avgöra vilka delar av projektet som behöver ändras och vilka tester som bör uppdateras.

## Steg 11 – Fortsätt i en ny konversation

En lång utvecklingskonversation behöver inte leva för alltid.

När du vill fortsätta i en ny konversation gör du i princip samma sak som tidigare:

1. Starta en ny konversation.
2. Bifoga GPT Byggarens Chat ZIP.
3. Bifoga den senaste projekt-ZIP:en för GPT:n du utvecklar.
4. Be GPT Byggaren fortsätta projektet.

Exempel:

> Fortsätt utveckla detta GPT-projekt och gör nästa rekommenderade steg.

Eftersom projektstatus och viktiga beslut finns i projektet behöver du normalt inte återberätta hela historiken.

Det är därför viktigt att alltid utgå från **senaste projekt-ZIP:en**.

## Ett komplett arbetsflöde

Hela processen kan sammanfattas så här:

1. Hämta GPT Byggarens Chat ZIP.
2. Starta GPT Byggaren i en ny konversation.
3. Beskriv vilket problem din GPT ska lösa.
4. Besvara eventuella verksamhetsfrågor.
5. Granska GPT Byggarens analys.
6. Granska utvecklingsplanen.
7. Be GPT Byggaren skapa första projekt-ZIP:en.
8. Fortsätt stegvis med den senaste projekt-ZIP:en.
9. Prova den framväxande GPT:n med realistiska exempel.
10. Beskriv problem och förbättringsbehov.
11. Fortsätt tills assistenten är tillräckligt bra för sitt syfte.
12. Bygg den distribution du vill använda.

Det kan se ut som många steg när de listas så här, men i praktiken består arbetet till stor del av en konversation.

Du beskriver vad du vill åstadkomma, granskar viktiga beslut och ber sedan GPT Byggaren fortsätta.

## Ett misstag att undvika: bygg allt innan du provar

Det är frestande att låta hela utvecklingsplanen köras färdigt innan du testar något.

Det är sällan det bästa arbetssättet.

Om GPT Byggaren har missförstått en central del av användningsfallet är det bättre att upptäcka det efter några steg än efter hela projektet.

Prova därför assistenten när det finns en första meningsfull version.

Frågan är inte:

> Är GPT:n färdig?

utan snarare:

> Har vi byggt tillräckligt mycket för att lära oss något genom att använda den?

Det gör utvecklingen både snabbare och mer träffsäker.

## Praktiskt moment: starta ditt projekt

Om du följer boken praktiskt är det nu dags att skapa ditt eget projekt.

Utgå från GPT-kortet från kapitel 2.

Starta GPT Byggaren i Chat-läge och ge den en kort beskrivning av din idé.

När analysen kommer tillbaka, kontrollera tre saker innan du går vidare:

**1. Problemförståelse**  
Har GPT Byggaren förstått vilket arbete som ska underlättas?

**2. Resultat**  
Har den förstått vad användaren behöver få tillbaka?

**3. Gränser**  
Har de viktigaste begränsningarna följt med?

Om svaret är ja kan du låta GPT Byggaren skapa utvecklingsplanen och därefter första projekt-ZIP:en.

Spara den senaste ZIP-filen. Den är startpunkten för resten av arbetet.

## Kort sammanfattning

Att bygga en GPT med GPT Byggaren är i första hand ett **iterativt samtal om behov och kvalitet**, inte en övning i att manuellt skriva alla tekniska komponenter.

Du startar GPT Byggaren med dess Chat ZIP, beskriver din GPT-idé och granskar hur behovet har förståtts. Därefter skapas en utvecklingsplan och en projekt-ZIP som utvecklas steg för steg.

Den viktigaste arbetsrytmen är enkel:

> **Beskriv behovet → granska → bygg ett steg → prova → förbättra → fortsätt.**

I nästa kapitel tittar vi på vad GPT Byggaren faktiskt skapar inne i projektet. Målet är inte att du ska börja redigera allt manuellt, utan att du ska förstå de viktigaste byggstenarna och varför de finns.
