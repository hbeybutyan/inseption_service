import tensorflow as tf
from tensorflow import gfile
from id_to_string_converter import IdToStringConverter
import numpy as np
from constants import GRAPH_DEF_PATH
#from tensorflow.python.summary import summary
from tensorflow import summary
class Inferor:
    def __init__(self):
        self.converter = IdToStringConverter()
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
            softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
            features_tensor = sess.graph.get_tensor_by_name('pool_3:0')
            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            features_predictions = sess.run(features_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            print(predictions.shape)
            print(features_predictions.shape)
            predictions = np.squeeze(predictions)
            print(features_predictions.shape)
            print(predictions.shape)
            pb_visual_writer = summary.FileWriter("/home/strata/univ/inseption_service/logs")
            pb_visual_writer.add_graph(sess.graph)

            # Creates node ID --> English string lookup.

            top_k = predictions.argsort()[-5:][::-1]
            top_k_strings = []
            for node_id in top_k:
                human_string = self.converter.id_to_string(node_id)
                score = predictions[node_id]
                top_k_strings.append({human_string, score})
            return top_k_strings

    def load_graph(self):
        """"Loads a graph from file."""
        with gfile.FastGFile(GRAPH_DEF_PATH, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

