import os.path

RESOURCES_PATH = "/home/strata/univ/inseption_service/resources"
GRAPH_DEF_PATH = os.path.join(RESOURCES_PATH, 'classify_image_graph_def.pb')
LABEL_MAP_PATH = os.path.join(RESOURCES_PATH, 'imagenet_2012_challenge_label_map_proto.pbtxt')
HUMAN_LABEL_MAP_PATH = os.path.join(RESOURCES_PATH, 'imagenet_synset_to_human_label_map.txt')