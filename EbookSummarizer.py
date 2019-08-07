# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:27:43 2019

@author: Eric
"""
import easygui
#import sys
import ebooklib
from ebooklib import epub
#from ebooklib.utils import debug
from summa import summarizer
from bs4 import BeautifulSoup

#summarization_ratio = 0.01
summarization_words = 200

###open ebook
path = easygui.fileopenbox(filetypes = ["*.epub"],default="*.epub")
book = epub.read_epub(path)


###obtain right language
lang = 'german'
sprache = book.get_metadata('DC', 'language')
if sprache == "en":
    lang='english'
if sprache == "de":
    lang='german'
    
###print title and author
title = book.get_metadata('DC', 'title')
author = book.get_metadata('DC', 'creator')
text = (title[0][0] + " von "  + author [0][0] +"\r\n")

#print description
description = book.get_metadata('DC', 'description')
text+=("Beschreibung:\r\n"+description[0][0]+"\r\n")
text+=("Zusammengefasste Beschreibung:\r\n"+summarizer.summarize(description[0][0],language=lang, words=summarization_words)+"\r\n")

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        text+=('\r\n\r\nKapitel : '+ item.get_name() +"\r\n")
        soup = BeautifulSoup(item.get_content(),features="lxml")
        soup.encode("utf-8")
        summary=summarizer.summarize( soup.get_text(),language=lang, words=summarization_words)#ratio=summarization_ratio)
        text+=(summary)
        text+=("\r\n\r\n")

print(text)

path = easygui.filesavebox(msg="Zusammenfassung speichern.", title="Zusammenfassung speichern", default='', filetypes=["*.txt"])
text_file = open(path, "w", encoding='utf-8')
text_file.write(text)
text_file.close()