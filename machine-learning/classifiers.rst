.. _Classifiers:

***********
Classifiers
***********

Co to jest Classifier?
======================
A mapping from unlabeled instances to (discrete) classes. Classifiers have a form (e.g., decision tree) plus an interpretation procedure (including how to handle unknowns, etc.). Some classifiers also provide probability estimates (scores), which can be thresholded to yield a discrete class decision thereby taking into account a utility function.


Schemat działania classifiera
=============================
#. Collect Training Data
#. Train Classifier
#. Make Predictions

.. figure:: img/classification-spam.png
    :scale: 75%
    :align: center

    Schemat działania classifiera. Wiadomości email przechodząc przez classifer są oznaczane jako spam, lub nie spam.


Writing Own Classifier
======================

Random Classifier
-----------------

.. code-block:: python

    import random


    class MyClassifier():
        def fit(self, x_train, y_train):
            # Memorize
            self.x_train = x_train
            self.y_train = y_train

        def predict(self, x_test):
            predictions = []

            for row in x_test:
                label = random.choice(self.y_train)
                predictions.append(label)

            return predictions

Accuracy for Iris dataset: 0.346666666667

Nearest Neighbor Classifier
---------------------------
.. code-block:: python

    def euclidean_distance(point_from_numeric_data, point_from_testing_data):
        return distance.euclidean(point_from_numeric_data, point_from_testing_data)


    class MyClassifier():

        def fit(self, x_train, y_train):
            # Memorize
            self.x_train = x_train
            self.y_train = y_train

        def predict(self, x_test):
            predictions = []

            for row in x_test:
                label = self.closest(row)
                predictions.append(label)

            return predictions

        def closest(self, row):
            best_dist = euclidean_distance(row, self.x_train[0])
            best_index = 0

            for i in range(0, len(self.x_train)):
                dist = euclidean_distance(row, self.x_train[i])
                if dist < best_dist:
                    best_dist = dist
                    best_index = i

            return self.y_train[best_index]

Accuracy for Iris dataset: 0.946666666667

Zadania praktyczne
==================

Spam Classifier
---------------
#. Stwórz classifier który na podstawie wiadomości email zakwalifikuje je jako SPAM lub nie SPAM.

#. Zakwalifikuj wiadomości jak na przykładzie poniżej:

    ===============================  ========
    Email                            Labels
    ===============================  ========
    Click here to claim your prize!  Spam
    What's new?                      Not Spam
    Hang out later?                  Not Spam
    You have won $1,000,000          Spam
    Enlarge your...                  Spam
    Nigerian prince                  Spam
    ===============================  ========

#. Przygotuj dwie partycje danych:

    - treningową
    - testową

#. Skorzystaj treningowej bazy danych wiadomości spam

