*****************
System Operacyjny
*****************


Sprawdzanie systemu operacyjnego
================================
* Linux: Linux
* Mac: Darwin
* Windows: Windows

``platform``
------------
.. code-block:: python

    import platform

    platform.system()  # Windows
    platform.release()  # 7
    platform.platform()  # 'Windows-7-6.1.7601-SP1'
    platform.os.name  # 'nt'

    platform.uname()
    # uname_result(system='Windows', node='Lenovo-Komputer', release='7', version='6.1.7601', machine='AMD64', processor='Intel64 Family 6 Model 42 Stepping 7, GenuineIntel')

    platform.win32_ver()  # ('7', '6.1.7601', 'SP1', 'Multiprocessor Free')
    platform.mac_ver()
    platform.linux_distribution()  # deprecated since Python 3.5

    platform.uname()  # not working of Windows
    # ('Darwin', 'mainframe.local', '15.3.0', 'Darwin Kernel Version 15.3.0: Thu Dec 10 18:40:58 PST 2015; root:xnu-3248.30.4~1/RELEASE_X86_64', 'x86_64', 'i386')

``os``
------
.. code-block:: python

    import os

    os.name  # 'nt'
    os.name  # 'posix'

``psutil``
----------
.. code-block:: python

    import psutil

    psutil.OSX      # False
    psutil.WINDOWS  # True
    psutil.LINUX    # False

``sys``
-------
.. code-block:: python

    import sys

    sys.platform
    # 'win32'


``os``
======
.. code-block:: python

    import os

    os.walk()
    os.scandir()
    os.getcwd()
    os.stat()

    os.path.join()
    os.path.abspath()
    os.path.dirname()
    os.path.basename()

    os.mkdir()
    os.remove()
    os.rmdir()

.. code-block:: python

    >>> import os
    >>> os.path.isdir(os.path.join("c:", "\\", "Users"))
    True

    >>> os.path.isdir(os.path.join("c:", "/", "Users"))
    True

    >>> os.path.isdir(os.path.join("c:", os.sep, "Users"))
    True

.. code-block:: python

    import os

    for element in os.scandir('/etc'):
        print(element.name)

    script = os.path.basename(__file__)
    PWD = os.path.basename(os.getcwd())

    path = os.path.join(PWD, script)

    print(path)

.. code-block:: python

    import os
    from os.path import join, getsize


    for root, dirs, files in os.walk('/home/'):
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

.. code-block:: python

    # Delete everything reachable from the directory named in "top",
    # assuming there are no symbolic links.
    # CAUTION:  This is dangerous!  For example, if top == '/', it
    # could delete all your disk files.
    import os
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

Stats and permissions
---------------------
.. code-block:: python

    import os

    output = os.stat(r'c:\Python\__notepad__.py')
    print(output)
    # os.stat_result(st_mode=33206, st_ino=3659174697409906, st_dev=3763209288, st_nlink=1, st_uid=0, st_gid=0, st_size=780, st_atime=1530775767, st_mtime=1530775767, st_ctime=1523261133)

    oct_perm = oct(output.st_mode)
    print(oct_perm)
    # 0o100666

Permissions
-----------
.. code-block:: python

    import os

    os.access(r'C:\Python\README.rst', os.R_OK)
    # True
    os.access(r'C:\Python\README.rst', os.W_OK)
    # True
    os.access(r'C:\Python\README.rst', os.X_OK)
    # True

    os.access(r'C:\Python\notREADME.rst', os.R_OK)
    # False
    os.access(r'C:\Python\notREADME.rst', os.W_OK)
    # False
    os.access(r'C:\Python\notREADME.rst', os.X_OK)
    # False


``sys``
=======

Najczęściej wykorzystuje się:

.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.platform
    sys.path.insert(0, '/path/to/directory')
    sys.path.insert(index=0, object='/path/to/directory')

.. code-block:: python

    import sys

    sys.exit(0)


``subprocess``
==============

Najczęściej wykorzystuje się:

.. code-block:: python

    import subprocess

    subprocess.call('clear')
    subprocess.run()  # preferred for Python >= 3.5
    subprocess.Popen()  #

``subprocess.Popen()``
----------------------
* Used in Python < 3.5
* In Python >= 3.5 use ``subprocess.run()``

.. code-block:: python

    subprocess.Popen(
        args,
        stdin=None,
        stdout=None,
        stderr=None,
        shell=False,
        cwd=None,
        env=None,
        encoding=None,
        errors=None,
        # ... there are other, less commonly used parameters
    )

``subprocess.run()``
--------------------
* New in Python 3.5
* Preferred

.. code-block:: python

    subprocess.run(
        args,
        stdin=None,
        stdout=None,
        stderr=None,
        shell=False,
        timeout=None,  # important
        check=False,
        encoding=None
    )

``shell=True``
--------------

.. code-block:: python

    >>> import subprocess

    >>> subprocess.call('echo $HOME')
    Traceback (most recent call last):
    ...
    OSError: [Errno 2] No such file or directory


    >>> import subprocess
    >>> subprocess.call('echo $HOME', shell=True)
    /home/jose-jimenez
    0

Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process, and tell it to run the command. In other words, using an intermediate shell means that variables, glob patterns, and other special shell features in the command string are processed before the command is run. Here, in the example, ``$HOME`` was processed before the echo command. Actually, this is the case of command with shell expansion while the command ``ls -l`` considered as a simple command.

.. note:: source: `Subprocess Module <https://stackoverflow.com/a/36299483/228517>`

Uruchamianie poleceń
--------------------
.. code-block:: python

    subprocess.run('ls -la /home')  # doesn't capture output

.. code-block:: python

    import subprocess

    cmd = 'dir ..'

    output = subprocess.run(
        cmd,
        timeout=2,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')

    print(output.stdout)
    print(output.stderr)

.. code-block:: python

    import subprocess
    import shlex

    cmd = 'dir ..'

    output = subprocess.run(
        shlex.split(cmd),  # ['dir', '..']
        timeout=2,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')

    print(output.stdout)
    print(output.stderr)



.. code-block:: python

    subprocess.run("exit 1", shell=True, check=True)
    # Traceback (most recent call last):
    #   ...
    # subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

.. code-block:: python

    subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
    # CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
    # stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')

.. code-block:: python

    import subprocess
    import shlex

    cmd = 'ls -la'

    with subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE) as proc:
        ret = proc.stdout.read()
        print(ret)

Timeout dla wykonywania poleceń
-------------------------------
.. code-block:: python

    import subprocess
    cmd = ['ping', 'nasa.gov']

    try:
        subprocess.run(cmd, timeout=5)
    except subprocess.TimeoutExpired:
        print('process ran too long')

Przechwytywanie outputu
-----------------------
.. code-block:: python

    import logging
    import subprocess
    import shlex


    def run(command, timeout=15, clear=True):

        if clear:
            subprocess.call('clear')

        logging.debug(f'Execute: {command}\n')

        result = subprocess.run(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            timeout=timeout,
            encoding='utf-8')

        if result.stdout:
            logging.info(f'{result.stdout}')

        if result.stderr:
            logging.warning(f'{result.stderr}')

        return result

Parsowanie i sanityzacja argumentów
-----------------------------------

.. code-block:: python

    import shlex
    import subprocess

    command_line = input()
    # /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"

    args = shlex.split(command_line)
    print(args)
    # ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]

    p = subprocess.Popen(args) # Success!

.. note:: pssh https://linux.die.net/man/1/pssh


``tempfile``
============

.. code-block:: python

    >>> import tempfile

    # create a temporary file and write some data to it
    >>> fp = tempfile.TemporaryFile()
    >>> fp.write(b'Hello world!')
    # read data from file
    >>> fp.seek(0)
    >>> fp.read()
    b'Hello world!'
    # close the file, it will be removed
    >>> fp.close()

    # create a temporary file using a context manager
    >>> with tempfile.TemporaryFile() as fp:
    ...     fp.write(b'Hello world!')
    ...     fp.seek(0)
    ...     fp.read()
    b'Hello world!'
    >>>
    # file is now closed and removed

    # create a temporary directory using the context manager
    >>> with tempfile.TemporaryDirectory() as tmpdirname:
    ...     print('created temporary directory', tmpdirname)
    >>>
    # directory and contents have been removed


``io``
======
* ``io`` to biblioteka do obsługi strumienia wejściowego i wyjściowego
* StringIO jest wtedy traktowany jak plik wejściowy.

.. code-block:: python

    import io

    io.StringIO

``configparser``
================
* Wczytywanie konfiguracji programów
.. code-block:: python

    import configparser

    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                          'Compression': 'yes',
                          'CompressionLevel': '9'}

    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}

    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'     # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'

    with open('example.ini', 'w') as configfile:
        config.write(configfile)

.. code-block:: ini

    [DEFAULT]
    ServerAliveInterval = 45
    Compression = yes
    CompressionLevel = 9
    ForwardX11 = yes

    [bitbucket.org]
    User = hg

    [topsecret.server.com]
    Port = 50022
    ForwardX11 = no


Running commands in parallel across many hosts
==============================================
https://linux.die.net/man/1/pssh


Passwords and secrets
=====================
* UMASK
* Sticky bit
* setuid
* configparser

Python Executable
=================
* https://py2app.readthedocs.io/
* http://www.py2exe.org/
* http://www.pyinstaller.org/


Allegro Tipboard
================
* http://allegro.tech/tipboard/
* https://github.com/allegro/tipboard

Tipboard is a system for creating dashboards, written in JavaScript and Python. Its widgets ('tiles' in Tipboard's terminology) are completely separated from data sources, which provides great flexibility and relatively high degree of possible customizations.

Because of its intended target (displaying various data and statistics in your office), it is optimized for larger screens.

Similar projects: Geckoboard, Dashing.

.. code-block:: console

    $ pip install tipboard
    $ tipboard create_project my_test_dashboard
    $ tipboard runserver


Assignments
===========

Rekursywne przechodzenie i wykonywanie poleceń
----------------------------------------------
#. Sprawdź czy katalog "Python" już istnieje na pulpicie w Twoim systemie
#. Jeżeli nie istnieje to za pomocą ``os.mkdir()`` stwórz go w tym miejscu
#. Za pomocą ``subprocess.call()`` w tym katalogu stwórz plik ``README.rst`` i dodaj do niego tekst "Ehlo World"
#. Przeszukaj rekurencyjnie wszystkie katalogi na pulpicie
#. Znajdź wszystkie pliki ``README`` (z dowolnym rozszerzeniem)
#. Wyświetl ich zawartość za pomocą polecenia:

    * ``cat`` (macOS, Linux)
    * ``type`` (Windows)

#. Ścieżkę do powyższego pliku ``README`` skonstruuj za pomocą ``os.path.join()``
#. Ścieżka ma być względna w stosunku do pliku, który aktualnie jest uruchamiany
#. Jeżeli po przeszukaniu całego Pulpitu rekurencyjnie skrypt nie znajdzie pliku ``LICENSE.rst``, to ma rzucić informację ``logging.critical()`` i wyjść z kodem błędu ``1``.

:Podpowiedź:
    * Gdyby był problem ze znalezieniem pliku, a ścieżka jest poprawna to zastosuj ``shell=True``
    * ``os.walk()``
    * ``subprocess.run()``

:Co to zadanie sprawdza?:
    * Przeglądanie katalogów i algorytm przeszykiwania
    * Sanityzacja parametrów
    * Logowanie wydarzeń w programie
    * Uruchamianie poleceń w systemie
    * Przechwytywanie outputu poleceń
    * Kody błędów
    * Przechodzenie do katalogów
    * Ścieżki względne i bezwzględne
    * Łączenie ścieżek

Tree
----
Za pomocą znaków unicode: "┣━", "┗━" , "┃  " wygeneruj wynik przypominający wynik polecenia ``tree``.


.. code-block:: text

    root:.
    [.]
    ┣━[.idea]
    ┃  ┣━[scopes]
    ┃  ┃  ┗━scope_settings.xml
    ┃  ┣━.name
    ┃  ┣━Demo.iml
    ┃  ┣━encodings.xml
    ┃  ┣━misc.xml
    ┃  ┣━modules.xml
    ┃  ┣━vcs.xml
    ┃  ┗━workspace.xml
    ┣━[test1]
    ┃  ┗━test1.txt
    ┣━[test2]
    ┃  ┣━[test2-2]
    ┃  ┃  ┗━[test2-3]
    ┃  ┃      ┣━test2
    ┃  ┃      ┗━test2-3-1
    ┃  ┗━test2
    ┣━folder_tree_maker.py
    ┗━tree.py
