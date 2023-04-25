import pathlib
import pprint
import re
import sys

import ebooklib
from ebooklib import epub, utils

PATH = sys.argv[1]
ebookPath = pathlib.Path(PATH)

pp = pprint.PrettyPrinter()

if ebookPath.is_dir():
    for file in ebookPath.rglob("*.epub"):
        print(f"Analisando arquivo {file.name}...")
        with open(file, "r") as f:
            book = epub.read_epub(f.name)
        toc = book.toc
        print(f"Nome do livro: {book.title} \nTotal de capitulos: {len(toc)}")
        print("Documentos encontrados...")
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            print(
                f"Titulo do documento: {item.title}\nID do documento: {item.get_id()}"
            )

        print("\n\n\n")

elif ebookPath.is_file():
    book = epub.read_epub(PATH, {"ignore_ncx": True})
    print(f"Tamanho do TOC: {len(book.toc)}")
    print(f"Titulo do livro: {book.title}\n")

    if "title" in book.toc:
        for item in book.toc:
            print(f"Título do capítulo: {item.title}\n")
    else:
        print("TOC nao possui título!\n")

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_IMAGE:
            print("IMAGE properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_STYLE:
            print("STYLE properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_SCRIPT:
            print("SCRIPT properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_NAVIGATION:
            print("NAVIGATION properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_VECTOR:
            print("VECTOR properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_FONT:
            print("FONT properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_VIDEO:
            print("VIDEO properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_AUDIO:
            print("AUDIO properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            print("DOCUMENT properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            print(f"File links: {type(item.get_links())}")
            for link in item.get_links():
                print(f"Links encontrados no documento: {len(link)}")
            print("\n")

        if item.get_type() == ebooklib.ITEM_COVER:
            print("COVER properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
            print("\n")

        if item.get_type() == ebooklib.ITEM_SMIL:
            print("SMIL properties:")
            print(f"File get_name(): {item.get_name()}")
            print(f"File file_name: {item.file_name}")
            print(f"File get_id(): {item.get_id()}")
            print(f"File id: {item.id}")
            print(f"File get_type(): {item.get_type()}")
            print(f"File media_type: {item.media_type}")
            # print(utils.get_pages(item.get_id()))
