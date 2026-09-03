# Bygg din egen AI-assistent med GPT Byggaren

Detta är källprojektet för en kort, praktisk faktabok om hur man förstår och bygger specialiserade AI-assistenter med hjälp av GPT Byggaren.

Bokens huvudspår använder GPT Byggaren i Chat-läge. Läsaren behöver främst beskriva verksamhetsbehovet; GPT Byggaren hjälper till med projektstruktur, instruktioner, Knowledge, tester och distribution.

## Projektstruktur

- `chapters/` – bokmanus
- `docs/` – specifikation, kapitelplan, canon och projektstatus
- `scripts/` – reproducerbar export lokalt och i CI
- `.github/workflows/` – automatiserad PDF/EPUB-byggning
- `styles/` – EPUB/PDF-stilar
- `exports/` – genererade filer

## Export

Boken byggs med samma exportscript lokalt och i GitHub Actions.

### GitHub Actions

Workflowet **Build book** kan startas manuellt från Actions-fliken. Det körs också automatiskt när en GitHub Release publiceras. Vid release läggs PDF och EPUB även till som release-assets.

### Lokalt

Kör:

```bash
./scripts/export-book.sh
```

Pandoc krävs. För PDF används XeLaTeX. Se `docs/export-guide.md` för detaljer.
