import image_metrics
import os
import sys

# You can change it to,
# gt_folder = sys.argv[1]
# prop_folder = sys.argv[2]
# ground truth folder first!
gt_folder = 'data/DM++/test_label'
prop_folder = 'data/DM++/binarized_by_hard_th0.5'

files = os.listdir(gt_folder)

sTP, sFP, sFN = 0, 0, 0
msTP, msFP, msFN = 0, 0, 0

for f in files:
    gt_path = os.path.join(gt_folder, f)
    prop_path = os.path.join(prop_folder, f)

    print(f)

    # normal precision & recall with threshold = 0.4*255.
    TP, FP, FN = image_metrics.get_TP_FP_FN(gt_path, prop_path, threshold=0.4*255)
    sTP += TP
    sFP += FP
    sFN += FN

    # r = 3, threshold = 0.4 * 255.
    mTP, mFP, mFN = image_metrics.get_mod_TP_FP_FN(gt_path, prop_path, radius=3, threshold=0.4*255)
    msTP += mTP
    msFP += mFP
    msFN += mFN


Precision = sTP / (sTP + sFP)
Recall = sTP / (sTP + sFN)
print(Precision, Recall)

mPrecision = msTP / (msTP + msFP)
mRecall = msTP / (msTP + msFN)
print(mPrecision, mRecall)