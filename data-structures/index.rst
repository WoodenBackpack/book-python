.. _Data Structures:

***************
Data Structures
***************


Simple collections
==================

``tuple``
---------
* Immutable - cannot add, modify or remove elements
* Required comma for one element ``tuple``
* Brackets are optional
* Can store any type

.. code-block:: python

    my_tuple = ()
    my_tuple = tuple()

.. code-block:: python

    my_tuple = 1,
    my_tuple = (1,)

.. code-block:: python

    my_tuple = 1, 2, None, False, 'José'
    my_tuple = (1, 2, None, False, 'José')
    my_tuple = tuple(1, 2, None, False, 'José')

.. code-block:: python

    my_tuple = (1, 2, 3, 4, 5)

    my_tuple[:3]   # (1, 2, 3)
    my_tuple[1:4]  # (2, 3, 4)
    my_tuple[3:]   # (4, 5)
    my_tuple[::2]  # (1, 3, 5)
    my_tuple[-1]   # 5

.. code-block:: python

    my_tuple = (1, 2, 3, 4, 5)

    MIN = 1
    MAX = 5
    BETWEEN = slice(MIN, MAX)

    my_tuple[BETWEEN]  # (2, 3, 4)
    my_tuple[MIN:MAX]  # (2, 3, 4)

.. code-block:: python

    my_tuple = (1, 2, 3)
    len(my_tuple)  # 3

``list``
--------
* Brackets are required
* Can store any type
* No need for comma for one element ``list``
* Can be appended or extended

.. code-block:: python

    my_list = []
    my_list = list()

.. code-block:: python

    my_list = [1]

.. code-block:: python

    my_list = [1, 2, None, False, 'José']
    my_list = list(1, 2, None, False, 'José')

.. code-block:: python

    my_list = [1, 2, None, False, 'José']

    my_list[1]             # 2
    my_list[2:4]           # [None, False]
    my_list[::2]           # [1, None, 'José']
    my_list[-1]            # 'José'

.. code-block:: python

    [1, 2] + [3, 4]        # [1, 2, 3, 4]
    [1, 2].append(3)       # [1, 2, 3]
    [1, 2].append([3, 4])  # [1, 2, [3, 4]]
    [1, 2].extend([3, 4])  # [1, 2, 3, 4]

.. code-block:: python

    my_list = [1, 2, 3]
    len(my_list)  # 3

``set``
-------
* Only unique values
* No need for comma for one element ``set``

.. code-block:: python

    my_set = set()

.. code-block:: python

    my_set = {1}

.. code-block:: python

    my_set = {1, 3, 1}       # {1, 3}
    my_set = set([1, 3, 1])  # {1, 3}

.. code-block:: python

    my_set = {1, 2, 3}       # {1, 2, 3}

    my_set.add(4)            # {1, 2, 3, 4}
    my_set.add(4)            # {1, 2, 3, 4}
    my_set.add(3)            # {1, 2, 3, 4}

    my_set.update([4, 5])    # {1, 2, 3, 4, 5}
    my_set.update({4, 5})    # {1, 2, 3, 4, 5}

.. code-block:: python

    {1,2} - {2,3}            # {1}        # Subtract
    {1,2} | {2,3}            # {1, 2, 3}  # Sum
    {1,2} & {2,3}            # {2}        # Union
    {1,2} ^ {2,3}            # {1, 3}     # Symmetrical difference
    {1,2} + {3,4}            # TypeError: unsupported operand type(s) for +: 'set' and 'set'

.. code-block:: python

    my_set = {1, 2, None, False, 'José'}

    my_set[1]                # 2
    my_set[2:4]              # {None, False}
    my_set[::2]              # {1, None, 'José'}
    my_set[-1]               # 'José'

.. code-block:: python

    my_set = {1, 2, 3}
    len(my_set)              # 3

.. code-block:: python

    names = ['Max', 'Ivan', 'José', 'Max']

    unique_names = set(names)
    # {'Max', 'Ivan', 'José'}

``dict``
--------
* Key - Value storage
* Key can be any hashable object
* Value can be any object
* Przy wyświetlaniu elementów słownika, kolejność może się zmieniać!

.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez'
    }

    my_dict['last_name']
    # 'Jiménez'

.. code-block:: python

    my_dict = {
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    my_dict[1969]
    # 'First Step on the Moon'

.. code-block:: python

    my_dict = {
        'name': 'José',
        'name': 'Ivan',
    }
    # {'name': 'Ivan'}

.. code-block:: python

    my_dict = {
        'astronaut': {'first_name': 'José', 'last_name': 'Jiménez'}
        'agency': ['NASA', 'Roscosmos', 'ESA'],
        'age': 42,
    }

    my_dict['locations']                # ['NASA', 'Roscosmos', 'ESA']
    my_dict['astronaut']['first_name']  # José


.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez'
        'age': 42,
    }

    my_dict.keys()                    # ['first_name', 'last_name', 'age']
    my_dict.values()                  # ['José', 'Jiménez', 42]
    my_dict.items()                   # [('first_name', 'José'), ('last_name', 'Jiménez'), ('age', 42)]

Accessing ``dict`` values with ``[...]`` and ``.get(...)``
----------------------------------------------------------
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
* ``.get(...)`` returns ``None`` if key not found
* ``.get(...)`` can have default value, if key not found

.. code-block:: python

    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
    }

    data['last_name']          # 'Jiménez'
    data.get('last_name')      # 'Jiménez'

    data['agency']             # KeyError: 'agency'
    data.get('agency')         # None
    data.get('agency', 'n/a')  # n/a

``dict`` vs. ``set``
--------------------
* Należy zwrócić uwagę, aby nie pomylić z ``dict``

.. code-block:: python

    {}                                # dict
    {1}                               # set
    {1, 2}                            # set
    {1: 2}                            # dict
    {1:1, 2:2}                        # dict

.. code-block:: python

    my_data = {}
    isinstance(my_data, (set, dict))  # True
    isinstance(my_data, dict)         # True
    isinstance(my_data, set)          # False

    my_data = {1}
    isinstance(my_data, set)          # True
    isinstance(my_data, dict)         # False

    my_data = {1: 1}
    isinstance(my_data, set)          # False
    isinstance(my_data, dict)         # True


How to initialize?
==================
* ``list()`` or ``[]``
* ``tuple()`` or ``()``
* ``dict()`` or ``{}``
* ``set()`` or ``{}``


Nested collections
==================

``list`` of ``dict``
--------------------
.. code-block:: python

    DATA = [
        {'first_name': 'Max'},
        {'first_name': 'José', 'last_name': 'Jiménez'},
        {'first_name': 'Ivan', 'tags': ['astronaut', 'roscosmos', 'space']},
    ]

    DATA[0]                            # {'first_name': 'Max'}
    DATA[0]['last_name']               # KeyError: 'last_name'
    DATA[0].get('last_name', 'n/a')    # 'n/a'
    DATA[2].get('tags')                # ['astronaut', 'roscosmos', 'space']

Multidimensional lists
----------------------
.. code-block:: python

    array = [
        [0, 1, 2],
        [1, 2, 3],
        [1, 2, 3],
    ]

    array[2][1]  # 2

Mixed types
-----------
.. code-block:: python

    array = [
        [0, 1, 2],
        (1, 2, 3),
        {1, 3, 1},
        {'first_name': 'José', 'last_name': 'Jiménez'}
    ]

    array[3]['last_name']  # 'Jiménez'


How Python understands types?
=============================
* Dla każdego z poniższych przykładów wykonano funkcję ``type(what)`` i wynik pokazano poniżej.
* Dla czytelności przykładu pominięto tę linijkę.

.. code-block:: python

    what = (1, 2)    # <class 'tuple'>
    what = 1, 2      # <class 'tuple'>

.. code-block:: python

    what = ('foo')   # <class 'str'>
    what = 'foo'     # <class 'str'>

    what = ('foo',)  # <class 'tuple'>
    what = 'foo',    # <class 'tuple'>

.. code-block:: python

    what = 1.5      # <class 'float'>
    what = 1        # <class 'int'>
    what = (1.)     # <class 'float'>
    what = (.5)     # <class 'float'>
    what = 1.       # <class 'float'>
    what = .5       # <class 'float'>

.. code-block:: python

    what = (10.5)   # <class 'float'>
    what = (10,5)   # <class 'tuple'>
    what = (10.)    # <class 'float'>
    what = (10,)    # <class 'tuple'>
    what = (10)     # <class 'int'>

    what = 10.5     # <class 'float'>
    what = 10,5     # <class 'tuple'>
    what = 10.      # <class 'float'>
    what = 10,      # <class 'tuple'>
    what = 10       # <class 'int'>


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Split train/test
----------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-data-structures-iris-sample`
#. Wyodrębnij nagłówek (pierwsza linia) od danych
#. Ustaw dane z kolejnych linii w losowej kolejności
#. Podziel zbiór na dwie listy w proporcji:

    - dane do uczenia - 80%
    - dane testowe - 20%

:Założenia:
    * Nazwa pliku: ``structures_split_train_test.py``
    * Szacunkowa długość kodu: około 6 linii
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź:
    * ``from random import shuffle``
    * ``shuffle()`` modyfikuje dane "in place" i zwraca ``None``

.. literalinclude:: src/data-structures-iris-sample.py
    :name: listing-data-structures-iris-sample
    :language: python
    :caption: Sample Iris databases

