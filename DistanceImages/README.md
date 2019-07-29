By default, input images will be first binarized by hard-thresholding of value 128. 

The input should be 8-bit grayscale images. If not, you need to change the threshold correspondingly.

Distance images are 8-bit grayscale images. It computes, for each pixel in source image, the distance from it to its NN in the target image.

For example, if you call get_distance_image(predication, annotation), it will return a image in which each non-zero pixel corresponding to a
false positive element (based on the annotation). Since the annotation might not be perfect, it can be considered as a useful feedback
to annotators, if there is any process missed in the annotation.

Conversely, the distance image from annotation to prediction captures false negative. Similarly, it can be used as a reference if there is
mislabeled process.
