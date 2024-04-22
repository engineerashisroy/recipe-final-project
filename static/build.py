import shutil
import os

if not os.path.exists('static'):
    os.makedirs('static')

shutil.copytree('templates', 'static/templates')
shutil.copy('Cleaned_Indian_Food_Dataset.csv', 'static/')
shutil.copy('model_cbow.model', 'static/')
