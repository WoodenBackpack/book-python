**********************
Tworzenie dokumentacji
**********************

reStructuredText vs. Markdown
=============================

Format reStructuredText
=======================

Po co?
------

Paragrafy
---------
- newline

Nagłówki
--------
- Tytuł
- Nagłówek pierwszego poziomu
- Nagłówek drugiego poziomu
- Nagłówek trzeciego poziomu
- Nagłówek czwartego poziomu (czy stosować?)

Odnośniki
---------
- Wewnątrz dokumentu
- numref
- na zewnątrz dokumentu

Obrazki i media
---------------
- figure (scale, name,

Specjalne wstawki
-----------------
- ``.. todo::``

Listingi kodu
-------------
- Osadzone
- Z plików zewnętrznych

TODO
----

Listy
-----
- listy nieuporządkowane
- listy numerowane
- jednopoziomowe i zagnieżdżone
- listy mieszane

Tabele
------
- Table
- List Table
- CSV Table

Cytowanie
---------
- ``cite``
- bibtex


Sphinx
======
Zależnośći
----------
sphinx==1.6.5
sphinx_rtd_theme
sphinxcontrib-bibtex==0.3.6
sphinxjp.themes.revealjs

Config
------
- Wersja na podstawie hasba git

Dobre praktyki
--------------
- podział na rozdziały
- rozkład katalogów
- listingi kodu
- zdjecia
- dane w tabelkach CSV
- konwencja nazewnicza plikow
- konwencja nazewnicza figure, csv-table, literalinclude

Generowanie dokumentacji
------------------------
- Table of Contents

Buildery
--------
- make html
- make singlehtml
- make pdf

toctree
-------

Read the docs
=============
* http://readthedocs.org

Zadania kontrolne
=================

Dokumentacja
------------
#. Za pomocą ``sphinx-quickstart`` stwórz dokumentację.
#. Zmień theme na ``sphinx_rtd_theme``
#. Dokument zatytułuj "Szkolenie z Pythona"
#. Stwórz nagłówek pierwszego poziomu "Obrazki i tesksy" i w nim osadź obrazek jako figure, wraz tekstem opisującym, obrazek ma być połowy wielkości i wycentrowany, nazwany
#. Stwórz nagłówek pierwszego poziomu "Lorem Ipsum" i wklej tekst lorem ipsum do dokumentacji.
#. W tekście lorem ipsum wstaw numref do obrazka
#. Stwórz nagłówek pierwszego poziomu i zamieść tabelę Irysów na podstawie danych Iris Dataset https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv
#. Stwórz nagłówek pierwszego poziomu "Listingi kodu" i osadź dwa swoje skrypty z poprzednich zadań:

    - książka adresowa jako ``literalinclude`` w nagłówku drugiego poziomu "Książka Adresowa"
    - prosty skrypt jako ``code-block`` w nagłówku drugiego poziomu "Pozostałe przykłady"
    - które podejście jest lepsze?

#. Tekst lorem ipsum oznacz jako cytowanie cycerona wykorzystując bibtext

:Podpowiedź:
    - ``sphinxcontrib-bibtex==0.3.6``
