# Faktagranskning mot GPT Byggaren

Datum: 2026-09-03

## Granskningsbas

Boken har granskats mot aktuell `main` i `erland/gpt-byggaren` samt den senast publicerade releasen vid granskningstillfället, **v1.2.1** (publicerad 2026-09-02).

Primära källor:

- `README.md`
- `docs/getting-started.md`
- `docs/test-model.md`
- `docs/resume-flow.md`
- GitHub Release `v1.2.1`

## Bekräftat

- Huvudflödet idé → analys → utvecklingsplan → projekt-ZIP → stegvis utveckling → distribution stämmer med GPT Byggaren.
- Projekt-ZIP, Chat ZIP och Custom GPT ZIP har de roller som boken beskriver.
- Chat ZIP kan bifogas i en vanlig ChatGPT-konversation och användas som GPT-kontext.
- Projekt kan återupptas utan tidigare chathistorik genom projektets maskinläsbara kontrakt och status, där `project-status.yaml` är primär statuskälla.
- Utvecklingsplanen är vägledande och kan kompletteras med korrigeringssteg eller omplaneras.
- Testmodellen skiljer mellan deterministiska tester och beteendeevalueringar (evals), med ytterligare lager för bland annat build, distribution, runtime smoke tests och regression.
- Nya projekt har normalt GitHub-stöd med `README.md`, CI och release-workflow; GitHub kan väljas bort för uttryckligen GitHub-fria projekt.
- Releaseversion kan härledas från GitHub Release-taggen och releaseflödet kan publicera projekt-ZIP, Chat ZIP, Custom GPT ZIP, checksummor och leveransmanifest.

## Justeringar i boken

1. Kapitel 5 har preciserats så att tester inte framställs som enbart strukturkontroller. Deterministiska tester omfattar även exempelvis scripts, build, distribution och runtime-egenskaper.
2. Kapitel 7 har justerats så att GitHub-stöd beskrivs som normal standard för nya GPT Byggaren-projekt, snarare än bara en möjlig förberedelse.
3. Kapitel 4 anger det normala filnamnsmönstret för GPT Byggarens Chat ZIP utan att hårdkoda en viss releaseversion i lärobokstexten.

## Notering om versionsuppgifter

Bokens löptext undviker avsiktligt att ange en specifik GPT Byggaren-version eftersom den informationen snabbt blir gammal. Vid denna granskning var senaste GitHub Release v1.2.1. Projektets README innehåller samtidigt en äldre statusformulering som nämner v1.0.0 som första stabila release och maintenance mode; den formuleringen påverkar inte bokens arbetsflödesbeskrivning.
