import os
from os import listdir
from os.path import isfile, join
import nibabel as nib
from skimage import feature

loading_path_imgs = '/path/to/dhcp_neonatal_scans_directory'
saving_path = '/path/to/output_directory_for_lbp_maps'
onlyfiles = [f for f in listdir(loading_path_imgs) if isfile(join(loading_path_imgs,f))]
for x in onlyfiles:
    full_filename = os.path.join(loading_path_imgs, x)
    print('reading:', full_filename)
    img = nib.load(full_filename)
    img_data = img.get_fdata()
    i, j, k = img_data.shape 
    img_data_lbp = img_data
    for kk in range(i):
        img_data_lbp[kk] = feature.local_binary_pattern(img_data[kk], 8, 1, method='uniform')
    new_header = img.header.copy()
    new_img = nib.nifti1.Nifti1Image(img_data_lbp, None, header=new_header)
    nib.save(new_img, join(saving_path, x))
