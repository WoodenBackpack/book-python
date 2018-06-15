***************************
Object Oriented Programming
***************************

Method Resolution Order
=======================
.. literalinclude:: src/oop-mro.py
    :name: listing-oop-mro
    :language: python
    :caption: Method Resolution Order


``@staticmethod``
=================
Dekorator ``@staticmethod`` służy do tworzenia metod statycznych, takich które odnoszą się do klasy jako całości, nie do konkretnego obiektu.

.. code-block:: python

    def increment_population():
        Person.population += 1

    class Person:
        population = 0

        def __init__(self, name):
            self.name = name
            increment_population()

    jose = Person('José Jiménez')
    ivan = Person('Иван Иванович')

    # ile użytkowników zostało stworzonych
    print(Person.population)

.. code-block:: python

    class Person:
        population = 0

        def __init__(self, name):
            self.name = name
            Person.increment_population()

        @staticmethod
        def increment_population():
            Person.population += 1

    jose = Person('José Jiménez')
    ivan = Person('Иван Иванович')

    # ile użytkowników zostało stworzonych
    print(Person.population)


Hash
====
Set można zrobić z dowolnego hashowalnego obiektu:

.. code-block:: python

    class Adres:
        def __init__(self, miasto):
            self.miasto = miasto

    {1, 1, 2}
    # {1, 2}

    a = Adres(miasto='Gwiezdne')
    data = {a, a}
    len(data)
    # 1

    data = {Adres(miasto='Gwiezdne'), Adres(miasto='Gwiezdne')}
    len(data)
    # 2

.. code-block:: python

    key = 'last_name'

    my_dict = {
        'fist_name': 'Jose',
        key: 'Jimenez',
        1: 'id',
    }


.. code-block:: python

    class Adres:
        def __init__(self, ulica, miasto):
            self.ulica = ulica
            self.miasto = miasto

        def __hash__(self, *args, **kwargs):
            """
            __hash__ should return the same value for objects that are equal.
            It also shouldn't change over the lifetime of the object;
            generally you only implement it for immutable objects.
            """
            return hash(self.ulica) + hash(self.miasto)

        def __eq__(self, other):
            if self.ulica == other.ulica and self.miasto == other.miasto:
                return True
            else:
                return False


``@property`` i ``@x.setter``
=============================
Dekoratory ``@propery``, ``@kola.setter`` i ``@kola.deleter`` służą do zdefiniowania dostępu do 'prywatnych' pól klasy. W Pythonie z definicji nie ma czegoś takiego jak pole prywatne. Jest natomiast konwencja nazywania zmiennych zaczynając od symbolu podkreślnika (np. ``_kola``), jeżeli chcemy zaznaczyć, że to jest zmienna prywatna. Nic nie blokuje jednak użytkownika przed dostępem do tej zmiennej. Dekoratory ``@kola.setter`` i ``@property`` tworzą metody do obsługi zmiennej ``_kola`` (w przykładzie poniżej).

.. code-block:: python

    class Samochod:
        def __init__(self):
            self._kola = None

        @property
        def kola(self):
            print('Wyczytanie z książki pokazdu')
            return self._kola

        @kola.setter
        def kola(self, value):
            print('Wpis do książki pojazdu o zmienionych kołach')
            self._kola = value

        @kola.deleter
        def kola(self):
            del self._kola


    auto = Samochod()
    print(auto.kola)  # uruchamiany jest ``kola``, który jest property

    auto.kola = 4  # uruchamiany jest ``kola.setter z argumentem 4``
    print(auto.kola)  # uruchamiany jest ``kola``, który jest property

.. note:: Masz aplikację pisaną od 10 lat i chcesz wstrzyknąć logowanie użycia danej zmiennej w programie. Możesz dodać ``@property`` dla tej właściwości, która napierw zaloguje ``__name__`` i ``__file__`` a później zwróci wartość (nie zmieniając API aplikacji).


Polimorfizm
===========
.. code-block:: python

    >>> class Pojazd:
    ...    def zatrab(self):
    ...        raise NotImplementedError
    ...
    >>> class Motor(Pojazd):
    ...     def zatrab(self):
    ...         print('bip')
    ...
    >>> class Samochod(Pojazd):
    ...     def zatrab(self):
    ...         print('biiiip')
    ...
    >>> obj = Motor()
    >>> obj.zatrab()
    >>>
    >>> obj = Samochod()
    >>> obj.zatrab()

.. note:: to jest alternatywa dla instrukcji ``switch``

    .. code-block:: python

        if obj == 'motor'
            print('bip')
        elif obj == 'samochod'
            print('biiiip')
        ...


Interfejsy
==========
.. literalinclude:: src/oop-interface.py
    :name: listing-oop-interface
    :language: python
    :caption: Interfejsy

Klasy abstrakcyjne
==================
Klasa abstrakcyjna to taka klasa, która nie ma żadnych instancji (w programie nie ma ani jednego obiektu, który jest obiektem tej klasy). Klasy abstrakcyjne są uogólnieniem innych klas, wykorzystuje się to często przy dziedziczeniu. Na przykład tworzy się najpierw abstrakcyjną klasę ``figura``, która definiuje, że figura ma pole oraz, że jest metoda, ktora to pole policzy na podstawie jedynie prywatnych zmiennych. Po klasie ``figura`` możemy następnie dziedziczyć tworząc klasy ``kwadrat`` oraz ``trójkąt``, które będą miały swoje instancje i na których będziemy wykonywali operacje.

.. literalinclude:: src/oop-abstract-class.py
    :name: listing-abstract-class
    :language: python
    :caption: Abstract Class


Monkey Patching
===============
.. code-block:: python

    class User:
        def hello(self):
            print('hello')


    def monkey_patch():
        print('My function')


    User.hello = monkey_patch
    User.hello()
    # 'My function'

.. code-block:: python

    import datetime
    import json


    DATA = {
        'datetime': datetime.datetime(1961, 4, 12, 2, 7, 0, 123456),
        'date': datetime.datetime(1961, 4, 12),
        'name': 'José Jiménez',
    }

    def datetime_encoder(self, obj):
        if isinstance(obj, datetime.datetime):
            return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'
        elif isinstance(obj, datetime.date):
            return f'{obj:%Y-%m-%d}'
        else:
            return super().default(obj)

    json.JSONEncoder.default = datetime_encoder


Metaclass
=========
Każdy obiekt klasy jest instankcją tej klasy. Każda napisana klasa jest instancją obiektu, który nazywa się metaklasą. Domyślnie klasy są obiektem typu ``type``

.. code-block:: python

    class FooClass:
        pass

    f = FooClass()
    isinstance(f, FooClass)
    isinstance(f, type)
