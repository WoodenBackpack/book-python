*******
Doctest
*******

Niezwykle użytecznym sposobem komentowania są tzw. doctesty. W wielolinijkowym komentarzu wpisujemy sesję z interpreterem a po uruchomieniu doctestów otrzymujemy informację czy nasza funkcja poprawnie się wykonuje. Jest to bardzo proste narzędzie, które poza samym pokazaniem jak działa funkcja, jakie parametry przyjmuje i co zwraca daje możliwość weryfikacji poprawności działania kodu. W tych materiałach nieraz będziemy korzystać z tego rozwiązania.

Wykorzystując taki zapis natychmiast widzimy co dzieje się w danym rozwiązaniu. Doctesty bardzo przydają się przede wszystkim do zastosowań wykorzystujących wyrażenia regularne, których zrozumienie zapisu często wymaga chwili zastanowienia.


Test for ``bool`` return values
===============================
.. code-block:: python

    AGE_ADULT = 18

    def is_adult(age):
        """
        >>> is_adult(18)
        True
        >>> is_adult(17.9)
        False
        """
        if age >= AGE_ADULT:
            return True
        else:
            return False


Test for ``int`` return values
==============================
.. code-block:: python

    def sumowanie_liczb(a, b):
        """
        >>> sumowanie_liczb(1, 2)
        3
        >>> sumowanie_liczb(-1, 1)
        0
        >>> sumowanie_liczb(0, 0)
        0
        """
        return a + b


Test for ``str`` return values
==============================

Returning ``str``
-----------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        >>> hello()
        'José Jiménez'
        >>> hello('Ivan Ivanovich')
        'Ivan Ivanovich'
        """
        return name

Printing ``str``
----------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        >>> hello()
        José Jiménez
        >>> hello('Ivan Ivanovich')
        Ivan Ivanovich
        """
        print(name)

Printing ``str`` with newlines
------------------------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        >>> hello()
        José Jiménez
        José Jiménez
        José Jiménez
        <BLANKLINE>
        """
        print(f'{name}\n' * 3)

Testing for exceptions
======================
.. code-block:: python

    def add(a, b):
        """
        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
        >>> add(0, 0)
        0
        >>> add([1, 2])
        Traceback (most recent call last):
            ...
        TypeError: Argument must be int or float
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Argument must be int or float')

        if not isinstance(b, (int, float)):
            raise TypeError('Argument must be int or float')

        return a + b


Using python statements in ``doctest``
======================================
.. code-block:: python

    def when(date):
        """
        >>> import datetime
        >>> moon = datetime.date(1969, 7, 20)
        >>> hello(moon)
        '1969-07-20'
        """
        print(f'{date:%Y-%m-%d}')


Running doctest from standalone scripts
=======================================
* Testy dla wszystkich funkcji aktualnie zdefiniowanych w przestrzeni nazw

.. code-block:: python

    def add(a, b):
        """
        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
        >>> add(0, 0)
        0
        """
        return a + b


    if __name__ == '__main__':
        import doctest
        doctest.testmod()


Practical example
=================
.. code-block:: python

    from typing import Union


    def kilometers_from_meters(km: Union[int, float]) -> float:
        """
        >>> kilometers_from_meters(1)
        1000.0
        >>> kilometers_from_meters(0)
        0.0
        >>> kilometers_from_meters(-1)
        Traceback (most recent call last):
            ...
        ValueError: Argument must be positive
        >>> kilometers_from_meters([1, 2])
        Traceback (most recent call last):
            ...
        ValueError: Invalid Argument
        >>> kilometers_from_meters('one')
        Traceback (most recent call last):
            ...
        ValueError: Invalid Argument
        >>> kilometers_from_meters(1.5)
        1500.0
        """
        if not isinstance(km, (int, float)):
            raise ValueError('Invalid Argument')

        if km < 0:
            raise ValueError('Argument must be positive')

        return float(1000 * km)


Assignments
===========

Konwersja temperatury
---------------------
#. Napisz funkcję, która przeliczy temperaturę podaną w Fahrenheit na Kelviny
#. Napisz testy do rozwiązania i pokryj przypadki:

    * temperatura ujemna
    * temperatura zero
    * temperatura dodatnia
    * temperatura ``float``
    * temperatura ``int``
    * lista temperatur
    * podany parametr to ``str``

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * Jeden stopień Celsiusza odpowiada jednemu stopniowi w skali Kelvina
    * -273,15 °C = 0 K

:Założenia:
    * Nazwa pliku: ``doctest_temperature.py``
    * Szacunkowa długość kodu: około 6 linii
    * Maksymalny czas na zadanie: 5 min
