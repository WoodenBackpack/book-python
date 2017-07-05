**********************************
Principal Component Analysis (PCA)
**********************************

What is Principal Component Analysis?
=====================================
Principal component analysis (PCA) is a technique used to emphasize variation and bring out strong patterns in a dataset. It's often used to make data easy to explore and visualize.

Linear dimensionality reduction using Singular Value Decomposition of the data to project it to a lower dimensional space.

2D example
==========
* http://setosa.io/ev/principal-component-analysis/

First, consider a dataset in only two dimensions, like (height, weight). This dataset can be plotted as points in a plane. But if we want to tease out variation, PCA finds a new coordinate system in which every point has a new (x,y) value. The axes don't actually mean anything physical; they're combinations of height and weight called "principal components" that are chosen to give one axes lots of variation.

.. figure:: img/principal-component-analysis.png
    :scale: 75%
    :align: center

    PCA is useful for eliminating dimensions. If we're going to only see the data along one dimension, though, it might be better to make that dimension the principal component with most variation. We don't lose much by dropping PC2 since it contributes the least to the variation in the data set.

.. code-block:: python

    >>> import numpy as np
    >>> from sklearn.decomposition import PCA
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> pca = PCA(n_components=2)
    >>> pca.fit(X)
    PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
      svd_solver='auto', tol=0.0, whiten=False)
    >>> print(pca.explained_variance_ratio_)
    [ 0.99244...  0.00755...]

.. code-block:: python

    >>> pca = PCA(n_components=2, svd_solver='full')
    >>> pca.fit(X)
    PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
      svd_solver='full', tol=0.0, whiten=False)
    >>> print(pca.explained_variance_ratio_)
    [ 0.99244...  0.00755...]

.. code-block:: python

    >>> pca = PCA(n_components=1, svd_solver='arpack')
    >>> pca.fit(X)
    PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
      svd_solver='arpack', tol=0.0, whiten=False)
    >>> print(pca.explained_variance_ratio_)
    [ 0.99244...]

Przykłady praktyczne
====================
https://github.com/scikit-learn/scikit-learn/tree/master/examples/decomposition

PCA dla zbioru Iris
-------------------
.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D


    from sklearn import decomposition
    from sklearn import datasets

    np.random.seed(5)

    centers = [[1, 1], [-1, -1], [1, -1]]
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    plt.cla()
    pca = decomposition.PCA(n_components=3)
    pca.fit(X)
    X = pca.transform(X)

    for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
        ax.text3D(X[y == label, 0].mean(),
                  X[y == label, 1].mean() + 1.5,
                  X[y == label, 2].mean(), name,
                  horizontalalignment='center',
                  bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))

    # Reorder the labels to have colors matching the cluster results
    y = np.choose(y, [1, 2, 0]).astype(np.float)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.spectral, edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])

    plt.show()

.. figure:: img/pca-iris.png
    :name: PCA dla zbioru Iris
    :scale: 120%
    :align: center

    PCA dla zbioru Iris



Zadania kontrolne
=================

PCA dla zbioru Pima Indian Diabetes
-----------------------------------
Przeprowadź analizę PCA dla zbioru Indian Pima
