import os
import cv2
import cmapy
import numpy as np
import pandas as pd
from PIL import Image
from .modules import db, Images

def filter_image(img_dataset, depth_min, depth_max):
    df=None
    error_list = []
    try:
        df = pd.read_csv(img_dataset)
    except Exception as err:
        error_list.append(err)
    #Delete Nan rows
    df = df[df['depth'].notna()].drop(labels=0, axis=0)
    #Select data according to depth_min and depth_max
    df=df.loc[(df['depth'] <= depth_max)&(df['depth'] >= depth_min)]
    return df, error_list

def resize_image(df):
    imgObj = Image.fromarray(np.asarray(df))  # convert df to Image object
    resized_imgObj = imgObj.resize((150, len(df)))  # resize Image object
    return resized_imgObj

def save_db(output_name, output_path, type):
    project_root = os.path.dirname(os.path.realpath(__file__))
    pathfile = project_root+'/'+output_path
    newFile = Images(name=output_name, pathfile=pathfile, type_image=type)
    if Images.query.filter_by(name=output_name).first() is None:
        db.session.add(newFile)
        db.session.commit()

def save_image(resized_imgObj):
    type = "png"
    output_name= "resized_img"
    output_path = "public/{0}.{1}".format(output_name, type)
    resized_imgObj.convert('RGB').save(output_path, format="png")
    save_db(output_name, output_path, type)
    return output_path

def color_map(path_image_resized, output_name):
    type = "png"
    output_path = "public/{0}.{1}".format(output_name, type)
    img = cv2.imread(path_image_resized)
    img_colorized = cv2.applyColorMap(img, cmapy.cmap('viridis'))
    Image.fromarray(img_colorized).save(output_path, format="png")
    save_db(output_name, output_path, type)