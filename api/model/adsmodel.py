from abc import ABC

import tensorflow as tf

from api import utils_ops


class AdsModel(object):

    def __init__(self, path_to_graph):
        self._sess = None
        self._image_tensor = None
        self._tensor_dict = {}

        # Initialize graph
        self._detection_graph = tf.Graph()

        with self._detection_graph.as_default():
            od_graph_def = tf.GraphDef()

            with tf.gfile.GFile(path_to_graph, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

    def initialize_session(self):
        with self._detection_graph.as_default():
            self._sess = tf.Session()
            ops = tf.get_default_graph().get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            self._tensor_dict = {}

            for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes', 'detection_masks']:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    self._tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)

            if 'detection_masks' in self._tensor_dict:
                # The following processing is only for single image
                detection_boxes = tf.squeeze(self._tensor_dict['detection_boxes'], [0])
                detection_masks = tf.squeeze(self._tensor_dict['detection_masks'], [0])

                # Reframe is required to translate mask from box coordinates to image coordinates and
                # fit the image size.
                real_num_detection = tf.cast(self._tensor_dict['num_detections'][0], tf.int32)
                detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
                detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
                detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(detection_masks, detection_boxes,
                                                                                      image.shape[0], image.shape[1])
                detection_masks_reframed = tf.cast(tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                # Follow the convention by adding back the batch dimension
                self._tensor_dict['detection_masks'] = tf.expand_dims(detection_masks_reframed, 0)

        self._image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

    def close_session(self):
        """Closes the session"""
        self._sess.close()

    def predict(self, image):
        feed_dict = {self._image_tensor: np.expand_dims(image, 0)}
        output_dict = self._sess.run(self._tensor_dict, feed_dict=feed_dict)

        # all outputs are float32 numpy arrays, so convert types as appropriate
        output_dict['num_detections'] = int(output_dict['num_detections'][0])
        output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
        output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
        output_dict['detection_scores'] = output_dict['detection_scores'][0]
        if 'detection_masks' in output_dict:
            output_dict['detection_masks'] = output_dict['detection_masks'][0]

        return output_dict
