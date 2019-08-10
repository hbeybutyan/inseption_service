import tensorflow as tf
from tensorflow import gfile
import numpy as np
from constants import GRAPH_DEF_PATH
class Inferor:
    def __init__(self):
        pass

    def infer(self, image):
        """Runs inference on an image.
        Args:
          image: Image file name.
        Returns:
          Nothing
        """
        # image_data = gfile.FastGFile(image, 'rb').read()
        image_data = image.read()

        # Creates graph from saved GraphDef.
        self.load_graph()

        with tf.Session() as sess:
            # Some useful tensors:
            # 'softmax:0': A tensor containing the normalized prediction across
            #   1000 labels.
            # 'pool_3:0': A tensor containing the next-to-last layer containing 2048
            #   float description of the image.
            # 'DecodeJpeg/contents:0': A tensor containing a string providing JPEG
            #   encoding of the image.
            # Runs the softmax tensor by feeding the image_data as input to the graph.
            features_tensor = sess.graph.get_tensor_by_name('pool_3:0')
            features_predictions = sess.run(features_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            print(features_predictions.shape)
            features_predictions = np.squeeze(features_predictions)
            features_predictions = np.expand_dims(features_predictions, 0)
            print(features_predictions.shape)
            return features_predictions


    def load_graph(self):
        """"Loads a graph from file."""
        with gfile.FastGFile(GRAPH_DEF_PATH, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

