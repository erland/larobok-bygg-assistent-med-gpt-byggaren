#!/usr/bin/env python3
from pathlib import Path
import re, shutil, subprocess, sys, tempfile, zipfile

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "docs" / "export-metadata.yaml"
BOOK = ROOT / "book.yaml"
EXPORTS = ROOT / "exports"


def simple_yaml(path):
    data = {}
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if re.match(r"^[A-Za-z_]+:\s*$", line):
            current = line.split(":",1)[0]
            data[current] = [] if current == "chapters" else {}
            continue
        if current == "chapters" and re.match(r"^\s+-\s+", line):
            data[current].append(line.split("-",1)[1].strip().strip('"'))
            continue
        if not line.startswith(" ") and ":" in line:
            k,v = line.split(":",1)
            data[k.strip()] = v.strip().strip('"')
            current = None
    return data


def validate(md_files):
    errors = []
    for p in md_files:
        if not p.exists():
            errors.append(f"Saknat kapitel: {p.relative_to(ROOT)}")
            continue
        text = p.read_text(encoding="utf-8")
        if re.search(r"^####", text, re.M):
            errors.append(f"H4 eller djupare rubrik i {p.name}")
        for image in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            if "://" not in image and not (p.parent / image).resolve().exists() and not (ROOT / image).exists():
                errors.append(f"Saknad bildreferens i {p.name}: {image}")
    if errors:
        raise SystemExit("Validering misslyckades:\n- " + "\n- ".join(errors))


def postprocess_epub(path):
    temp = Path(tempfile.mkdtemp())
    try:
        with zipfile.ZipFile(path, 'r') as z: z.extractall(temp)
        opf = next(temp.rglob("*.opf"), None)
        nav = next(temp.rglob("nav.xhtml"), None)
        if not opf or not nav:
            raise SystemExit("EPUB-kontroll misslyckades: nav.xhtml eller OPF saknas")
        text = opf.read_text(encoding="utf-8")
        nav_ids = re.findall(r'<item[^>]+id="([^"]+)"[^>]+properties="[^"]*nav[^"]*"', text)
        for nav_id in nav_ids:
            text = re.sub(rf'(<itemref[^>]+idref="{re.escape(nav_id)}"[^>]*)(/?>)', lambda m: m.group(1) + (' linear="no"' if 'linear=' not in m.group(1) else '') + m.group(2), text)
        opf.write_text(text, encoding="utf-8")
        rebuilt = path.with_suffix('.tmp.epub')
        with zipfile.ZipFile(rebuilt, 'w') as z:
            mimetype = temp / 'mimetype'
            if mimetype.exists(): z.write(mimetype, 'mimetype', compress_type=zipfile.ZIP_STORED)
            for f in sorted(temp.rglob('*')):
                if f.is_file() and f != mimetype:
                    z.write(f, f.relative_to(temp).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
        rebuilt.replace(path)
    finally:
        shutil.rmtree(temp, ignore_errors=True)


def main():
    if not BOOK.exists() or not META.exists():
        raise SystemExit("book.yaml eller docs/export-metadata.yaml saknas")
    if not shutil.which("pandoc"):
        raise SystemExit("Pandoc saknas. Installera Pandoc och kör igen.")
    meta = simple_yaml(META)
    title, subtitle, author, lang = meta.get('title'), meta.get('subtitle'), meta.get('author'), meta.get('language')
    cover_rel = meta.get('cover_image')
    cover = ROOT / cover_rel if cover_rel else None
    if cover and not cover.exists():
        raise SystemExit(f'Omslagsbild saknas: {cover_rel}')
    if not all([title, author, lang]):
        raise SystemExit("Titel, författare och språk måste finnas i exportmetadata")
    chapters = [ROOT / c for c in meta.get('chapters', [])]
    validate(chapters)
    EXPORTS.mkdir(exist_ok=True)
    merged = ROOT / 'exports' / '.book-build.md'
    merged.write_text('\n\n'.join(p.read_text(encoding='utf-8') for p in chapters), encoding='utf-8')
    slug = meta.get('identifier', 'book')
    epub = EXPORTS / f'{slug}.epub'
    epub_cmd = ['pandoc', str(merged), '--from=gfm', '--to=epub3', '--toc', '--toc-depth=1', '--metadata', f'title={title}', '--metadata', f'author={author}', '--metadata', f'lang={lang}', '--css', str(ROOT/'styles/epub.css'), '--output', str(epub)]
    if subtitle:
        epub_cmd.extend(['--metadata', f'subtitle={subtitle}'])
    if cover:
        epub_cmd.extend(['--epub-cover-image', str(cover)])
    subprocess.run(epub_cmd, check=True)
    postprocess_epub(epub)
    pdf = EXPORTS / f'{slug}.pdf'
    if shutil.which('xelatex'):
        header_path = ROOT/'styles/pdf-header.tex'
        tmp_header = None
        if cover:
            tmp_header = EXPORTS/'.pdf-header-build.tex'
            cover_tex = str(cover.resolve()).replace('\\', '/')
            tmp_header.write_text('\\def\\BookCoverImage{' + cover_tex + '}\n' + header_path.read_text(encoding='utf-8'), encoding='utf-8')
            header_path = tmp_header
        pdf_cmd = ['pandoc', str(merged), '--from=gfm', '--pdf-engine=xelatex', '--toc', '--toc-depth=1', '--metadata', 'toc-title=Innehåll', '--metadata', f'title={title}', '--metadata', f'author={author}', '--metadata', f'lang={lang}', '--include-in-header', str(header_path), '--output', str(pdf)]
        if subtitle:
            pdf_cmd.extend(['--metadata', f'subtitle={subtitle}'])
        subprocess.run(pdf_cmd, check=True)
        if tmp_header:
            tmp_header.unlink(missing_ok=True)
    else:
        print('XeLaTeX saknas: EPUB skapad, PDF hoppades över. Installera MacTeX/TinyTeX för PDF.', file=sys.stderr)
    merged.unlink(missing_ok=True)

if __name__ == '__main__': main()
