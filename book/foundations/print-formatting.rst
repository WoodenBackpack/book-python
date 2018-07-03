.. _Print Formatting:

****************
Print Formatting
****************

Python umożliwia kilka sposobów manipulacji stringami i uwzględnianie zmiennych w wyświetlanych napisach.

Funkcja ``print``
=================
.. code-block:: python

    def print(*args, sep=' ', end='\n', file=None):
        """
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
        """
        ...

Konkatenacja stringów
=====================

Wykorzystanie parametrów funkcji ``print()``
--------------------------------------------
Do łączenia ciągów znakowych, które mają zostać wyświetlone dla użytkownika, można wykorzystać bezpośrednio właściwość funkcji ``print``, która może przyjąć wiele argumentów, które następnie ze sobą połączy.

.. code-block:: python

    >>> imie = 'José Jiménez'
    >>> print('My name', imie, '!')
    My name José Jiménez!

Można tutaj podać jako argumenty zarówno ciągi znaków jak i wartości liczbowe. Ciągi znaków będą od siebie odseparowane ciągiem znaków przekazanym przez argument ``sep``, domyślnie jest to spacja ``' '``.

.. code-block:: python

    >>> imie = 'José Jiménez'
    >>> print('My name', imie, '!', sep=';')
    My;name;José;Jiménez!

Operator ``+``
--------------
Operator + skleja ze sobą stringi. Ten sposób jest niepolecany, ale można go jeszcze często spotkać. Szczególnie u osób, które programują w innych językach tj. Java, JavaScript i C#.

.. code-block:: python

    >>> imie = 'José Jiménez'
    >>> print('My name ' + imie + '!')
    My name José Jiménez!

Można go użyć do wyświetlania zmiennych liczbowych, ale nie jest to najlepsze rozwiązanie.

.. code-block:: python

    >>> imie = 'José Jiménez'
    >>> wiek = 35
    >>> print('My name is ' + imie + ' and I am ' + str(wiek) + ' years old!')
    My name is José Jiménez and I am 35 years old!


Interpolacja zmiennych
======================

Operator: ``%s``, ``%d``, ``%f``
--------------------------------
Używanie tych operatorów przypomina używanie funkcji ``printf``, znanej między innymi z C++. W tekście stringa wstawiamy odpowiedni operator: ``%s`` dla stringa, ``%d`` dla liczby całkowitej, ``%f`` dla liczby zmiennoprzecinkowej. Następnie podajemy po znaku % krotkę z wartościami do wstawienia.

* kolejnościowe
* nazwane
* typy: ``string``, ``int``, ``float``
* operatory na stringu

.. code-block:: python

    >>> imie = 'José Jiménez'
    >>> wiek = 35

    >>> def get_imie(imie):
    >>>    return imie

    >>> print('My name %s!' % imie)
    My name José Jiménez!

    >>> print("%s is %s years old" % (imie, wiek))
    José Jiménez is 35 years old

    >>> print('%s is %s years old' % (wiek, imie))
    35 is José Jiménez years old

    >>> print('%s is %10.1f years old' % (imie, wiek))
    José Jiménez is       35.0 years old

    >>> print('%s is %.1f years old' % (imie, wiek))
    José Jiménez is 35.0 years old

    >>> print('%s is %d years old' % (get_imie(imie), wiek))
    José Jiménez is 35 years old

    >>> print('%(imie)s is %(wiek)d years old' % {
    ...    'wiek': wiek,
    ...    'imie': imie,
    ... })
    José Jiménez is 35 years old

    >>> print('My name %(imie)s.' % locals())
    My name José Jiménez.


Metoda ``.format()``
====================

Wbudowana metoda ``format`` upraszcza nieco powyższy schemat. Zamiast operatora z procentem, używamy w tekście stringu ``{}``, następnie na tym stringu wywołujemy funkcję ``format``, której argumentami są wartości do wstawienia do tekstu.

* ``string``
* ``int``
* ``float``
* operatory na stringu
* jako parametry do ``print("string", **args)``

.. code-block:: python

    >>> imie = 'José Jiménez'
    >>> wiek = 35

    >>> print('{imie} ma {wiek} lat'.format(imie=imie, wiek=wiek))
    José Jiménez ma 35 lat

    >>> print('{wiek} ma {imie} lat'.format(**locals()))
    35 ma José Jiménez lat

    >>> print('Hej mam na imie {} i mam {} lat'.format(imie, wiek))
    Hej mam na imie José Jiménez i mam 35 lat

    >>> print('Hej mam na imie {0} i mam {1} lat'.format(imie, wiek))
    Hej mam na imie José i mam 35 lat

    >>> print('Hej mam na imie {1} i mam {0} lat'.format(imie, wiek))
    Hej mam na imie 35 i mam José lat

    >>> print('Hej mam na imie {1:.3} i mam {0:.1} lat'.format(float(wiek), imie))
    Hej mam na imie Jos i mam 35.0 lat

    >>> print('Hej mam na imie {1:.3} i mam {0:10.1} lat'.format(float(wiek), imie))
    Hej mam na imie Jos i mam       35.0 lat


f-strings - Python >= 3.6
=========================
f-strings to rozwinięcie funkcji ``format``. Jedyne co trzeba zrobić żeby umieścić zmienną w tekście to dodać przed stringiem ``f`` i w nawiasach klamrowych wpisać nazwę zmiennej (np. ``f'to jest zmienna: {zmienna}'``).

* ``f'{variable}'``
* ``f'{self.field}'``
* ``f'{datetime:%Y-%m-%d %H:%M}'``

.. code-block:: python

    >>> import datetime
    >>> imie = 'José'
    >>> wiek = 35

    >>> def get_imie(imie):
    ...    return imie

    >>> print(f'My name {imie}!')
    My name José Jiménez

    >>> print(f'My name {get_imie(imie)}, masz: {wiek} lat')
    My name José, masz: 35 lat

    >>> print(f'dzis jest: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}')
    dzis jest: 1969-07-21 02:56:15

    >>> now = datetime.datetime.now
    >>> print(f'dzis jest: {now():%Y-%m-%d %H:%M:%S}')
    dzis jest: 1969-07-21 02:56:15


Przykład z życia
================
.. warning:: Kod podatny jest na SQL Injection. W praktyce skorzystaj z funkcji ``prepare``.

.. code-block:: python

    username = "' OR 1=1; DROP TABLE users -- "
    password = '132'


    sql_query = f"""

        SELECT *
        FROM users
        WHERE 'username'='{username}'
        AND 'password'='{password}'

    """

    print(sql_query)
    # SELECT id, username, email
    # FROM users
    # WHERE 'username'='' OR 1=1; DROP TABLE users -- '
    # AND 'password'='132'


PEP 3101 -- Advanced String Formatting
======================================
* https://www.python.org/dev/peps/pep-3101/

Basic formatting
----------------
.. code-block:: python

    '%s %s' % ('one', 'two')
    # one two

    '{} {}'.format('one', 'two')
    # one two

    '{1} {0}'.format('one', 'two')
    # two one

Value conversion
----------------
.. code-block:: python

    class Data(object):

        def __str__(self):
            return 'str'

        def __repr__(self):
            return 'repr'


    '%s %r' % (Data(), Data())
    # str repr

    '{0!s} {0!r}'.format(Data())
    # str repr

Padding and aligning strings
----------------------------
.. code-block:: python

    '%10s' % ('test',)
    # '      test'

    '{:>10}'.format('test')
    # '      test'

.. code-block:: python

    '%-10s' % ('test',)
    # 'test      '

    '{:10}'.format('test')
    # 'test      '

.. code-block:: python

    '{:_<10}'.format('test')
    # 'test______'

    '{:^10}'.format('test')
    # '   test   '

    '{:^6}'.format('zip')
    # ' zip  '

Truncating long strings
-----------------------
.. code-block:: python

    '%.5s' % ('xylophone',)
    # 'xylop'

    '{:.5}'.format('xylophone')
    # 'xylop'

Combining truncating and padding
--------------------------------
.. code-block:: python

    '%-10.5s' % ('xylophone',)
    # 'xylop     '

    '{:10.5}'.format('xylophone')
    # 'xylop     '

Numbers
-------
.. code-block:: python

    '%d' % (42,)
    # '42'

    '{:d}'.format(42)
    # '42'

.. code-block:: python

    '%f' % (3.141592653589793,)
    # '3.141593'

    '{:f}'.format(3.141592653589793)
    # '3.141593'

Padding numbers
---------------
.. code-block:: python

    '%4d' % (42,)
    # '  42'

    '{:4d}'.format(42)
    # '  42'

.. code-block:: python

    '%06.2f' % (3.141592653589793,)
    # '003.14'

    '{:06.2f}'.format(3.141592653589793)
    # '003.14'

.. code-block:: python

    '%04d' % (42,)
    # '0042'

    '{:04d}'.format(42)
    # '0042'

Signed numbers
--------------
.. code-block:: python

    '%+d' % (42,)
    # '+42'

    '{:+d}'.format(42)
    # '+42'

.. code-block:: python

    '% d' % ((- 23),)
    # '-23'

    '{: d}'.format((- 23))
    # '-23'

.. code-block:: python

    '% d' % (42,)
    # ' 42'

    '{: d}'.format(42)
    # ' 42'

.. code-block:: python

    '{:=5d}'.format((- 23))
    # '-  23'

    '{:=+5d}'.format(23)
    # '+  23'

Named placeholders
------------------
.. code-block:: python

    data = {'first': 'Hodor', 'last': 'Hodor!'}

    '%(first)s %(last)s' % data
    # 'Hodor Hodor!'

    '{first} {last}'.format(**data)
    # 'Hodor Hodor!'

.. code-block:: python

    '{first} {last}'.format(first='Hodor', last='Hodor!')
    # 'Hodor Hodor!'

Getitem and Getattr
-------------------
.. code-block:: python

    person = {'first': 'Jean-Luc', 'last': 'Picard'}

    '{p[first]} {p[last]}'.format(p=person)
    # 'Jean-Luc Picard'

.. code-block:: python

    data = [4, 8, 15, 16, 23, 42]
    '{d[4]} {d[5]}'.format(d=data)
    # '23 42'

.. code-block:: python

    class Plant(object):
        type = 'tree'

    '{p.type}'.format(p=Plant())
    # tree

.. code-block:: python

    class Plant(object):
        type = 'tree'
        kinds = [{'name': 'oak'}, {'name': 'maple'}]

    '{p.type}: {p.kinds[0][name]}'.format(p=Plant())
    # 'tree: oak'

Datetime
--------
.. code-block:: python

    from datetime import datetime

    '{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))
    # '2001-02-03 04:05'

Parametrized formats
--------------------
.. code-block:: python

    '{:{align}{width}}'.format('test', align='^', width='10')
    # '   test   '

.. code-block:: python

    '%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182)
    # 'Gib = 2.718'

    '{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
    # 'Gib = 2.718'

.. code-block:: python

    '%*.*f' % (5, 2, 2.7182)
    # ' 2.72'

    '{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)
    # ' 2.72'

.. code-block:: python

    '{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')
    # 'Gib = 2.72'

.. code-block:: python

    from datetime import datetime
    dt = datetime(2001, 2, 3, 4, 5)

    '{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')
    # '2001-02-03 04:05'

.. code-block:: python

    '{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)
    # '     +2.72'

.. code-block:: python

    '{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')
    # '     +2.72'

Custom objects
--------------
.. code-block:: python

    class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

    '{:open-the-pod-bay-doors}'.format(HAL9000())
    # "I'm afraid I can't do that."

Więcej informacji
=================
* https://pyformat.info - Formatowanie stringów w Python


``pprint``
==========
.. code-block:: python

    from pprint import pprint

    data = [{'first_name': 'José', 'last_name': 'Jiménez'}, {'first_name': 'Max', 'last_name': 'Peck'}, {'first_name': 'Ivan', 'last_name': 'Ivanovic'}]

    pprint(data)
    # [{'first_name': 'José', 'last_name': 'Jiménez'},
    #  {'first_name': 'Max', 'last_name': 'Peck'},
    #  {'first_name': 'Ivan', 'last_name': 'Ivanovic'}]

.. code-block:: python

    from pprint import pformat

    data = [{'first_name': 'José', 'last_name': 'Jiménez'}, {'first_name': 'Max', 'last_name': 'Peck'}, {'first_name': 'Ivan', 'last_name': 'Ivanovic'}]

    # returns formatted data
    my_string = pformat(data)


Assignments
===========

Powielanie napisów
------------------
#. Wczytaj od użytkownika tekst
#. Napisz trzy funkcje:

    * ``print_1(what)`` wykorzystującą ``range()``
    * ``print_2(what)`` wykorzystującą pętlę ``while``
    * ``print_3(what)`` wykorzystującą mnożenie stringów

#. Każda funkcja ma wyświetlić 5 kopii tego napisu, każda w osobnej linii.
#. Napisz doctest do wszystkich funkcji.

:Założenia:
    * Nazwa pliku: ``print_lines.py``
    * Szacunkowa długość kodu: około 5 linii
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * formatowanie ciągu znaków
    * korzystanie z pętli i instrukcji warunkowych

Przeliczanie temperatury
------------------------
#. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni).
#. Wynik musi być taki jak na listingu poniżej
#. Znak ma być zawsze wyświetlany
#. Zwróć uwagę na wyjustowanie tekstu
#. Zwróć uwagę na wypełnienie miejsca niezajętego przez cyfry

    .. code-block:: text

        Temperatura -     20C to ____-4____F
        Temperatura -     15C to ____+5____F
        Temperatura -     10C to ___+14____F
        Temperatura -      5C to ___+23____F
        Temperatura +      0C to ___+32____F
        Temperatura +      5C to ___+41____F
        Temperatura +     10C to ___+50____F
        Temperatura +     15C to ___+59____F
        Temperatura +     20C to ___+68____F
        Temperatura +     25C to ___+77____F
        Temperatura +     30C to ___+86____F
        Temperatura +     35C to ___+95____F
        Temperatura +     40C to ___+104___F

:Założenia:
    * Nazwa pliku: ``print_formatting.py``
    * Szacunkowa długość kodu: około 3 linie
    * Maksymalny czas na zadanie: 10 min

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * .. code-block:: python

        def celsius_to_fahrenheit(degree):
            return degree*1.8 + 32

:Co zadanie sprawdza?:
    * zaawansowane formatowanie ciągu znaków
