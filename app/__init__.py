from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
UPLOAD_FOLDER =  "/media/kanishk/8E8481E28481CCE1/Learn/repos/SAAS/oth/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

from app import routes