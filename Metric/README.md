There are two functions in image_metrics.py. One is for computing regular TP, FP and FN. The other one is for computing modified TP, FP and FN.

By default, the input images are first binarized by hard-thresholding of 128, and the radius for calculating modified TP (FP, FN) is 2.

The definitions of modified TP, FP, and FN are as follow:

Given a fixed radius r, two binary images of prediction and annotation.

#### Modified True Positive: 
The set of white pixels in prediction, such that its nearest neighbor (can has distance 0) in annotation has distance SMALLER THAN (<) r.

#### Modified False Positive: 
The remaining white pixels in prediction excluding all True Positives.

#### Modified False Negative: 
The set of white pixels in annotation such that its NN in prediction is NO SMALLER THAN (>=) r.
