****************************
Convolutional Neural Network
****************************

.. todo:: Zrobić aby wykorzystywało szablon ``_template.rst``

Combination of:

    - Deep Neural Networks
    - Kernel Convolutions
    - With assumption, that input is image

.. figure:: img/convolutional-neural-network-overview.png
    :scale: 66%
    :align: center

    General overview of Convolutional Neural Network


Problemy z przetwarzaniem obrazów
=================================
* cienie
* nakładające się obrazy
* zmiany kąta i pochyłości kamery
* kąt padania światła
* kolorystyka
* zakrzywienia płaszczyzny
* szumy


What is and Kernel Convolution?
===============================

.. figure:: img/convolutional-neural-network-kernels.png
    :scale: 75%
    :align: center

    Convolutional Neural Network with 3x3 kernel convolutions

.. figure:: img/convolution-filter-mean.gif
    :scale: 33%
    :align: center

    Convolution with 3x3 kernel for Mean Blur Filter

.. figure:: img/convolution-filter-gaussian.gif
    :scale: 33%
    :align: center

    Convolution with 3x3 kernel for Gaussian Blur Filter


What is Convolutional Neural Network (CNN / ConvNet)
====================================================

.. figure:: img/convolutional-neural-network-architecture.jpg
    :scale: 66%
    :align: center

    Architecture of the Convolutional Neural Network

Convolutional Neural Networks are very similar to ordinary Neural Networks from the previous chapter: they are made up of neurons that have learnable weights and biases. Each neuron receives some inputs, performs a dot product and optionally follows it with a non-linearity. The whole network still expresses a single differentiable score function: from the raw image pixels on one end to class scores at the other. And they still have a loss function (e.g. SVM/Softmax) on the last (fully-connected) layer and all the tips/tricks we developed for learning regular Neural Networks still apply.

.. figure:: img/convolutional-neural-network-transformation.png
    :scale: 66%
    :align: center

    Convolutional Neural Network layer pool transformation

So what does change? ConvNet architectures make the explicit assumption that the inputs are images, which allows us to encode certain properties into the architecture. These then make the forward function more efficient to implement and vastly reduce the amount of parameters in the network.

.. figure:: img/convolutional-neural-network-example.jpg
    :scale: 75%
    :align: center

    Convolutional Neural Network example


.. code-block:: python

    import tensorflow as tf
    from tensorflow.examples.tutorials.mnist import input_data


    mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

    # MNIST total classes (0-9 digits)
    n_classes = 10
    batch_size = 128

    # tf Graph input
    x = tf.placeholder('float', [None, 784])
    y = tf.placeholder('float')

    keep_rate = 0.8
    keep_prob = tf.placeholder(tf.float32)


    def conv2d(input, filter):
        return tf.nn.conv2d(
            input=input,
            filter=filter,
            strides=[1, 1, 1, 1],
            padding='SAME')


    def maxpool2d(value):
        return tf.nn.max_pool(
            value=value,
            padding='SAME',

            # size of window
            ksize=[1, 2, 2, 1],

            # movement of windo
            strides=[1, 2, 2, 1])


    def convolutional_neural_network(x):
        weights = {
            # 5 x 5 convolution, 1 input image, 32 outputs
            'W_conv1': tf.Variable(tf.random_normal([5, 5, 1, 32])),

            # 5x5 conv, 32 inputs, 64 outputs
            'W_conv2': tf.Variable(tf.random_normal([5, 5, 32, 64])),

            # fully connected, 7*7*64 inputs, 1024 outputs
            'W_fc': tf.Variable(tf.random_normal([7 * 7 * 64, 1024])),

            # 1024 inputs, 10 outputs (class prediction)
            'out': tf.Variable(tf.random_normal([1024, n_classes]))}

        biases = {
            'b_conv1': tf.Variable(tf.random_normal([32])),
            'b_conv2': tf.Variable(tf.random_normal([64])),
            'b_fc': tf.Variable(tf.random_normal([1024])),
            'out': tf.Variable(tf.random_normal([n_classes]))}

        # Reshape input to a 4D tensor
        x = tf.reshape(
            tensor=x,
            shape=[-1, 28, 28, 1])

        # Convolution Layer, using our function
        # Computes rectified linear: max(features, 0)
        conv1 = tf.nn.relu(conv2d(x, weights['W_conv1']) + biases['b_conv1'])

        # Max Pooling (down-sampling)
        conv1 = maxpool2d(conv1)

        # Convolution Layer
        # Computes rectified linear: max(features, 0)
        conv2 = tf.nn.relu(conv2d(conv1, weights['W_conv2']) + biases['b_conv2'])

        # Max Pooling (down-sampling)
        conv2 = maxpool2d(conv2)

        # Fully connected layer
        # Reshape conv2 output to fit fully connected layer
        fc = tf.reshape(conv2, [-1, 7 * 7 * 64])

        # Computes rectified linear: max(features, 0)
        fc = tf.nn.relu(tf.matmul(fc, weights['W_fc']) + biases['b_fc'])

        # Computes dropout
        fc = tf.nn.dropout(fc, keep_rate)

        # Multiplies matrix `a` by matrix `b`, producing `a` * `b`
        return tf.matmul(fc, weights['out']) + biases['out']


    def train_neural_network(x):
        prediction = convolutional_neural_network(x)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
        optimizer = tf.train.AdamOptimizer().minimize(cost)

        hm_epochs = 10
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())

            for epoch in range(hm_epochs):
                epoch_loss = 0

                for _ in range(int(mnist.train.num_examples / batch_size)):
                    epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                    _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                    epoch_loss += c

                print(f'Epoch {epoch} completed out of {hm_epochs} loss {epoch_loss}')

            correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

            accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

            print('Accuracy:', accuracy.eval({
                x: mnist.test.images,
                y: mnist.test.labels
            }))


    train_neural_network(x)

MNIST za pomocą biblioteki ``keras``
------------------------------------

.. code-block:: python

    '''Trains a simple convnet on the MNIST dataset.
    Gets to 99.25% test accuracy after 12 epochs
    (there is still a lot of margin for parameter tuning).
    16 seconds per epoch on a GRID K520 GPU.
    '''

    import keras
    from keras.datasets import mnist
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Flatten
    from keras.layers import Conv2D, MaxPooling2D
    from keras import backend as K

    batch_size = 128
    num_classes = 10
    epochs = 12

    # input image dimensions
    img_rows, img_cols = 28, 28

    # the data, shuffled and split between train and test sets
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu',
                     input_shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

Przydatne odnośniki
===================
* https://github.com/fchollet/keras/tree/master/examples
