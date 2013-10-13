from __future__ import print_function
from random import shuffle
from copy import copy
from collections import namedtuple
import sys

IMG_PATH = '/experiment/face-composites'

files = ['Aligned_029_0_C1.jpg', 'Aligned_034_0_C1.jpg', 'Aligned_040_0_C1.jpg', 'Aligned_062_0_C1.jpg', 'Aligned_110_0_C1.jpg', 'Aligned_118_0_C1.jpg', 'Aligned_124_0_C1.jpg', 'Aligned_130_0_C1.jpg', 'Aligned_144_0_C1.jpg', 'Aligned_178_0_C1.jpg', 'Aligned_180_0_C1.jpg', 'Aligned_184_0_C1.jpg', 'Aligned_203_0_C1.jpg', 'Aligned_215_0_C1.jpg', 'Aligned_223_0_C1.jpg', 'Aligned_255_0_C1.jpg', 'Aligned_261_0_C1.jpg', 'Aligned_277_0_C1.jpg', 'Aligned_287_0_C1.jpg', 'Aligned_288_0_C1.jpg', 'Aligned_291_0_C1.jpg', 'Aligned_294_0_C1.jpg', 'Aligned_299_0_C1.jpg', 'Aligned_303_0_C1.jpg', 'Aligned_C2_006.jpg', 'Aligned_C2_007.jpg', 'Aligned_C2_009.jpg', 'Aligned_C2_021.jpg', 'Aligned_C2_024.jpg', 'Aligned_C2_025.jpg', 'Aligned_C2_028.jpg', 'Aligned_C2_030.jpg', 'Aligned_C2_032.jpg', 'Aligned_C2_033.jpg', 'Aligned_C2_037.jpg', 'Aligned_C2_039.jpg', 'Aligned_C2_042.jpg', 'Aligned_C2_050.jpg', 'Aligned_C2_054.jpg', 'Aligned_C2_059.jpg', 'Aligned_C2_060.jpg', 'Aligned_C2_071.jpg', 'Aligned_C2_072.jpg', 'Aligned_C2_085.jpg', 'Aligned_C2_088.jpg', 'Aligned_C2_089.jpg', 'Aligned_C2_094.jpg', 'Aligned_C2_097.jpg', 'Aligned_C2_098.jpg', 'Aligned_C2_104.jpg', 'Aligned_C2_117.jpg', 'Aligned_C2_131.jpg', 'Aligned_C2_132.jpg', 'Aligned_C2_135.jpg', 'Aligned_C2_137.jpg', 'Aligned_C2_142.jpg', 'Aligned_C2_143.jpg', 'Aligned_C2_152.jpg', 'Aligned_C2_153.jpg', 'Aligned_C2_160.jpg', 'Aligned_C2_167.jpg', 'Aligned_C2_168.jpg', 'Aligned_C2_181.jpg', 'Aligned_C2_182.jpg', 'Aligned_C2_185.jpg', 'Aligned_C2_201.jpg', 'Aligned_C2_210.jpg', 'Aligned_C2_214.jpg', 'Aligned_C2_216.jpg', 'Aligned_C2_217.jpg', 'Aligned_C2_219.jpg', 'Aligned_C2_234.jpg', 'Aligned_C2_235.jpg', 'Aligned_C2_242.jpg', 'Aligned_C2_244.jpg', 'Aligned_C2_246.jpg', 'Aligned_C2_254.jpg', 'Aligned_C2_256.jpg', 'Aligned_C2_265.jpg', 'Aligned_C2_286.jpg', 'Aligned_C2_290.jpg', 'Aligned_C2_296.jpg', 'Aligned_C2_300.jpg', 'Aligned_C2_301.jpg', 'Aligned_C2_304.jpg', 'Aligned_Cropped_10.jpg', 'Aligned_Cropped_12.jpg', 'Aligned_Cropped_64.jpg', 'Aligned_Cropped_69.jpg', 'Aligned_Cropped_72.jpg', 'Aligned_Cropped_76.jpg', 'Aligned_Cropped_77.jpg', 'Aligned_Cropped_8.jpg', 'Aligned_Cropped_New_1.jpg', 'Aligned_Cropped_New_10.jpg', 'Aligned_Cropped_New_11.jpg', 'Aligned_Cropped_New_12.jpg', 'Aligned_Cropped_New_13.jpg', 'Aligned_Cropped_New_14.jpg', 'Aligned_Cropped_New_15.jpg', 'Aligned_Cropped_New_16.jpg', 'Aligned_Cropped_New_17.jpg', 'Aligned_Cropped_New_18.jpg', 'Aligned_Cropped_New_20.jpg', 'Aligned_Cropped_New_21.jpg', 'Aligned_Cropped_New_22.jpg', 'Aligned_Cropped_New_23.jpg', 'Aligned_Cropped_New_5.jpg', 'Aligned_Cropped_New_7.jpg', 'Aligned_Cropped_New_8.jpg', 'Aligned_Cropped_New_9.jpg', 'Aligned_Exemplar_C2_008.jpg']

occupations = {
    'hs': ['doctor', 'lawyer', 'professor', 'CEO'],
    'ls': ['maid', 'nanny', 'bus driver', 'secretary']
}

Stim = namedtuple('Stim', ['fan', 'status', 'occupation', 'eyes', 'face', 'test', 'test_eyes'])

def stimgen(dir='.'):
    master = copy(files)
    if len(master) != 112:
        raise 'master list does not have 112-items'

    shuffle(master)

    lf_master = {
        'hs': master[0:8],
        'ls': master[8:16]
    }
    hf_master = {
        'hs': master[16:64],
        'ls': master[64:112]
    }

    lf_stim = {}
    hf_stim = {}

    for status in ['hs', 'ls']:
        eyes = lf_master[status]
        faces = rotate(lf_master[status], 2)
        test = ['old', 'new'] * 4
        test_eyes = repeat(rotate(lf_master[status][0::2], 1), 2)
        zipped = zip(repeat(occupations[status], 2), eyes, faces, test, test_eyes)
        lf_stim[status] = [Stim('lf', status, *args) for args in zipped]

    for status in ['hs', 'ls']:
        eye_donors = hf_master[status][0:8]
        eyes = repeat(eye_donors, 6)
        faces = rotate(hf_master[status], 1)
        test = repeat(['old', 'new'], 3) * 8
        test_eyes = repeat(flatten([[x,y] for x,y in zip(eye_donors, rotate(eye_donors, 4))]), 3)
        zipped = zip(repeat(occupations[status], 6) * 2, eyes, faces, test, test_eyes)
        hf_stim[status] = [Stim('hf', status, *args) for args in zipped]

    stim_master = lf_stim['hs'] + lf_stim['ls'] + hf_stim['hs'] + hf_stim['ls']
    master_file = open(dir + '/master.csv', 'w')
    print_stim(None, master_file)
    for stim in stim_master:
        print_stim(stim, master_file)
    master_file.close()

    study = copy(stim_master)
    shuffle(study)
    study_file = open(dir + '/master-study.csv', 'w')
    study_img_file = open(dir + '/study-img.txt', 'w')
    study_occupation_file = open(dir + '/study-occupation.txt', 'w')
    print_stim(None, study_file)
    for stim in study:
        print_stim(stim, study_file)
        print(img_path(stim), file=study_img_file)
        print(stim.occupation, file=study_occupation_file)
    study_file.close()
    study_img_file.close()
    study_occupation_file.close()

def rotate(list, n=1):
    return list[n:] + list[0:n]

def repeat(list, n=2):
    return flatten([[x]*n for x in list])

def flatten(list):
    return reduce(lambda x,y: x+y, list, [])

def print_stim(stim, file):
    if stim:
        print(stim.fan, stim.status, stim.occupation, stim.eyes, stim.face, stim.test, stim.test_eyes, sep=',', file=file)
    else:
        print('fan', 'status', 'occupation', 'eyes', 'face', 'test', 'test_eyes', sep=',', file=file)

def img_path(stim):
    return '%s/%s+%s+EyeMask2.jpg' % (IMG_PATH, stim.eyes, stim.face)
