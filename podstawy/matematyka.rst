.. _Matematyka:

**********
Matematyka
**********

Moduł ``math`` w bibliotece standardowej
========================================

.. code-block:: python

    import math

    math.sin()
    math.cos()
    math.tan()
    math.pi

Moduł ``statistics`` w bibliotece standardowej
==============================================

.. code-block:: python

    import statistics

    statistics.avg()
    statistics.mean()
    statistics.stdev()

Moduł ``random`` w bibliotece standardowej
==========================================

.. code-block:: python

    import random

    random.sample()
    random.random()

Zadania kontrolne
=================

Obliczanie odległości między dwoma punktami - Eucledean Distance
----------------------------------------------------------------
Dla dwóch (constant) punktów ``x`` i ``y`` o podanych koordynatach napisz program, który obliczy odległość między nimi wykorzystując algorytm Eucledesa.

:Zadanie z gwiazdką:
    Przekształć algorytm tak, aby działał w :math:`N` wymiarowej przestrzeni.

.. figure:: ../machine-learning/img/k-nearest-neighbors-euclidean-distance.png
    :scale: 100%
    :align: center

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.


Przeliczenia trygonometryczne
-----------------------------
Napisz program, który wczyta od użytkownika wielkość kąta w stopniach i wyświetli wartość czterech podstawowych funkcji trygonometrycznych (sin, cos, tg, ctg) o ile dla danego kąta jest to możliwe.

:Zadanie z gwiazdką:
    Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta, zwróć wyjątek ``ValueError('dla tego kąta wartośćfunkcji nie istnieje')``


Lotto
-----
Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.

:Podpowiedź:
    * ``random.randrange()``
    * ``random.sample()``

:Pytania:
    * Czym sa liczby pseudolosowe?
    * Czy da się stworzyć program czysto losowy?
    * Dlaczego?


Pole trójkąta
-------------
Napisz program, który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. Wykorzystaj doctest do przetestowania funckji.


