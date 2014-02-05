from __future__ import print_function
from random import shuffle
from copy import copy, deepcopy
from collections import namedtuple
import sys
import os

IMG_PATH = 'C:\\Users\\Joyce\\Dropbox\\Peynircioglu Lab\\Faces\\DISSERTATION & MATERIALS\\Experiments\\experiment\\face-composites'

files = {
    'young': ['Aligned_029_0_C1.jpg', 'Aligned_034_0_C1.jpg', 'Aligned_040_0_C1.jpg', 'Aligned_062_0_C1.jpg', 'Aligned_110_0_C1.jpg', 'Aligned_118_0_C1.jpg', 'Aligned_124_0_C1.jpg', 'Aligned_130_0_C1.jpg', 'Aligned_144_0_C1.jpg', 'Aligned_178_0_C1.jpg', 'Aligned_180_0_C1.jpg', 'Aligned_184_0_C1.jpg', 'Aligned_203_0_C1.jpg', 'Aligned_215_0_C1.jpg', 'Aligned_223_0_C1.jpg', 'Aligned_255_0_C1.jpg', 'Aligned_261_0_C1.jpg', 'Aligned_277_0_C1.jpg', 'Aligned_287_0_C1.jpg', 'Aligned_288_0_C1.jpg', 'Aligned_291_0_C1.jpg', 'Aligned_294_0_C1.jpg', 'Aligned_299_0_C1.jpg', 'Aligned_303_0_C1.jpg', 'Aligned_C2_006.jpg', 'Aligned_C2_007.jpg', 'Aligned_C2_009.jpg', 'Aligned_C2_021.jpg', 'Aligned_C2_024.jpg', 'Aligned_C2_025.jpg', 'Aligned_C2_028.jpg', 'Aligned_C2_030.jpg', 'Aligned_C2_032.jpg', 'Aligned_C2_033.jpg', 'Aligned_C2_037.jpg', 'Aligned_C2_039.jpg', 'Aligned_C2_042.jpg', 'Aligned_C2_050.jpg', 'Aligned_C2_054.jpg', 'Aligned_C2_059.jpg', 'Aligned_C2_060.jpg', 'Aligned_C2_071.jpg', 'Aligned_C2_072.jpg', 'Aligned_C2_085.jpg', 'Aligned_C2_088.jpg', 'Aligned_C2_089.jpg', 'Aligned_C2_094.jpg', 'Aligned_C2_097.jpg', 'Aligned_C2_098.jpg', 'Aligned_C2_104.jpg', 'Aligned_C2_117.jpg', 'Aligned_C2_131.jpg', 'Aligned_C2_132.jpg', 'Aligned_C2_135.jpg', 'Aligned_C2_137.jpg', 'Aligned_C2_142.jpg', 'Aligned_C2_143.jpg', 'Aligned_C2_152.jpg', 'Aligned_C2_153.jpg', 'Aligned_C2_160.jpg', 'Aligned_C2_167.jpg', 'Aligned_C2_168.jpg', 'Aligned_C2_181.jpg', 'Aligned_C2_182.jpg', 'Aligned_C2_185.jpg', 'Aligned_C2_201.jpg', 'Aligned_C2_210.jpg', 'Aligned_C2_214.jpg', 'Aligned_C2_216.jpg', 'Aligned_C2_217.jpg', 'Aligned_C2_219.jpg', 'Aligned_C2_234.jpg', 'Aligned_C2_235.jpg', 'Aligned_C2_242.jpg', 'Aligned_C2_244.jpg', 'Aligned_C2_246.jpg', 'Aligned_C2_254.jpg', 'Aligned_C2_256.jpg', 'Aligned_C2_265.jpg', 'Aligned_C2_286.jpg', 'Aligned_C2_290.jpg', 'Aligned_C2_296.jpg', 'Aligned_C2_300.jpg', 'Aligned_C2_301.jpg', 'Aligned_C2_304.jpg', 'Aligned_Cropped_10.jpg', 'Aligned_Cropped_12.jpg', 'Aligned_Cropped_64.jpg', 'Aligned_Cropped_69.jpg', 'Aligned_Cropped_72.jpg', 'Aligned_Cropped_76.jpg', 'Aligned_Cropped_77.jpg', 'Aligned_Cropped_8.jpg', 'Aligned_Cropped_New_1.jpg', 'Aligned_Cropped_New_10.jpg', 'Aligned_Cropped_New_11.jpg', 'Aligned_Cropped_New_12.jpg', 'Aligned_Cropped_New_13.jpg', 'Aligned_Cropped_New_14.jpg', 'Aligned_Cropped_New_15.jpg', 'Aligned_Cropped_New_16.jpg', 'Aligned_Cropped_New_17.jpg', 'Aligned_Cropped_New_18.jpg', 'Aligned_Cropped_New_20.jpg', 'Aligned_Cropped_New_21.jpg', 'Aligned_Cropped_New_22.jpg', 'Aligned_Cropped_New_23.jpg', 'Aligned_Cropped_New_5.jpg', 'Aligned_Cropped_New_7.jpg', 'Aligned_Cropped_New_8.jpg', 'Aligned_Cropped_New_9.jpg', 'Aligned_Exemplar_C2_008.jpg'],
    'older': ['005_o_f_n_a_aligned.jpg', '021_o_f_n_a_aligned.jpg', '030_o_f_n_a_aligned.jpg', '075_o_f_n_a_aligned.jpg', 'Older_101_01_aligned.jpg', 'Older_60to70_02_aligned.jpg', 'Older_60to70_04_aligned.jpg', 'Older_80to90_01_aligned.jpg', 'Older_80to90_03_aligned.jpg', 'neutral_o_f_10_aligned.jpg', 'neutral_o_f_11_aligned.jpg', 'neutral_o_f_12_aligned.jpg', 'neutral_o_f_13_aligned.jpg', 'neutral_o_f_14_aligned.jpg', 'neutral_o_f_15_aligned.jpg', 'neutral_o_f_16_aligned.jpg', 'neutral_o_f_17_aligned.jpg', 'neutral_o_f_18_aligned.jpg', 'neutral_o_f_19_aligned.jpg', 'neutral_o_f_1_aligned.jpg', 'neutral_o_f_20_aligned.jpg', 'neutral_o_f_21_aligned.jpg', 'neutral_o_f_22_aligned.jpg', 'neutral_o_f_23_aligned.jpg', 'neutral_o_f_24_aligned.jpg', 'neutral_o_f_25_aligned.jpg', 'neutral_o_f_26_aligned.jpg', 'neutral_o_f_27_aligned.jpg', 'neutral_o_f_28_aligned.jpg', 'neutral_o_f_29_aligned.jpg', 'neutral_o_f_2_aligned.jpg', 'neutral_o_f_30_aligned.jpg', 'neutral_o_f_31_aligned.jpg', 'neutral_o_f_32_aligned.jpg', 'neutral_o_f_33_aligned.jpg', 'neutral_o_f_34_aligned.jpg', 'neutral_o_f_35_aligned.jpg', 'neutral_o_f_36_aligned.jpg', 'neutral_o_f_37_aligned.jpg', 'neutral_o_f_38_aligned.jpg', 'neutral_o_f_39_aligned.jpg', 'neutral_o_f_40_aligned.jpg', 'neutral_o_f_4_aligned.jpg', 'neutral_o_f_5_aligned.jpg', 'neutral_o_f_6_aligned.jpg', 'neutral_o_f_7_aligned.jpg', 'neutral_o_f_8_aligned.jpg', 'neutral_o_f_9_aligned.jpg']
}

Stim = namedtuple('Stim', ['fan', 'age', 'eyes', 'face', 'test', 'test_eyes', 'id'])

def stimgen(dir='.'):
    if not os.path.exists(dir):
        os.makedirs(dir)

    master = deepcopy(files)

    shuffle(master['young'])
    shuffle(master['older'])

    lf_master = {
        'young': master['young'][0:24],
        'older': master['older'][0:24]
    }
    hf_master = {
        'young': master['young'][24:48],
        'older': master['older'][24:48]
    }

    stim_master = []
    matching = []

    # Low fan stim
    for age in ['young', 'older']:
        faces = lf_master[age]
        eyes = rotate(faces, 1)
        n = len(eyes)
        test_eyes = eyes[0:n/2] + rotate(eyes[n/2:], 1)
        test = repeat(['old', 'new'], n/2)
        zipped = zip(eyes, faces, test, test_eyes, xrange(len(stim_master), len(stim_master)+n))
        stim = [Stim('lf', age, *args) for args in zipped]
        stim_master += stim
        matching += zip(stim, stim)
        matching += zip(stim, rotate(stim, 3))

    # High fan stim
    for age in ['young', 'older']:
        eye_donors = hf_master[age][0:4]
        eyes = repeat(eye_donors, 6)
        n = len(eyes)
        faces = rotate(hf_master[age], 1)
        test = repeat(['old', 'new'], 3) * 4
        test_eyes = copy(eyes)
        for i in xrange(4):
            swapped_eyes = [eye_donors[j] for j in xrange(len(eye_donors)) if j != i]
            swapped_start = 6*i + 3
            test_eyes[swapped_start:swapped_start+3] = swapped_eyes
        zipped = zip(eyes, faces, test, test_eyes, xrange(len(stim_master), len(stim_master)+n))
        stim = [Stim('hf', age, *args) for args in zipped]
        stim_master += stim
        matching += zip(stim, stim)
        matching += zip(stim, flatten([rotate(x) for x in group(stim, 6)]))

    master_file = open(dir + '/master.csv', 'w')
    print_stim(None, master_file)
    for stim in stim_master:
        print_stim(stim, master_file)
    master_file.close()

    study = copy(stim_master)
    shuffle(study)
    study_file = open(dir + '/master-study.csv', 'w')
    study_img_file = open(dir + '/study-img.txt', 'w')
    study_trigger_file = open(dir + '/study-trigger.txt', 'w')
    print_stim(None, study_file)
    for stim in study:
        print_stim(stim, study_file)
        print(img_path(stim), file=study_img_file)
        print(stim_trigger(stim, False), file=study_trigger_file)
    study_file.close()
    study_img_file.close()
    study_trigger_file.close()

    shuffle(matching)
    matching_file = open(dir + '/master-matching.csv', 'w')
    left_img_file = open(dir + '/matching-img-left.txt', 'w')
    right_img_file = open(dir + '/matching-img-right.txt', 'w')
    matching_trigger_file = open(dir + '/matching-trigger.txt', 'w')
    print('match', 'stim_id_left', 'stim_id_right', 'age_left', 'age_right', 'trigger', sep=',', file=matching_file)
    for pair in matching:
        trigger = stim_trigger(pair[0], pair[0] != pair[1])
        print(pair[0] == pair[1], pair[0].id, pair[1].id, pair[0].age, pair[1].age, trigger, sep=',', file=matching_file)
        print(img_path(pair[0]), file=left_img_file)
        print(img_path(pair[1]), file=right_img_file)
        print(trigger, file=matching_trigger_file)
    matching_file.close()
    left_img_file.close()
    right_img_file.close()
    matching_trigger_file.close()

    test = copy(stim_master)
    shuffle(test)
    test_file = open(dir + '/master-test.csv', 'w')
    test_img_file = open(dir + '/test-img.txt', 'w')
    test_trigger_file = open(dir + '/test-trigger.txt', 'w')
    print_stim(None, test_file)
    for stim in test:
        print_stim(stim, test_file)
        print(img_path(stim, test=True), file=test_img_file)
        print(stim_trigger(stim, stim.test == 'new'), file=test_trigger_file)
    test_file.close()
    test_img_file.close()
    test_trigger_file.close()

def rotate(list, n=1):
    return list[n:] + list[0:n]

def repeat(list, n=2):
    return flatten([[x]*n for x in list])

def flatten(list):
    return reduce(lambda x,y: x+y, list, [])

def group(list, n):
    return [list[start:start+n] for start in xrange(0, len(list), n)]

def print_stim(stim, file):
    if stim:
        study_trigger = stim_trigger(stim, False)
        test_trigger = stim_trigger(stim, stim.test == 'new')
        print(stim.id, stim.fan, stim.age, stim.face, stim.eyes, stim.test_eyes, stim.test, study_trigger, test_trigger, sep=',', file=file)
    else:
        print('stim_id', 'fan', 'age', 'face', 'eyes', 'test_eyes', 'test', 'study_trigger', 'test_trigger', sep=',', file=file)

def stim_trigger(stim, test_condition):
    trigger = 1 # always need at least one bit set to mark the event.
    trigger |= 2 if stim.fan == 'hf' else 0
    trigger |= 4 if stim.age == 'older' else 0
    trigger |= 8 if test_condition else 0
    return trigger

def img_path(stim, test=False):
    eyes = stim.test_eyes if test else stim.eyes
    return '%s\\%s+%s+EyeMask2.jpg' % (IMG_PATH, eyes, stim.face)
