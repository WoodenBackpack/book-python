.. _Print Formatting:

****************
Print Formatting
****************

Python umożliwia kilka sposobów manipulacji stringami i uwzględnianie zmiennych w wyświetlanych napisach.

Funkcja ``print``
=================
.. code-block:: python

    def print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
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

    name = 'José Jiménez'

    print('My name', name, '!')
    # My name José Jiménez!

Można tutaj podać jako argumenty zarówno ciągi znaków jak i wartości liczbowe. Ciągi znaków będą od siebie odseparowane ciągiem znaków przekazanym przez argument ``sep``, domyślnie jest to spacja ``' '``.

.. code-block:: python

    name = 'José Jiménez'

    print('My name', name, '!', sep=';')
    # My;name;José;Jiménez!

Operator ``+``
--------------
Operator + skleja ze sobą stringi. Ten sposób jest niepolecany, ale można go jeszcze często spotkać. Szczególnie u osób, które programują w innych językach tj. Java, JavaScript i C#.

.. code-block:: python

    name = 'José Jiménez'

    print('My name ' + name + '!')
    # My name José Jiménez!

Można go użyć do wyświetlania zmiennych liczbowych, ale nie jest to najlepsze rozwiązanie.

.. code-block:: python

    name = 'José Jiménez'
    age = 35

    print('My name ' + name + ' and I am ' + str(age) + ' years old!')
    # My name is José Jiménez and I am 35 years old!


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

    name = 'José Jiménez'
    age = 42

    def my(name):
        return name

    print('My name %s!' % name)                 # My name José Jiménez!
    print("%s has %s years" % (name, age))      # José Jiménez has 42 years
    print('%s has %s years' % (age, name))      # 42 has José Jiménez years
    print('%s has %10.1f years' % (name, age))  # José Jiménez has       42.0 years
    print('%s has %.1f years' % (name, age))    # José Jiménez has 42.0 years
    print('%s has %d years' % (my(name), age))  # José Jiménez has 42 years

    print('%(name)s has %(age)d years' % {
        'age': age,
        'name': name,
    })
    # José Jiménez has 42 years

    print('My name %(name)s.' % locals())
    # My name José Jiménez.


Metoda ``.format()``
====================

Wbudowana metoda ``format`` upraszcza nieco powyższy schemat. Zamiast operatora z procentem, używamy w tekście stringu ``{}``, następnie na tym stringu wywołujemy funkcję ``format``, której argumentami są wartości do wstawienia do tekstu.

* ``string``
* ``int``
* ``float``
* operatory na stringu
* jako parametry do ``print("string", **args)``

.. code-block:: python

    name = 'José Jiménez'
    age = 42

    print('My name {name} has {age} years'.format(name=name, age=age))   # 'My name José Jiménez has 42 years'
    print('My name {age} has {name} years'.format(**locals()))           # 'My name 42 has José Jiménez years'
    print('My name {} has {} years'.format(name, age))                   # 'My name José Jiménez has 42 years'
    print('My name {0} has {1} years'.format(name, age))                 # 'My name José Jiménez has 42 years'
    print('My name {1} has {0} years'.format(name, age))                 # 'My name 42 has José Jiménez years'
    print('My name {1:.3} has {0:10.1} years'.format(float(age), name))  # 'My name Jos has       42.0 years'
    print('My name {1:.3} has {0:.1} years'.format(float(age), name))    # 'My name Jos has 42.0 years'


f-strings - Python >= 3.6
=========================
f-strings to rozwinięcie funkcji ``format``. Jedyne co trzeba zrobić żeby umieścić zmienną w tekście to dodać przed stringiem ``f`` i w nawiasach klamrowych wpisać nazwę zmiennej (np. ``f'to jest zmienna: {zmienna}'``).

* ``f'{variable}'``
* ``f'{self.field}'``
* ``f'{datetime:%Y-%m-%d %H:%M}'``

.. code-block:: python

    import datetime

    name = 'José'
    age = 42
    now = datetime.datetime.utcnow
    format = '%Y-%m-%d %H:%M:%S'

    def my(name):
        return name

    print(f'My name {name}!')                                        # 'My name José Jiménez'
    print(f'My name {my(name)}, age: {age} years')                   # 'My name José, age: 42 years'
    print(f'Today is: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}')  # 'Today is: 1969-07-21 02:56:15'
    print(f'Today is: {now():%Y-%m-%d %H:%M:%S}')                    # 'Today is: 1969-07-21 02:56:15'
    print(f'Today is: {now():{format}}')                             # 'Today is: 1969-07-21 02:56:15'


Przykład z życia
================
.. warning:: Kod podatny jest na SQL Injection. W praktyce skorzystaj z funkcji ``prepare``.

.. code-block:: python

    username = "' OR 1=1; DROP TABLE users -- "
    password = '132'

    sql_query = f"""

        SELECT * FROM users
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

    one, two = 'one', 'two'

    '%s %s' % (one, two)        # one two
    '{} {}'.format(one, two)    # one two
    '{1} {0}'.format(one, two)  # two one
    f'{one} {two}'              # one two

Value conversion
----------------
.. code-block:: python

    class Data(object):

        def __str__(self):
            return 'str'

        def __repr__(self):
            return 'repr'


    '%s %r' % (Data(), Data())    # str repr
    '{0!s} {0!r}'.format(Data())  # str repr
    f'{Data()!s} {Data()!r}'      # str repr

Padding and aligning strings
----------------------------
.. code-block:: python

    text = 'test'

    '%10s' % text          # '      test'
    '%10s' % (text,)       # '      test'
    '{:>10}'.format(text)  # '      test'
    f'{text:>10}'          # '      test'

.. code-block:: python

    text = 'test'

    '%-10s' % text        # 'test      '
    '%-10s' % (text,)     # 'test      '
    '{:10}'.format(text)  # 'test      '
    f'{text:10}'          # 'test      '

.. code-block:: python

    text = 'test'

    '{:_<10}'.format(text)  # 'test______'
    f'{text:_<10}'          # 'test______'

    '{:^10}'.format(text)   # '   test   '
    f'{text:^10}'           # '   test   '

    '{:^6}'.format(text)    # ' test  '
    f'{text:^6}'            # ' test  '


Truncating long strings
-----------------------
.. code-block:: python

    text = 'Lorem Ipsum'

    '%.5s' % text         # 'Lorem'
    '%.5s' % (text,)      # 'Lorem'
    '{:.5}'.format(text)  # 'Lorem'
    f'{text:.5}'          # 'Lorem'

Combining truncating and padding
--------------------------------
.. code-block:: python

    text = 'Lorem Ipsum'

    '%-10.5s' % text        # 'Lorem     '
    '%-10.5s' % (text,)     # 'Lorem     '
    '{:10.5}'.format(text)  # 'Lorem     '
    f'{text:10.5}'          # 'Lorem     '

Numbers
-------
.. code-block:: python

    number = 35

    '%d' % number          # '35'
    '%d' % (number,)       # '35'
    '{:d}'.format(number)  # '35'
    f'{number:d}'          # '35'

.. code-block:: python

    number = 3.141592653589793

    '%f' % number          # '3.141593'
    '%f' % (number,)       # '3.141593'
    '{:f}'.format(number)  # '3.141593'
    f'{number:f}'          # '3.141593'

Padding numbers
---------------
.. code-block:: python

    number = 42

    '%4d' % (number,)       # '  42'
    '{:4d}'.format(number)  # '  42'
    f'{number:4d}'          # '  42'


.. code-block:: python

    number = 3.141592653589793

    '%06.2f' % number          # '003.14'
    '%06.2f' % (number,)       # '003.14'
    '{:06.2f}'.format(number)  # '003.14'
    f'{number:06.2f}'          # '003.14'

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
