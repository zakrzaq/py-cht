import os
import sys
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown

doc = None
doc = sys.argv[1]

home_dir = str(Path.home())
docs_dir = os.path.join(home_dir, "cht")
if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)

if doc:
    if doc == 'list':
        md_files = [] 

        for file in os.listdir(docs_dir):
            if file.endswith('.md'):
                md_files.append(Path(file).stem)

        md_files.sort()

        print('\t'.join(md_files))

        sys.exit()

    doc_path = os.path.join(docs_dir, f"{doc}.md")
    console = Console()
    with open(doc_path) as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)
