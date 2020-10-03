#!/usr/bin/env python3

import pandas
import tensorflow as tf
from pathlib import Path
import shutil, os

DNNClassifier = tf.estimator.DNNClassifier(

    # for a DNN, this feature_columns object is really just a definition
    # of the input layer
    feature_columns=[tf.feature_column.numeric_column(key='features',
                                                      shape=(320),  # this is apparently always num features times 2
                                                      dtype=tf.float32)],

    # four hidden layers with 256 nodes in each layer
    hidden_units=[256, 256, 256, 256],

    # number of classes (aka number of nodes on the output layer)
    n_classes=3,

)


def parser(record):
    '''
    This is a parser function. It defines the template for
    interpreting the examples you're feeding in. Basically,
    this function defines what the labels and data look like
    for your labeled data.
    '''

    # the 'features' here include your normal data feats along
    # with the label for that data
    features = {
        'features': tf.FixedLenFeature([], tf.string),
        'label': tf.FixedLenFeature([], tf.int64),
    }

    parsed = tf.parse_single_example(record, features)

    # some conversion and casting to get from bytes to floats and ints
    features = tf.convert_to_tensor(tf.decode_raw(parsed['features'], tf.float32))
    label = tf.cast(parsed['label'], tf.int64)

    # since you can have multiple kinds of feats, you return a dictionary for feats
    # but only an int for the label
    return {'features': features}, label


def my_input_fn(tfrecords_path):
    dataset = (
        tf.data.TFRecordDataset(tfrecords_path)
            .map(parser)
            .batch(32)  # look up what this means
    )

    iterator = dataset.make_one_shot_iterator()

    batch_feats, batch_labels = iterator.get_next()

    return batch_feats, batch_labels


if __name__ == '__main__':
    path = 'train.tfrecords'
    my_input_fn(path)

    train_spec_dnn = tf.estimator.TrainSpec(input_fn=lambda: my_input_fn('./train/train.tfrecords'), max_steps=1000)
    eval_spec_dnn = tf.estimator.EvalSpec(input_fn=lambda: my_input_fn('./test/csv.tfrecords'))

    tf.estimator.train_and_evaluate(DNNClassifier, train_spec_dnn, eval_spec_dnn)

    predictions = list(DNNClassifier.predict(input_fn=lambda: my_input_fn('./test/csv.tfrecords')))
    print(predictions)

    output_data = pandas.DataFrame(predictions)

    output_data_to_csv = output_data.to_csv('./results/predictions_data.csv', index=None, header=True)
