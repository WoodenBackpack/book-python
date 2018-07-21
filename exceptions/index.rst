**********
Exceptions
**********

Po co są wyjątki?
=================
Wyjątki stosowane są wtedy, gdy pewna metoda albo funkcja nie może wykonać się poprawnie. Na przykład kiedy dane wprowadzone od użytkownika są nieprawidłowe albo jest problem z dostępem do zasobu (np. pliku). Wyjątek jest wtedy podnoszony, żeby powiadomić program, że funkcja nie jest w stanie sobie poradzić z napotkanym problemem. Program może wtedy albo próbować poradzić sobie z wyjątkiem, albo przekazać go wyżej, dochodząc ostatecznie do warstwy systemu.

Wyjątki nie powinny być stosowane przy normalnym użytkowaniu projektowanej aplikacji. Wystąpienie wyjątku oznacza błąd programu!


Podnoszenie wyjątków
====================
.. code-block:: python

    raise NameError

Tworzenie własnych wyjątków
===========================
.. code-block:: python

    class CtgDoesNotExistsError(ArithmeticError):
        strerror = 'Cotangens dla kąta 90 nie istnieje'
        errno = 10

    def ctg(deg):
        if deg == 90:
            raise CtgDoesNotExistsError
        return "wylicz cotangens kąta"


Przechwytywanie wyjątków
========================
Python spróbuje najpierw wykonać to co będzie zaprogramowane w ramach słowa kluczowego ``try``. Jeżeli w trakcie wykonywania tego fragmentu kodu interpreter napotka na wyjątek, kod zostanie przerwany i zostanie wykonany fragment zaprogramowany w ramach słowa kluczowego ``except``, odnoszący się do danego wyjątku, albo do wszystkich pozostałych ``else``. Na koniec, niezależnie od tego czy wyjątek wystąpił czy nie, zostanie wykonany fragment zawarty w ``finally``.

* ``try``
* ``except``
* ``else``
* ``finally``

.. code-block:: python

    def bar():
        raise NameError


    try:
        bar()

    except NameError:
        print('Błąd nazwy złapany')

    except SyntaxError:
        print('Błąd składni złapany')

.. code-block:: python

      while True:
          try:
              print('hello')
          except:
              continue


      while True:
          try:
              print('hello')
          except Exception:
              continue

Przykład z życia
================
.. code-block:: python

    from django.contrib.auth.models import User

    try:
        User.objects.get(id=2)
    except User.DoesNotExists:
        pass

Najpopularniejsze wyjątki
=========================
.. csv-table:: Najpopularniejsze wyjątki
    :header-rows: 1
    :widths: 25, 75
    :file: data/exception-popular.csv

Hierarchia wyjątków
===================
.. code-block:: text

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning

Przykład wyjątków przy czytaniu plików
======================================
.. warning:: uważaj aby zawsze przechwytywać wyjątki! Inaczej możesz nie zabić procesu. Poniżej błędny kod

      .. code-block:: python

            while True:
                try:
                    input('Podaj ocenę: ')
                except:
                    continue

.. code-block:: python

    import logging
    log = logging.getLogger(__name__)

    log.info('Rozpoczynam program')

    try:

        log.debug('Próbuję odczytać plik')

        with open(FILENAME, 'w') as file:
            content = file.read()
            print(content)

        log.debug('Plik odczytany i zamknięty')

    except PermissionError as e:
        log.error(e)
        print(e.strerror)

    except OSError as e:
        log.error(e)
        print(e.strerror)

    except Exception as e:
        log.error(e)
        print(e.strerror)

    else:
        log.info('Operacje na pliku zakończyły się powodzeniem')

    finally:
        log.debug('Zakończenie pracy nad plikiem')

    log.info('Kończymy program')


Korzystanie z ``warnings``

.. code-block:: python

    import warnings

    def sumuj(a, b):
        warnings.warn('Przestarzala nazwa, uzyj sum()', PendingDeprecationWarning)
        return a + b

    def sum(a, b):
        return a + b


    sumuj(1, 2)
    sum(1, 2)

.. code-block:: console

    $ python __notepad__.py

    $ python -W all __notepad__.py
    __notepad__.py:5: PendingDeprecationWarning: Przestarzala nazwa, uzyj sum()
      warnings.warn('Przestarzala nazwa, uzyj sum()', PendingDeprecationWarning)

