from flask import request
from .utils import *
from .modules import app

@app.route("/", methods=['GET'])
def homepage():
    return 'Welcome to the Challenge 2'

@app.route("/solution", methods=['POST'])
def solution():
    content = request.get_json()
    output_name = "result_img"
    # Get image frames of the intervall [depth_min, depth_max]
    df, error_list = filter_image('public/img.csv', content["depth_min"], content["depth_max"])
    # resize the image width to 150 instead of 200
    resized_imgObj = resize_image(df)  # imageobject
    # Store the image in the database sqlite3 (In module Images)
    path_image_resized= save_image(resized_imgObj)
    #Apply a custom color map to the generated frames and save the image colored in the database (Images table)
    color_map(path_image_resized, output_name)
    imageobj = Images.query.filter_by(name=output_name).first()
    return {output_name: imageobj.pathfile}

if __name__ == "__main__":
    app.run(debug=True)
