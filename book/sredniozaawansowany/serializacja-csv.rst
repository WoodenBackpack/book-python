*********************************
Serializacja i deserializacja CSV
*********************************


Odczytywanie danych z plików CSV
================================
.. literalinclude:: src/csv-read.py
    :name: listing-csv-read
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictReader()``


Zapis do plików CSV
===================
.. literalinclude:: src/csv-write.py
    :name: listing-csv-write
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictWriter()``


Parsowanie innych plików za pomocą ``csv.DictReader()``
=======================================================
.. literalinclude:: src/csv-passwd.py
    :name: listing-csv-passwd
    :language: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``


Zadania Kontrolne
=================

Wczytywanie pliku ``csv``
-------------------------
* https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv

#. ściągnij plik z URL podanego powyżej i zapisz na dysku w miejscu gdzie masz skrypty
#. Wczytaj dane z pliku ``csv``
#. Pierwsza linijka stanowi header

Serializacja ``csv``
--------------------
* Za pomocą ``csv.DictWriter()`` zapisz do pliku dane o zmiennej strukturze.
* ``fieldnames`` nie może być zahardkodowane w skrypcie.

.. code-block:: python

    DATABASE = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Ivan'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'Jose', 'born': 1961, 'first_step': 1969},
    ]

:Podpowiedź:
    * Kod powinien mieć około 5 linii
    * To jest bardzo często występujący i użyteczny przykład

:Co zadanie sprawdza?:
    * Umiejętność korzystania z modułu ``csv``
    * Umiejętność iteracji po złożonych strukturach danych
    * Dynamiczne generowanie struktur danych na podstawie innych


Serializacja obiektów do CSV
----------------------------
#. Użyj obiektu ``książka_adresowa`` z listingu :numref:`listing-address-book`
#. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
#. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami, kodowanie UTF-8.
#. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Podpowiedź:
    - powtarzanie rekordów (user pozostaje ten sam) z innymi danymi adresowymi
    - dodawanie kolumn (ulica_1, miasto_1, panstwo_1, ulica_2, miasto_2, panstwo_2) i automatyczne generowanie fieldnames
    - wrzucenie danych jako string do jednego pola adres_1, adres_2, adres_3 i ustalenie separatora (np: średnik - ';')
    - jedno pole adres (w ramach niego wszystkie adresy rozdzielone ";" a dane przecinkami ",")

.. literalinclude:: src/csv-address-book.py
    :name: listing-address-book
    :language: python
    :caption: Address book