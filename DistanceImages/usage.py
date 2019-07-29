import distance_image
import os

gt_folder = 'data/DM++/test_label'
prop_folder = 'data/DM++/binarized_by_hard_th0.5'
save_folder = 'data/DM++/dist_pred2gt'


files = os.listdir(gt_folder)


for f in files:
    gt_path = os.path.join(gt_folder, f)
    prop_path = os.path.join(prop_folder, f)
    print(f)
    

    img = distance_image.get_distance_image(prop_path, gt_path)
    img.save(os.path.join(save_folder, f))
