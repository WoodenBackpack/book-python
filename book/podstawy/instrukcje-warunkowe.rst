.. _Instrukcje warunkowe:

********************
Instrukcje warunkowe
********************

``if`` ... ``elif`` ... ``else``
================================

Instrukcje warunkowe pozwalają kierować wykonywanymi instrukcjami pod pewnym warunkiem. Jeżeli kod wpisany po słowie kluczowym ``if`` wykona się jako wartość prawdziwa (niezerowa, nie-``None``, itp.), wykonany zostanie kod pod tym słowem kluczowym.

.. code-block:: python

    if True :
         print('this is true')


Do instrukcji warunkowej można dodać słowo kluczowe ``else``. Wtedy, jeżeli wartość przy słowie kluczowym ``if`` ewaluuje się jako fałsz, wykonany zostanie kod pod słowem kluczowym ``else``.


.. code-block:: python

    if True :
        print('this is true')
    else:
        print('this is false')


.. code-block:: python

    if name != 'José Jiménez':
         print('this is false')
     else:
         print('this is true')


Możliwe jest także sprawdzenie kilku warunków przed przejściem do ``else``. Do sprawdzenia drugiego i kolejnych warunków służy słowo kluczowe ``elif`` (w wielu innych językach rozwijane jako ``else if``).

.. code-block:: python

    if name == 'José Jiménez':
         print('My name José Jiménez')
    elif name == 'Max Peck':
        print('Your name is Max Peck')
    else:
         print('Your name is neither José Jiménez nor Max Peck')

.. code-block:: python

    if not 0 <= k <= n:
        raise ValueError('Sample larger than population')


``not``, ``in``, ``is``
=======================

Słowo kluczowe ``in`` pozwala na sprawdzenie czy dana wartość zawiera się w zbiorze (iteratorze).

.. code-block:: python

    if name in {'José Jiménez', 'Max Peck'}:
        print('Your name is José Jiménez or Max Peck')
    else:
         print('Your name is neither José Jiménez nor Max Peck')


``not`` pozwala zanegować warunek.

.. code-block:: python

    if not name == 'José Jiménez':
         print('Not José')
     else:
         print('My name José Jiménez')

.. code-block:: python

    if not name:
         print('Name is not set')
     else:
         print('You have set your name')


``is`` porównuje czy dwa obiekty są tożsame.

.. code-block:: python

    if name is None:
         print('Name is not set')
     else:
         print('You have set your name')


Bardzo kuszący jest następujący przykład:

 .. code-block:: python

     if name is 'Max Peck':
          print('You are Max!')
      else:
          print('You are not Max!')


**Nie jest on jednak do końca poprawny. Słowo kluczowe ``is`` porównuje czy dwa obiekty są tym samym obiektem, nie czy mają taką samą wartość.** Poniższy przykład ilustruje, że pomimo że dwa obiekty przechowują takiego samego stringa to nie są sobie tożsame, mimo że są sobie równe.

 .. code-block:: python

     a = 'hello'
     b = 'hello'

     print(f'a is {a}, b is {b}')
     print(f'a == b returns: {a==b}')
     print(f'a is b returns: {a is b}')

     a = 'hello'
     b = ''.join('hello')

     print(f'a is {a}, b is {b}')
     print(f'a == b returns: {a==b}')
     print(f'a is b returns: {a is b}')


``switch`` statement?!
======================
* Why ``switch`` is bad practise?

    "You can do this easily enough with a sequence of ``if... elif... elif... else``. There have been some proposals for switch statement syntax, but there is no consensus (yet) on whether and how to do range tests. See PEP 275 for complete details and the current status. "

.. code-block:: python

    if name == 'José Jiménez':
        print('My name José Jiménez')
    elif name == 'Ivan Ivanovic':
        print('Your name is Ivan Ivanovic')
    elif name == 'Max Peck':
        print('Your name is Max Peck')
    else:
         print('Your name is other')


.. code-block:: python

    switch = {
        'a': 1,
        'b': 2,
    }

    switch['a']


.. code-block:: python

    choices = {'a': 1, 'b': 2}
    key = 'a'

    result = choices.get(key, 'default value when key is not found')


.. code-block:: python

    def switch(key):
        return {
            'a': 1,
            'b': 2,
        }.get(key, 'default value')

    switch('a')  # 1
    switch('x')  # 'default value'

Zadania kontrolne
=================

Zmienne i wczytywanie ciągu od użytkownika
------------------------------------------
#. Napisz program, który poprosi użytkownika o wiek i wyświetli wartość.
#. Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest "dorosła" czy "niepełnoletnia".

:Co zadanie sprawdza?:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie