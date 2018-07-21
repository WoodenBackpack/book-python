.. _Builtin and Keywords:

********************
Builtin and Keywords
********************


Keywords
========
Słowa kluczowe (keywords) to wyrazy zarezerwowane do użytku Pythona. Nie można użyć słowa kluczowego jako nazwy zmiennej, nazwy funkcji czy innego identyfikatora. Każdy ze słów kluczowych odgrywa ważną rolę w tym języku. Lista słów kluczowych może być uzyskana wpisując:

.. code-block:: python

    import keyword
    print(keyword.kwlist)

``import``
----------
Biblioteki w Pythonie są pogrupowane w moduły. Słowo kluczowe ``import`` służy do importowania modułów do naszej przetrzeni nazw. Przestrzeń nazw (namespace) zawiera wszystkie zmienne (również funkcje i klasy), które zadeklarowaliśmy w trakcie działania programu. ```import`` to Pythonowy odpowiednik np. dyrektywy ``#include<nazwa_biblioteki>`` z C++.

.. code-block:: python

    import module

Wykonanie powyższego kodu spowoduje dodanie do aktualnej przestrzeni nazw modułu ``module``. Każdy moduł może zawierać submoduły, funkcje, klasy, itp. Możemy dodatkowo wskazać, którą klasę lub metodę chcemy zaimportować z modułu. Dodatkowo, wykorzystując słowo kluczowe ``as`` możemy nadać zaimportowanemu modułowi czy funkcji nową nazwę.

.. code-block:: python

    from module import submodule
    from module.submodule import function as alias
    from module import submodule as alias

Aby wykorzystać funkcję z danego modułu, musimy najpierw wskazać, z którego modułu chcemy skorzystać a następnie podać nazwę funkcji czy zmiennej do której chcemy się odwołać. Korzystając z przykładu powyżej:

.. code-block:: python

    import keyword
    print(keyword.kwlist)

W pierwszej linijce importujemy moduł ``keyword``. W drugiej linijce wypisujemy zawartość zmiennej ``kwlist`` z modułu ``keyword``. Moglibyśmy uzyskać podobny efekt wykonując:

.. code-block:: python

    from keyword import kwlist
    print(kwlist)

W tym przykładzie, z modułu ``keyword`` importujemy jedynie zmienną ``kwlist``. Przy takiej składni warto wspomnieć, że zmniejsza ona czytelność, nie podnosząc wcale efektywności kodu. Interpreter i tak wczyta najpierw całą zawartość modułu, następnie stworzy nową zmienną ``kwlist``, której przypisze odpowiednią wartość. Taki zapis zmniejsza czytelność kodu i zwiększa prawdopodobieństwo błędu.  Używając zapisu ``import module`` i następnie ``module.variable`` jednoznacznie wskazujemy z jakiego modułu korzystamy.

.. code-block:: python

    from . import module
    from .. import module

    from .module import submodule
    from ..module import submodule

``pass``
--------
Python domyślnie oczekuje wcięcia po dwukropku. Jeżeli chcemy zostawić klasę czy funkcję pustą, korzystamy wtedy ze słowa kluczowego ``pass``.

.. code-block:: python

    def my_function():
        pass

.. code-block:: python

    def my_function():
        pass

    my_var = my_function()
    # None

``continue``
------------
Słowo kluczowe ``continue`` powoduje przerwanie aktualnie wykonywanej pętli i przejście do kolejnej iteracji.

.. code-block:: python

    ETC_PASSWD = """
    # User Database
    root:x:0:0:root:/root:/bin/bash
    peck:x:1000:1000:Max Peck:/home/peck:/bin/bash
    jimenez:x:1001:1001:Jose Jimenez:/home/jimenez:/bin/bash
    ivanovic:x:1002:1002:Ivan Ivanovic:/home/ivanovic:/bin/bash
    """

    for line in ETC_PASSWD:
        if line.startswith('#'):
            continue

        name = line.split(':')[4]
        print(name)


.. code-block:: python

    ETC_PASSWD = """
    # User Database
    root:x:0:0:root:/root:/bin/bash
    peck:x:1000:1000:Max Peck:/home/peck:/bin/bash
    jimenez:x:1001:1001:Jose Jimenez:/home/jimenez:/bin/bash
    ivanovic:x:1002:1002:Ivan Ivanovic:/home/ivanovic:/bin/bash
    """

    for line in ETC_PASSWD:
        print(line)
        continue

        # ten kod się nie wywoła
        # przydatne do zrozumienia działania funkcji i zobaczenia jaki jest aktualny element
        if line.startswith('#'):
            continue

        name = line.split(':')[4]
        print(name)

``break``
---------
Słowo kluczowe ``break`` przerywa aktualnie wykonywaną pętlę.

.. code-block:: python

    while True:
        number = input('Type number: ')

        if number:
            break

``eval()``
----------
.. code-block:: python

    eval('name="José Jiménez"; print(name)')
    # José Jiménez


``__file__``
------------
.. code-block:: python

    import os

    BASE_DIR = os.path.dirname(__file__)
    path = os.path.join(BASE_DIR, 'main.py')

``__name__``
------------
* Zmienna ``__name__`` pozwala ustalić czy dany plik jest wykonywany czy importowany.
* Jeżeli dany plik jest wykonywany, zmienna ``__name__`` ustawiana jest na ``'__main__'``.
* Jeżeli dany plik jest importowany jako moduł, zmienna ``__name__`` ustawiana jest na nazwę modułu.
* Jest to przydatne na przykład przy testowaniu modułów.

Dodanie do modułu poniższej linijki:

.. code-block:: python

    if __name__ == '__main__':
        print('hello world')

Sprawi, że wypisane na konsoli zostanie ``'hello world!'`` jeżeli dany plik jest uruchamiany z konsoli. Powyższy kod nie wykona się natomiast jeżeli plik zaimportujemy jako moduł w innym pliku.

Przykład z życia:

.. code-block:: python

    import logging

    log = logging.getLogger(__name__)

.. code-block:: python

    def run():
        ...

    if __name__ == '__main__':
        # Jeżeli skrypt wywoływany jest z konsoli "z ręki" to uruchom funckję ``run()``
        # Jeżeli został zaimportowany, to ten fragment będzie zignorowany
        # I trzeba uruchomić funkcję ``run()`` samodzielnie - kontrolowanie
        run()


Builtin functions
=================

``sorted()`` and ``sort()``
---------------------------
* Sortują elementy listy.
* ``sorted()`` zwraca posortowaną listę, ale nie zapisuje zmienionej kolejności
* ``.sort()`` zmienia listę na stałe

.. code-block:: python

    numbers = [3, 1, 2]
    sorted(numbers)
    # [1, 2, 3]
    print(numbers)
    # [3, 1, 2]

.. code-block:: python

    numbers = [3, 1, 2]
    numbers.sort()  # returns None
    print(numbers)
    # [1, 2, 3]

``range()``
-----------
* Tworzy **iterator**, który zwraca liczby w sekwencji.

.. code-block:: python

    for liczba in range(0, 5):
        print(liczba)


    for liczba in range(0, 5, 2):
        print(liczba)

.. code-block:: python

    numbers_generator = range(0, 5)
    print(numbers_generator)
    # range(0, 5)


.. code-block:: python

    numbers_generator = range(0, 5)
    numbers = list(numbers_generator)

    print(numbers)  # [0, 1, 2, 3, 4]

``isinstance()``
----------------
* Sprawdza czy dany obiekt jest instancją danej klasy
* Jeżeli jest więcej niż jeden typ to musi być ``tuple`` a nie ``list`` lub ``set``

.. code-block:: python

    isinstance(10, int)           # True
    isinstance(10, float)         # False
    isinstance(10, (int, float))  # True

``min()``
---------
Wartość minimalna z listy.

.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    min(numbers)  # 1
    min(3, 1, 5)  # 1

``max()``
---------
Wartość maksymalna z listy.

.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    max(numbers)  # 5
    max(3, 1, 5)  # 5

``len()``
---------
Długość listy, tuple, stringa itp.

.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    len(numbers)                   # 5
    len('Max')                     # 3
    len({'id': 3, 'name': 'Max'})  # 2


``bin()``
---------
* Konwertuje liczbę na binarną
* Nie stosuje kodu uzupełnień do dwóch

.. code-block:: python

    bin(3)   # '0b11'
    bin(-3)  # '-0b11'

``hex()``
---------
* Konwertuje liczbę na heksadecymalną
* Konwersja kolorów w HTML
* Shellcode

.. code-block:: python

    hex(99)  # '0x63'

``oct()``
---------
* Konwertuje liczbę na octalną
* Przydatne do uprawnień w systemie operacyjnym

.. code-block:: python

    oct(33261)  # '0o100755'

``ord()``
---------
Zwraca kod ASCII jednoznakowego stringa.

.. code-block:: python

    ord('a')  # 97

``chr()``
---------
Z pozycji w tablicy ASCII konwertuje kod na znak Unicode.

.. code-block:: python

    chr(97)  # 'a'


Other builtin functions
=======================
.. todo:: Convert table to CSV

.. csv-table:: Most used Built-in functions
    :header-rows: 1

    "Name", "Description"
    "", ""
    "", ""
    "", ""
    "", ""
    "", ""
    "", ""
    "", ""


===============  ==============  ==================  ============  ================
..               ..              Built-in Functions  ..            ..
---------------  --------------  ------------------  ------------  ----------------
`abs()`          `dict()`        `help()`            `min()`       `setattr()`
`all()`          `dir()`         `hex()`             `next()`      `slice()`
`any()`          `divmod()`      `id()`              `object()`    `sorted()`
`ascii()`        `enumerate()`   `input()`           `oct()`       `staticmethod()`
`bin()`          `eval()`        `int()`             `open()`      `str()`
`bool()`         `exec()`        `isinstance()`      `ord()`       `sum()`
`bytearray()`    `filter()`      `issubclass()`      `pow()`       `super()`
`bytes()`        `float()`       `iter()`            `print()`     `tuple()`
`callable()`     `format()`      `len()`             `property()`  `type()`
`chr()`          `frozenset()`   `list()`            `range()`     `vars()`
`classmethod()`  `getattr()`     `locals()`          `repr()`      `zip()`
`compile()`      `globals()`     `map()`             `reversed()`  `__import__`
`complex()`      `hasattr()`     `max()`             `round()`
`delattr()`      `hash()`        `memoryview()`      `set()`
===============  ==============  ==================  ============  ================
