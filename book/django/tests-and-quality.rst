*****************
Tests and quality
*****************

Tests
=====
* https://docs.djangoproject.com/en/2.0/topics/testing/overview/

.. literalinclude:: src/django-tests.py
    :language: python
    :name: listing-django-tests
    :caption: Django Tests

.. code-block:: console

    # By default, this will discover tests in any file named “test*.py” under the current working directory.
    $ python manage.py test --parallel

    # Run all the tests in the animals.tests module
    $ ./manage.py test animals.tests

    # Run all the tests found within the 'animals' package
    $ ./manage.py test animals

    # Run just one test case
    $ ./manage.py test animals.tests.AnimalTestCase

    # Run just one test method
    $ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

Test URLs
=========
.. code-block:: python

    import logging
    from django.contrib.auth.models import User
    from django.test import TestCase
    from django.test.client import Client


    class Test(TestCase):
        assert_http_200 = []

        def setUp(self):
            self.logger = logging.getLogger(__name__)
            self.user = User.objects.create_superuser('testrunner', 'test@test.com', 'testrunner')
            self.client.login(username='testrunner', password='testrunner')

        def tearDown(self):
            self.client.logout()
            self.user.delete()

        def test_http_200(self):
            for url in self.assert_http_200:
                response = self.client.get(url)

                if response.status_code != 200:
                    self.logger.error(f'{response.status_code} {url}')
                    raise AssertionError(f'HTTP {response.status_code} for "{url}"')
                else:
                    self.logger.info(f'{response.status_code} {url}')

.. code-block:: python

    from habitat.tests import Test


    class ExtravehucularTest(Test):
        assert_http_200 = [
            '/extravehicular/',

            '/extravehicular/activity/',
            '/extravehicular/activity/add/',

            '/extravehicular/contingency/',
            '/extravehicular/contingency/add/',

            '/extravehicular/location/',
            '/extravehicular/location/add/',

            '/extravehicular/objective/',
            '/extravehicular/objective/add/',

            '/extravehicular/report/',
            '/extravehicular/report/add/',

            '/extravehicular/spacewalker/',
            '/extravehicular/spacewalker/add/',
        ]


SonarQube
=========
.. code-block:: text

    sonar.host.url=https://sonarcloud.io
    sonar.organization=astromatt
    sonar.login=...

    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true

    sonar.projectKey=habitatOS
    sonar.projectName=habitatOS
    sonar.projectDescription=Operating System for analog extraterrestrial habitats.
    sonar.links.homepage=https://bitbucket.org/AstroMatt/habitatOS/
    sonar.links.scm=https://bitbucket.org/AstroMatt/habitatOS/
    sonar.links.issue=https://bitbucket.org/AstroMatt/habitatOS/issues
    sonar.links.ci=https://bitbucket.org/AstroMatt/habitatos/addon/pipelines/home

    sonar.projectBaseDir=habitat
    sonar.sources=.
    sonar.exclusions=**/migrations/**

    # Pylint
    sonar.python.pylint=/usr/local/bin/pylint
    sonar.python.pylint_config=.pylintrc
    sonar.python.pylint.reportPath=pylint-report.txt

    # Unit tests
    sonar.python.xunit.reportPath=test-reports/*.xml
    sonar.python.coverage.reportPath=coverage.xml

    # Integration tests
    sonar.python.coverage.itReportPath=it-coverage.xml

    # Turn off these rules
    sonar.issue.ignore.multicriteria=e1,e2
    # python:s100: "Method names should comply with a naming convention" gives many false positives when overriding
    # TestCase methods (such as setUp and tearDown) in test files.
    sonar.issue.ignore.multicriteria.e1.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e1.resourceKey=**/tests.py
    sonar.issue.ignore.multicriteria.e2.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e2.resourceKey=**/tests.py

Debug Toolbar
=============
