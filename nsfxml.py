import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import os
import zipfile
import pandas as pd

import zipfile

dir_name = '//Users/Aerdaxie/Dropbox/Job/Data incubator/DI2017/nsfgrant'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file

all_file = os.listdir(dir_name)



def xml_single (xml_data):
    tree = ET.ElementTree(file = xml_data)
    tree_list = tree.findall('.//') # element tree
    record = {}
    for i in range(len(tree_list)):
        child_tree = tree_list [i]
        if (child_tree.tag == 'AbstractNarration')|(child_tree.tag == 'LongName')|(child_tree.tag == 'Award'): continue
        if (child_tree.tag == 'Directorate')|(child_tree.tag == 'Division'):
                   record.update ({child_tree.tag + '_Name'  :lst[i+1].text  } )

        else:
            record.update ({child_tree.tag : child_tree.text})

    return record

def xml2df(file_list):
    all_record = []
    for file_name in file_list:
        single_record = xml_single (file_name)
        all_record.append (single_record)
        nsf_grant = pd.DataFrame.from_dict (all_record)
    return nsf_grant

dir_test = '//Users/Aerdaxie/Dropbox/Job/Data incubator/DI2017/nsftest'
test_file = os.listdir(dir_test)
os.chdir(dir_test)
len (test_file)

import random
file_ind = random.sample(range(0,(len(test_file)-1)), 1000)
test_list=[]
for i in file_ind:
    test_list.append(test_file[i])

nsf_test = xml2df(test_list)

nsf_test.set_index('AwardID',inplace = True)

nsf_test.to_csv(os.path.join(dir_test, 'nsf_test.csv'))
