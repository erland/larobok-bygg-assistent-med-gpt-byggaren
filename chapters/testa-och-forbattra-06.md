# 6. Testa, förbättra och fortsätt utveckla

När den första versionen av din GPT finns är det lätt att tänka att projektet nästan är klart.

I praktiken börjar då en av de viktigaste delarna av arbetet: att **prova assistenten i verkliga situationer och förbättra den utifrån det du ser**.

En GPT är inte som ett vanligt formulär där alla möjliga indata kan listas i förväg. Användare formulerar sig olika, dokument ser olika ut och situationer innehåller ofta sådant du inte tänkte på när idén först beskrevs.

Därför är det bättre att se den första fungerande versionen som början på en förbättringscykel:

> **bygg → prova → observera → förbättra → prova igen**

GPT Byggaren hjälper till med själva förändringsarbetet, men du behöver fortfarande avgöra om assistenten fungerar bra i den verklighet där den ska användas.

## Börja med realistiska uppgifter

Det enklaste sättet att testa en GPT är att använda den så som en riktig användare skulle göra.

Om du har byggt en dokumentanalys-GPT bör du alltså inte börja med konstruerade frågor som bara kontrollerar om en viss instruktion finns. Ge den i stället några dokument som liknar sådant den faktiskt kommer att möta.

Välj gärna olika typer av situationer:

- ett enkelt fall där rätt svar är ganska tydligt,
- ett mer omfattande dokument,
- ett fall där påverkan är osäker,
- ett fall där nästan inget är relevant,
- ett fall där information saknas,
- en fråga där användaren uttrycker sig otydligt.

Du försöker inte bevisa att GPT:n fungerar perfekt. Du försöker upptäcka **var den inte fungerar tillräckligt bra ännu**.

## Bedöm mer än om svaret är korrekt

När du provar assistenten är det frestande att bara fråga: "Blev svaret rätt?"

Det är viktigt, men ofta inte tillräckligt.

En användbar GPT behöver också fungera bra som arbetsverktyg.

Fundera därför på exempelvis:

- Hittar den det viktigaste?
- Missar den något som en människa normalt skulle reagera på?
- Lägger den för mycket vikt vid oviktiga detaljer?
- Skiljer den fakta från egna slutsatser?
- Markerar den osäkerhet på ett begripligt sätt?
- Är resultatet lagom långt?
- Är strukturen konsekvent mellan olika körningar?
- Ställer den frågor när information verkligen saknas?
- Undviker den onödiga följdfrågor?
- Håller den sig inom sitt uppdrag?

Detta är ofta mer värdefullt än att försöka bedöma varje enskild formulering.

## Beskriv problemet, inte den tekniska lösningen

När du hittar ett problem kan du återvända till GPT Byggaren och beskriva vad som inte fungerar.

Anta att dokumentanalys-GPT:n ger mycket långa svar där små detaljer får lika stor plats som viktiga konsekvenser.

Du behöver inte säga:

> Ändra instruktion 4.2 och lägg till en prioriteringsregel före output-schemat.

Det räcker bättre att beskriva observationen och önskat beteende:

> När jag provar GPT:n på längre dokument blir svaren för omfattande. Viktiga konsekvenser försvinner bland detaljer. Jag vill att den prioriterar de viktigaste konsekvenserna först och håller övriga observationer kortare.

Det ger GPT Byggaren möjlighet att avgöra **vilka delar av projektet som behöver ändras**.

Det kan handla om instruktioner, arbetsflöde, exempel, evals eller flera delar samtidigt.

Samma princip som när projektet startades gäller alltså fortfarande:

> **Beskriv verksamhetsproblemet så tydligt som möjligt. Låt GPT Byggaren föreslå hur projektet bör förändras.**

## Bra återkoppling är konkret

Jämför två sätt att beskriva ett problem.

Det första är svårt att arbeta vidare från:

> Resultatet känns inte riktigt bra.

Det andra ger betydligt bättre underlag:

> När dokumentet innehåller både ekonomiska och organisatoriska konsekvenser beskriver GPT:n ekonomin utförligt men missar ofta behovet av förändrade arbetssätt. Jag vill att den alltid bedömer båda typerna när underlaget ger stöd för det.

En användbar återkoppling innehåller ofta tre delar:

1. **Situation** – när händer problemet?
2. **Observation** – vad gör GPT:n idag?
3. **Önskat beteende** – hur borde den agera i stället?

Du behöver inte skriva detta som ett formellt formulär. Modellen är bara ett sätt att göra problemet tydligt.

## Ändra en sak utan att förstöra något annat

En förbättring kan ibland skapa ett nytt problem.

Anta att vi ber GPT:n att alltid vara mycket kortfattad. Det kanske löser problemet med långa svar, men samtidigt gör att viktiga reservationer eller förklaringar försvinner.

Det är därför man behöver **regressionstestning**.

Ordet låter tekniskt, men principen är enkel:

> När du har förbättrat något ska du också kontrollera att sådant som redan fungerade fortfarande fungerar.

Om du exempelvis förbättrar prioriteringen av viktiga konsekvenser kan du köra några tidigare testfall igen och kontrollera att GPT:n fortfarande:

- markerar osäkerheter,
- skiljer fakta från slutsatser,
- ignorerar irrelevant material,
- inte börjar fatta beslut åt användaren.

GPT Byggaren kan lägga till eller uppdatera tester och evals när förändringen motiverar det. Du behöver inte själv implementera testsystemet för att dra nytta av principen.

## Korrigeringssteg är en normal del av processen

En utvecklingsplan är inte en checklista som måste följas mekaniskt från första till sista raden.

Under arbetet kan exempelvis en validering visa att något behöver rättas innan nästa planerade steg är meningsfullt.

Då kan flödet se ut så här:

```text
planerat steg
    ↓
kontroll hittar ett problem
    ↓
korrigeringssteg
    ↓
ny kontroll
    ↓
fortsatt utveckling
```

Detta är inte ett misslyckande. Det är snarare ett tecken på att projektet använder sina kvalitetskontroller.

På samma sätt kan GPT Byggaren upptäcka att två planerade steg bör slås ihop eller att ett steg inte längre behövs.

Det viktiga är projektets faktiska tillstånd, inte att stegnumren följs blint.

## Spara den version du faktiskt förbättrar

Efter varje förbättringsvarv bör du spara den senaste projekt-ZIP:en. Den innehåller både projektet och den status GPT Byggaren behöver för att fortsätta arbetet.

Det gör också att du kan byta konversation utan att återskapa historiken. Starta GPT Byggaren igen, bifoga den senaste projekt-ZIP:en och be den fortsätta projektet.

Det viktiga är alltså inte att bevara en lång chatt, utan att fortsätta från **rätt projektversion**.

## När användartestning avslöjar ett större problem

Ibland visar testerna inte bara ett litet fel utan att själva idén behöver justeras.

Kanske försöker GPT:n lösa för många olika uppgifter.

Kanske behöver den mer kunskap än du först trodde.

Kanske kräver resultatet en mänsklig bedömning som inte bör automatiseras.

Eller kanske två olika användargrupper egentligen behöver olika assistenter.

Då är det bättre att ändra projektets inriktning än att försöka laga allt med fler instruktioner.

Exempel:

> Vår GPT ska både göra en snabb första sortering av inkommande dokument och skriva en fullständig konsekvensanalys.

Efter testning kanske det visar sig att dessa två arbetsuppgifter kräver olika detaljnivå, olika frågor och olika resultatformat.

En möjlig förbättring är då att dela upp arbetsflödet eller skapa två tydliga lägen.

GPT Byggaren kan hjälpa till med en sådan omplanering, men beslutet om vad verksamheten faktiskt behöver är fortfarande ditt.

## När är en version tillräckligt bra?

Det finns ingen generell punkt där en GPT blir "färdig för alltid".

En rimlig första version är ofta tillräckligt bra när:

- den löser sitt huvudsakliga användningsfall,
- de viktigaste gränsfallen har provats,
- kända begränsningar är begripliga,
- resultatet är konsekvent nog för målgruppen,
- allvarliga fel inte återkommer i regressionstester,
- användaren förstår vad assistenten kan och inte kan göra.

Det är ofta bättre att nå en avgränsad, fungerande version än att fortsätta lägga till funktioner bara för att de är möjliga.

En bra specialiserad assistent behöver inte kunna allt.

Den behöver vara **pålitligt användbar för sitt uppdrag**.

## Ett praktiskt förbättringsvarv

När du har en egen GPT kan du använda följande enkla rutin:

1. Välj tre till fem realistiska uppgifter.
2. Kör dem som en vanlig användare.
3. Skriv ner de viktigaste problemen du ser.
4. Prioritera ett eller ett fåtal problem åt gången.
5. Beskriv situation, observation och önskat beteende för GPT Byggaren.
6. Låt GPT Byggaren uppdatera projektet.
7. Prova både det förbättrade fallet och några tidigare fall igen.
8. Spara den nya projekt-ZIP:en.

Detta behöver inte bli en stor testorganisation.

För en mindre GPT kan några väl valda verkliga exempel ge mycket värdefull information.

## Det viktigaste från kapitlet

Att bygga en GPT är inte en engångsaktivitet där en perfekt instruktion skrivs från början.

Arbetet blir bättre om du tänker iterativt:

> **prova verkliga uppgifter, observera beteendet och förbättra det viktigaste först.**

GPT Byggaren tar hand om mycket av projektförändringen, teststrukturen och paketeringen. Din viktigaste uppgift är att kunna se om assistenten verkligen hjälper användaren på rätt sätt.

När projektet ligger i sin projekt-ZIP kan utvecklingen dessutom fortsätta i en ny konversation utan att du behöver återskapa hela historiken.

I nästa kapitel lämnar vi utvecklingsloopen och tittar på nästa fråga: **när är en GPT ett experiment, när är den ett riktigt arbetsverktyg och vilken distributionsform passar då bäst?**
