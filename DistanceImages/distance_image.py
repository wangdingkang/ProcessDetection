from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import os
import numpy as np
from sklearn.neighbors import NearestNeighbors


# distance image from source_path to target_path, find NN from source pixels in target pixel.
def get_distance_image(source_path, target_path, threshold=128):
    im_source = Image.open(source_path)
    im_target = Image.open(target_path)
    source_arr = np.array(im_source)
    target_arr = np.array(im_target)
    width, height = im_source.size
    distimg_arr = np.zeros((width, height))

    source_id = np.argwhere(source_arr > threshold)
    target_id = np.argwhere(target_arr > threshold)

    if len(source_id) == 0:
        pass
    elif len(target_id) == 0:
        for id in source_id:
            distimg_arr[id[0]][id[1]] = 255
    else:
        nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(target_id)
        # print(source_id)
        # from source id to target id

        distances, _ = nbrs.kneighbors(source_id)
        for id, dist in zip(source_id, distances):
            distimg_arr[id[0]][id[1]] = dist
    return Image.fromarray(distimg_arr.astype('uint8'), 'L')