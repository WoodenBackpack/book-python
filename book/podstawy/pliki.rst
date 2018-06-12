.. _Operacje na plikach:

*******************
Operacje na plikach
*******************

Konstrukcja ``with``
====================
* Context manager


Czytanie
========
.. literalinclude:: src/file-read.py
    :language: python
    :caption: Reading from file


Zapis
=====
.. literalinclude:: src/file-write.py
    :language: python
    :caption: Writing to file


Tryby odczytu i zapisu
======================
.. csv-table::
    :header: "Character", "Meaning"
    :widths: 20, 80

    "``'r'``", "open for reading (default)"
    "``'w'``", "open for writing, truncating the file first"
    "``'a'``", "open for writing, appending to the end of the file if it exists"
    "``'b'``", "binary mode"


Obsługa wyjątków
================
.. literalinclude:: src/file-exception.py
    :language: python
    :caption: Exception handling while accessing files


Zadania kontrolne
=================

Zawartość zadanego pliku
------------------------
#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

Parsowanie ``/etc/hosts``
-------------------------
#. Do pliku ``hosts`` w katalogu gdzie będzie Twój skrypt zapisz poniższy szablon: :numref:`listing-file-etc-hosts`
#. Ważne są komentarze, białe spacje i linie przerwy
#. Przedstaw go w formie listy dictów jak w przykładzie poniżej: :numref:`listing-file-hosts`
#. Zwróć uwagę na uprawnienia do odczytu pliku

:Co zadanie sprawdza?:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Podpowiedź:
    * kod powinien mieć około 10 linii

.. literalinclude:: src/file-etc-hosts.txt
    :name: listing-file-etc-hosts
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/hosts``

.. literalinclude:: src/file-hosts.py
    :name: listing-file-hosts
    :language: python
    :caption: ``/etc/hosts`` example
