# Typografi- och layoutrevision

## Syfte

Slutlig visuell revision av PDF- och EPUB-exporterna efter färdigt och språkgranskat manus.

## Genomförda justeringar

- PDF använder nu A4 med jämna 25 mm marginaler och något luftigare styckerytm.
- Titelsidan är en egen sida med centrerad titel, undertitel och författare.
- PDF-innehållsförteckningen är begränsad till H1/kapitelnivå för att förbli kort och överskådlig.
- Varje H1, inklusive inledningen och kapitel 1-7, börjar på ny sida.
- Kapitelrubriker är centrerade och tydligt större än underrubrikerna.
- H2/H3 har stramats upp så att hierarkin är tydlig utan att underrubriker konkurrerar med kapitelrubriken.
- Blockcitat och praktiska prompt-/exempelblock visas som diskreta tonade rutor med vänsterlinje i PDF och EPUB.
- Kod-/textblock tillåts radbrytas så att långa rader inte går utanför sidan eller läsytan.
- Tabeller har ökad cellhöjd/radluft i PDF samt diskreta radavskiljare och cellpadding i EPUB.
- EPUB-titelsidan har centrerad titel, undertitel och författare och EPUB:s navigerbara innehållsförteckning ligger kvar på endast H1-nivå.
- EPUB har ingen separat synlig innehållsförteckning i löptexten.

## Verifiering

PDF har byggts med XeLaTeX och renderats till sidbilder för visuell kontroll. Kontrollerna omfattade titelsida, innehållsförteckning, kapitelstarter, tabeller, promptblock, rubriker och vanliga textsidor. Ingen klippning eller överlappning noterades.

EPUB har packats upp och kontrollerats avseende titelsida, H1-baserad navigations-TOC, separata kapitel-filer och stylesheet.
