.. _Object Oriented Programming:

***************************
Object Oriented Programming
***************************

Object Paradigm
===============
* Odwzorowanie świata na obiekty i relacje między nimi

Classes and Objects
===================
.. literalinclude:: src/oop-class.py
    :language: python
    :caption: Classes and Objects

Fields
======

Static Fields
-------------
.. literalinclude:: src/oop-fields-static.py
    :language: python
    :caption: Static Fields

Dynamic Fields
--------------
.. literalinclude:: src/oop-fields-dynamic.py
    :language: python
    :caption: Dynamic fields

Static vs. Dynamic Fields
-------------------------
.. literalinclude:: src/oop-fields-static-vs-dynamic.py
    :language: python
    :caption: Static vs. Dynamic fields

``__dict__`` - Getting dynamic fields and values
------------------------------------------------
.. literalinclude:: src/oop-fields-dict.py
    :language: python
    :caption: ``__dict__`` - Getting dynamic fields and values


Methods
=======
.. literalinclude:: src/oop-methods-noargs.py
    :language: python
    :caption: Methods

.. literalinclude:: src/oop-methods-args.py
    :language: python
    :caption: Methods

``self`` - Instance as an argument
----------------------------------
* pierwszy argument do metody
* wyjątek ``@staticmethod`` o tym będzie później
* przy uruchomieniu funkcji nie podajemy go jawnie

.. literalinclude:: src/oop-methods-self.py
    :language: python
    :caption: Methods argument ``self``

``__init__()`` - Initializer Method
----------------------------------
* ``__init__()`` to nie konstruktor
* Domyślny ``__init__()`` gdy niezdefiniowaliśmy własnego
* Inicjalizacja pól klasy tylko w ``__init__``

.. literalinclude:: src/oop-fields-dynamic.py
    :language: python
    :caption: Fields added dynamically

.. literalinclude:: src/oop-init.py
    :language: python
    :caption: ``__init__()`` - Initializer Method

``__str__()`` - Stringify object
--------------------------------
* print converts it's arguments to ``str()`` automatically before printing

.. literalinclude:: src/oop-str.py
    :language: python
    :caption: Stringify object

Inheritance
===========
.. literalinclude:: src/oop-inheritance.py
    :language: python
    :caption: Inheritance

Multiple Inheritance
--------------------
.. literalinclude:: src/oop-inheritance-multiple.py
    :language: python
    :caption: Multiple Inheritance

Composition (Mixin Classes)
---------------------------
.. literalinclude:: src/oop-composition.py
    :language: python
    :caption: Composition (Mixin Classes)

Inheritance vs. Composition
---------------------------
* Kompozycja ponad dziedziczenie!

``super()`` - Calling object parent
-----------------------------------
.. literalinclude:: src/oop-super.py
    :language: python
    :caption: Using ``super()`` on a class

``_`` and ``__`` - Private, protected, public?!
===============================================
* Brak pól protected i private
* Wszystkie pola są public
* ``_nazwa`` - pola prywatne (tylko konwencja)
* ``__nazwa__`` - funkcje systemowe
* ``nazwa_`` - używane przy kolizji nazw

.. literalinclude:: src/oop-private-public.py
    :language: python
    :caption: ``_`` and ``__`` - Private, protected, public?!

What should be in the class and what not?
-----------------------------------------
* Jeżeli metoda w swoim ciele ma ``self`` i z niego korzysta to powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` to nie powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` ale wybitnie pasuje do klasy, to można ją tam zamieścić oraz dodać dekorator ``@staticmethod``

.. literalinclude:: src/oop-staticmethod.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``

One class per file?
-------------------
* Jeżeli klasy są małe - jeden plik
* Jeżeli klasy są duże - osobne pliki


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Address Book (Easy)
-------------------
#. Dla danych z :numref:`listing-oop-addressbook-easy` napisz książkę adresową
#. Wszystkie dane w książce muszą być reprezentowane przez klasy.
#. Klasy powinny wykorzystywać domyślne argumenty w ``__init__``.
#. Użytkownik może mieć wiele adresów.
#. Użytkownik może nie mieć żadnego adresu

:Założenia:
    * Nazwa pliku: ``oop_addressbook_easy.py``
    * Szacunkowa długość kodu: około 10 linii
    * Maksymalny czas na zadanie: 20 min

:Co zadanie sprawdza?:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na stringa oraz jego reprezentacja (które i kiedy użyć)

.. literalinclude:: src/oop-assignment-addressbook-easy.py
    :name: listing-oop-addressbook-easy
    :language: python
    :caption: Address Book

Points and Vectors
------------------
Przekształć swój kod z przykładu z modułu "Matematyka" tak żeby wykorzystywał klasy.

:Zadanie 0:
    Napisz klasę ``ObiektGraficzny``, która implementuje "wirtualną" funkcję ``plot()``. Niech domyślnie ta funkcja podnosi ``NotImplementedError`` (podpowiedź: ``raise NotImplementedError``).

:Zadanie 1:
    Napisz klasę ``Punkt``, która dziedziczy po ``ObiektGraficzny``, która będzie miała "ukryte" pola ``_x``, ``_y``. Konstruktor tej klasy ma przyjmować współrzędne ``x`` oraz ``y`` jako argumenty. Napisz obsługę pól ukrytych ``_x`` oraz ``_y`` jako ``@property`` tej klasy (obsługiwane jako ``x`` oraz ``y``). Dopisz implementacje metod ``__str__`` oraz ``__repr__``. Zaimplementuj metodę ``plot(kolor)``, która wyrysuje ten punkt na aktualnie aktywnym wykresie. Kolor domyślnie powinien przyjmować wartość ``'black'``.

    Dopisz do tej klasy metodę statyczną, która zwróci losowy punkt w podobny sposób jak funkcja ``random_point(center, std)`` zwracała obiekt dwuelementowy.

:Zadanie 2:
    Dopisz do tej klasy dwie metody, które pozwolą obliczyć odległość między dwoma punktami. Jedna z tych metod niech będzie metodą statyczną, która przyjmuje dwa punkty jako argumenty, a zwraca odległość między nimi (przykładowe wywołanie tej metody: ``Punkt.oblicz_odleglosc_miedzy_punktami(punkt_A, punkt_B)``). Druga z tych metod niech będzie zwykłą metodą klasy, która przyjmie jeden punkt jako argument oraz obliczy odległość od tego punktu do punktu na którym jest wykonywana (``punkt_A.oblicz_odleglosc_do(punkt_B)``).

:Zadanie 3:
    Napisz kod, który wykorzystując klasę zaimplementowaną w przykładzie powyżej, wygeneruje listę losowych punktów wokół punktów A i B. Wyrysuj te punkty na wykresie, podobnie jak w przykładzie z modułu "Matematyka".

:Zadanie 4:
    Napisz kod, który zaklasyfikuje te losowo wygenerowane punkty do punktów A oraz B na podstawie odległości. W tym celu wykorzystaj napisane metody do obliczania odległości między punktami. Po klasyfikacji wyrysuj te punkty na wykresie, podobnie jak w przykładzie z modułu "Matematyka".

:Założenia:
    * Nazwa pliku: ``oop-vector.py``
    * Szacunkowa długość kodu: około 20 linii
    * Maksymalny czas na zadanie: 30 min
