from flask import Flask
import os

app=Flask(__name__,template_folder=r'D:\major_project\megha\website\templates',static_folder=r'D:\major_project\megha\website\static')
app.config['SECRET_KEY']='123456'




from website.views import views 
app.register_blueprint(views)

UPLOADER_PATH='website/static/temp_images'

if not  os.path.exists(UPLOADER_PATH):
    os.makedirs(UPLOADER_PATH)
    print('Path created')
else:
    print('Already exits')
    

app.config['UPLOADER_FOLDER']=UPLOADER_PATH
