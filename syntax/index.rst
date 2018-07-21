******
Syntax
******


Indentation instead of braces
=============================
Jest to chyba najciekawsza rzecz w samym języku. Autorzy specyfikacji zdecydowali się na zastąpienie nawiasów klamrowych wcięciami, czyli tzw. białymi spacjami (ang. whitespace). Jest to dość nietypowe rozwiązanie, które okazało się bardzo rewolucyjne i niesamowicie podniosło czytelność kodu źródłowego.

Sama idea spowodowała dużą polaryzację programistów. Jedni bardzo sobie chwalą to rozwiązanie, a inni przyzwyczajeni do języków przypominających składnią C są jej zaciekłymi wrogami. Osobiście jestem wielkim zwolennikiem takiego rozwiązania!

.. code-block:: python

    from __future__ import braces
    # SyntaxError: not a chance


End lines
=========
Pierwszą rzeczą (poza znaczącymi wcięciami), która może zaskoczyć programistów przyzwyczajonych do składni C jest brak konieczności, a nawet zalecenie do niestawiania znaku średnika ``;`` na końcu linii. Programy interpretowane są linia po linii. Linia kończy się tam, gdzie ostatni znak polecenia.

Python pozwala na stosowanie znaków końca linii zarówno znanych z systemów Windows (\r\n) jak i środowiska \*nix (\n). W tych materiałach będziemy posługiwali się znakiem \n symbolizującym koniec linii.


Comments
========
Komentarze są wykorzystywane by podpowiedzieć programiście, który będzie czytał kod źródłowy w przyszłości co dana funkcja, metoda lub po prostu kolejna linijka kodu robi. Jestem wielkim fanem pisania tak swoich programów, aby komentarze w kodzie były zbędne. Dobrego dzielenia aplikacji na mniejsze części, właściwego stosowania whitespace'ów, precyzyjnego i opisowego ich nazywania. Komentarze mogą być bardzo przydatne, ale w większości sytuacji jeżeli potrzebujemy z nich skorzystać to znaczy, że logicznie źle rozplanowaliśmy układ naszego kodu. Ponadto komentarze mają brzydką właściwość szybkiego starzenia się, tzn. kod ewoluuje, a komentarz opisuje zachowanie starej funkcji. Może to powodować dezinformację.

Commented code
--------------
Bardzo często spotykam się z problemem zakomntowanego kodu. O ile komentarze opisujące działanie poszczególnych elementów są użyteczne to zakomentowany kod jest nieakceptowalny. Często stosujemy tą technikę by chwilowo wyłączyć działanie jakiejś funkcjonalności. Jednakże niedopuszczalne jest commitowanie zmian zawierających zakomentowany kod. Kod taki bardzo często jest już niedziałający i taki pozostanie na zawsze. Bardzo często słyszę argument, że może kiedyś będziemy chcieli powrócić do tego kodu i bez sensu będzie go wymyślać i pisać na nowo. W dobie systemów kontroli wersji sytuacja ta nie będzie stwarzała jakiegokolwiek problemu. Wystarczy przeglądnąć diffa (podgląd różnicowy) pliku albo wykonać ``git blame`` i mamy dostęp do starego sposobu.

Nieuruchamiający się i niewywoływany kod nie powinien znaleźć się w repozytorium. Kropka!

Commenting line
---------------
W Pythonie mamy kilka sposobów komentowania. Najprostszym z nich jest komentowanie całej linii poprzez wykorzystanie znaku zwanego "pound" lub "hash" ``#``. Ciąg znaków znajdujących się za ``#`` zostanie zignorowany przez kompilator.

.. code-block:: python

    >>> # na ekranie otrzymamy: Hello World!
    ... print('Hello World!')
    Hello World!

Tu możemy zaobserwować zachowanie, o którym wspominaliśmy trochę wcześniej, tzn. kontynuacja jest oznaczana przez znak zachęty trzech kropek ``...``.

Inline comments
---------------
Kolejnym sposobem jest komentowanie inline tzn. w linijce. Tego typu komentarze stosuje się aby wytłumaczyć zachowanie poszczególnych linii kodu. Choć kompilator dopuszcza ich stosowanie, to w ramach dobrych praktyk lepiej zastąpić je komentarzami w linijce poprzedzającej wywołanie.

.. code-block:: python

    >>> print('Hello World!')  # na ekranie otrzymamy: Hello World!
    Hello World!


Multiline comments
------------------
Komentarze wieloliniowe w Pythonie można robić na dwa sposoby poprzez wykorzystanie trzech znaków cudzysłowia:

* pojedynczego ``'''``,
* podwójnego ``"""``.

W jednym i drugim przypadku cudzysłowie podwójne lub pojedyncze będzie oznaczało początek jak i koniec komentarza. Rodzaj cudzysłowiów nie ma znaczenia, ale utarło się aby stosować podwójne ``"``. W materiałach będziemy korzystać właśnie z tej notacji.

.. code-block:: python

    """
    Tu jest treść komentarza, który obejmuje wiele linii
    W ramach dobrych praktyk, powinniśmy takim komentarzem opisać każdą z funkcji,
    aby narzędzia takie jak np. ``help()`` wyświetlały ładne podpowiadanie działania.
    """

Są dwie szkoły tworzenia takich komentarzy. Jedna mówi, aby tekst pisać bezpośrednio po znaku cudzysłowia, a druga od nowej linijki. Jest to kwestia estetyki i czytelności komentarza.

Docstring
---------
Pierwszy wielolinijkowy komentarz w pliku jest traktowany jako opis modułu. Może się w nim znajdować np. licencja użytkowania programu, instrukcja jego obsługi itp. Bardzo ciekawym pomysłem jest również napisanie komentarza opisującego parametry programów wykorzystującego standard \*unix takiego opisu. Dzięki temu poza samym jednoznacznym opisem działania programu zgodnym z ogólnie przyjętą konwencją dostajemy możliwość wykorzystania modułu docopt do jego sparsowania i obsługi parametrów przekazywanych z linii poleceń.
