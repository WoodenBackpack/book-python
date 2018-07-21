.. _Types:

*****
Types
*****


Variables and constants
=======================

Variable declaration
--------------------
.. code-block:: python

    my_variable = 10
    my_variable = 'ehlo world'

Constant declaration
--------------------
.. code-block:: python

    MY_CONSTANT = 10
    MY_CONSTANT = 'ehlo world'

Variables vs. constants
-----------------------
* Jedyną różnicą jest konwencja nazewnicza
* Stałe zapisujemy dużymi literami
* Zmienne zapisujemy małymi literami

Types
-----
* Od Python 3.5 wprowadzono nową składnię
* Nowa składnia nie jest wymagana (ale jest dobrą praktyką)
* Nowa składnia uruchomiona w Python przed 3.5 rzuci SyntaxError
* Twórcy języka mówą, że typy nigdy nie będą wymagane
* Aby sprawdzić poprawność trzeba użyć bibliotek zewnętrznych tj: ``mypy`` lub ``pyre-check``
* Typy można znaleźć w wielu funkcjach w bibliotece standardowej
* Dobre IDE podpowiada typy i informuje o błędach

.. code-block:: python

    name: str = 'José Jiménez'
    age: int = 30

Type inference
--------------
* Static Typing (Java, C++, Swift)

.. code-block:: java

    String name = new String("José Jiménez")

* Dynamic Typing (Python, PHP, Ruby)

.. code-block:: python

    name = str('José Jiménez')

.. code-block:: python

    name: str = str('José Jiménez')  # Type annotations

    # Type annotations (type hinting not forcing)
    # this will work, but IDE should warn
    name: str = 10


Numerical types
===============

``int``
-------
* Liczba całkowita
* Funkcja ``int()`` kowertuje argument na ``int``
* W Python 3 ``int`` nie ma maksymalnej wartości (dynamicznie się rozszerza)

.. code-block:: python

    age = 30
    age: int = 30

    int(10)  # 10
    int(10.0)  # 10
    int(10.9)  # 10

    milion = 1000000
    milion = 1_000_000
    milion = 1e6

``float``
---------
* Liczba zmiennoprzecinkowa
* Funkcja ``float()`` konwertuje argument na ``float``

.. code-block:: python

    float(10)              # 10.0

    float('+1.23')         # 1.23
    float('-1.23')         # -1.23
    float('   -123.45\n')  # -123.45

    float('1e-003')        # 0.001
    float('+1E6')          # 1000000.0

    float('-inf')          # -inf
    float('-Infinity')     # -inf
    float('inf')           # inf
    float('Infinity')      # inf

``complex``
-----------
* Liczba zespolona (część rzeczywista i urojona)
* Notacja inżynierska ``j`` a nie matematyczna ``i``
* W ciągu nie może być spacji

.. code-block:: python

    complex('1+2j')    # (1+2j)
    complex('1 + 2j')  # ValueError: complex() arg is a malformed string


Logical types
=============

``bool``
--------
* Wartość logiczna
* Funkcja ``bool()`` konwertuje argument na ``bool``
* Zwróć uwagę na wielkość liter

.. code-block:: python

    True
    False

``None``
--------
* Wartość pusta
* Nie jest to wartość ``False`` ani ``0``
* Jest używany, gdy wartość jest nieustawiona

.. code-block:: python

    name = None

    if name is None:
        print('What is your name?')

    if not wiek:
        print('What is your name?')


Character types
===============

``str``
-------
* Ciąg (łańcuch) znaków
* Funkcja ``str()`` konwertuje argument na ``str``

.. code-block:: python

    name = 'José'       # 'José'
    name = "José"       # 'José'
    name: str = 'José'  # 'José'
    'José' * 3          # JoséJoséJosé

    str(1969)           # '1969'
    str(13.37)          # '13.37'

    name = """
        José Jiménez
        Max Peck
        Ivan Ivanovic
    """
    # '\nMax Peck\nMax Peck\nIvan Ivanovic\n'


Single or double quote?
-----------------------
* Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
* Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
* Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia.
* Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.
* Ma to znaczenie przy ``doctest``, który zawsze korzysta z pojedynczych i rzuca errorem jak są podwójne

.. code-block:: python

    my_str = 'it\'s José\'s book'
    my_str = "it's José's book"

.. code-block:: python

    my_str = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

Escape characters
-----------------
.. code-block:: text

    \n
    \r
    \r\n

.. figure:: img/type-machine.jpg
    :scale: 50%
    :align: center

    Why we have '\\r\\n' on Windows?

.. code-block:: text

    \x1F680  # after \x goes hexadecimal number
    \u1F680  # after \u goes four hexadecimal numbers
    🚀
    \b1010   # after \b goes bytes
    \t
    \'

Characters before strings
-------------------------
* Format string: since Python 3.6

.. csv-table:: String modifiers
    :header-rows: 1
    :widths: 15, 30, 55
    :file: data/str-modifiers.csv

.. code-block:: python

    name = 'José Jiménez'

    f'My name {name}'
    u'zażółć gęślą jaźń'
    b'this is text'
    r'(?P<foo>)\n'
    r'C:\Users\Admin\file.txt'

.. code-block:: python

    print('C:\Users\Admin\file.txt')
    # ``\Users`` (``s`` is invalid hexadecimal for unicode)
    # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


``print()``
-----------
* Prints on the screen
* More in :numref:`Print Formatting`

.. code-block:: python

    print('My name José Jiménez')  # My name José Jiménez

    name = 'José Jiménez'
    print(f'My name {name}')        # My name José Jiménez

String immutability
-------------------
* ``str`` jest niemutowalny
* Każda operacja na ``str`` tworzy nową kopię
* Zwróć uwagę ile stringów jest przechowywanych w pamięci

.. code-block:: python

    name = 'José'
    name += ' Jiménez'

    print(name)  # José Jiménez

String methods
--------------

``split()``
^^^^^^^^^^^
.. code-block:: python

    text = 'José Jiménez'
    text.split()         # ['José', 'Jiménez']

    text = 'Max,Peck'
    text.split(',')         # ['Max', 'Peck']

``strip()``, ``lstrip()``, ``rstrip()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    name = '    Max Peck    '

    name.strip()   # 'Max Peck'
    name.lstrip()  # 'Max Peck    '
    name.rstrip()  # '    Max Peck'

``startswith()``
^^^^^^^^^^^^^^^^
* starts_with

.. code-block:: python

    name = 'José Jiménez'

    if name.startswith('José'):
        print('My name José Jiménez')
    else:
        print('I have no name')

``join()``
^^^^^^^^^^
.. code-block:: python

    names = ['José', 'Max', 'Ivan', str(1961), '1969']

    ';'.join(names)
    # 'José;Max;Ivan;1961;1969'

``title()``, ``lower()``, ``upper()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Przydatne do czyszczenia danych przed analizą lub Machine Learning
* Przykład:

    * 'Jana III Sobieskiego 1/2'
    * 'ul. Jana III Sobieskiego 1/2'
    * 'Ul. Jana III Sobieskiego 1/2'
    * 'UL. Jana III Sobieskiego 1/2'
    * 'os. Jana III Sobieskiego 1/2'
    * 'Jana 3 Sobieskiego 1/2'
    * 'Jana 3ego Sobieskiego 1/2'
    * 'Jana III Sobieskiego 1 m. 2'
    * 'Jana III Sobieskiego 1 apt 2'
    * 'Jana Iii Sobieskiego 1/2'
    * 'Jana IIi Sobieskiego 1/2'

.. code-block:: python

    name = 'joSé jiMénEz'

    name.title()  # 'José Jiménez'
    name.upper()  # 'JOSÉ JIMÉNEZ'
    name.lower()  # 'josé jiménez'

``replace()``
^^^^^^^^^^^^^
.. code-block:: python

    name = 'José Jiménez'
    name.replace('J', 'j')  # 'josé jiménez'

String splicing
---------------
.. code-block:: python

    text = 'Lorem ipsum'

    text[2]      # 'r'
    text[:2]     # 'Lo'
    text[0:3]    # 'Lor'
    text[1:4]    # 'ore'
    text[-3]     # 's'
    text[-3:]    # 'sum'
    text[-3:-1]  # 'su'
    text[:-2]    # 'Lorem ips'
    text[::2]    # 'Lrmism'
    text[::-1]   # 'muspi meroL'
    text[::-2]   # 'msimrL'

Handling user input
-------------------
* Funkcja ``input()`` zawsze zwraca ``str``
* Pamiętaj o spacji na końcu prompt

.. code-block:: python

    name = input('Type your name: ')


Assignments
===========

Basic usage of ``print()`` function
-----------------------------------
#. Stwórz skrypt o treści:

    .. code-block:: python

        import sys
        print(sys.version)

#. Uruchom go w swoim IDE

:Założenia:
    * Nazwa pliku: ``python_version.py``
    * Szacunkowa długość kodu: 2 linie
    * Maksymalny czas na zadanie: 2 min

Variables and types
-------------------
#. Wczytaj od użytkownika imię
#. Użytkownik wprowadza tylko dane typu ``str``
#. Za pomocą f-string formatting wyświetl na ekranie ``'My name "IMIE".\nI hope you\'re ok!'``, gdzie IMIE to wartość którą podał
#. Zwróć uwagę na znaki apostrofów, cudzysłowów i nowych linii
#. Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na ``_``
#. Nie korzystaj z dodawania stringów ``str + str``

:Założenia:
    * Nazwa pliku: ``types_input.py``
    * Szacunkowa długość kodu: 3 linie
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika

Handling user input and type casting
------------------------------------
#. Użytkownik wprowadza odległości w metrach
#. Użytkownik wprowadza tylko dane typu ``int`` lub ``float``
#. Dane przy wyświetlaniu muszą być przekonwertowane do typów podanych poniżej
#. Napisz program który przekonwertuje odległości i wyświetli je w formacie zgodnie z szablonem:

.. code-block:: python

    print(f'Meters: {meters}')                 # int
    print(f'Kilometers: {...}')                # int
    print(f'Miles: {...}')                     # float
    print(f'Nautical Miles: {...}')            # float
    print(f'All: {...}, {...}, {...}, {...}')  # int, int, float, float

:Założenia:
    * Nazwa pliku: ``types_casting.py``
    * Szacunkowa długość kodu: 3 linie
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Konwersja typów
    * Operacje matematyczne na zmiennych
    * Wczytywanie tekstu od użytkownika

:Podpowiedź:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska
