# Exportguide

Boken exporteras reproducerbart via `scripts/export-book.py`. Samma exportkommando används lokalt och i GitHub Actions, så att PDF och EPUB byggs på samma sätt oavsett var bygget körs.

## GitHub Actions

Workflowet finns i `.github/workflows/build-book.yml` och stöder två sätt att bygga boken.

### Manuell byggning

1. Öppna **Actions** i GitHub-repot.
2. Välj workflowet **Build book**.
3. Välj **Run workflow**.
4. När jobbet är klart finns PDF och EPUB i en nedladdningsbar Actions-artifact.

### Automatisk byggning vid release

När en GitHub Release **publiceras** startar samma workflow automatiskt.

Workflowet:

1. checkar ut källkoden,
2. installerar Pandoc och XeLaTeX,
3. kör `./scripts/export-book.sh`,
4. verifierar att både PDF och EPUB skapats,
5. sparar dem som Actions-artifact,
6. laddar dessutom upp PDF och EPUB som assets på den publicerade GitHub-releasen.

De publicerade filerna heter:

```text
bygg-din-egen-ai-assistent-med-gpt-byggaren.pdf
bygg-din-egen-ai-assistent-med-gpt-byggaren.epub
```

Workflowet har `contents: write` eftersom releasebygget behöver rättighet att bifoga filer till en release.

## Lokal export

### Krav

- Python 3
- Pandoc
- För PDF: XeLaTeX

### Körning

```bash
./scripts/export-book.sh
```

Filer skapas i `exports/`.

EPUB använder endast en navigerbar läsar-TOC och ingen synlig innehållsförteckning som eget kapitel. EPUB-TOC är begränsad till H1. PDF får en innehållsförteckning före manus med endast H1-nivån, så att den förblir kort och överskådlig.
