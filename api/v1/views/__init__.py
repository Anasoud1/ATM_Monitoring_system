#!/usr/bin/python3
from flask import Blueprint


app_views = Blueprint("app_views", __name__,  url_prefix= "/api/v1")


from api.v1.views.regions import *
from api.v1.views.branches import *
from api.v1.views.groups import *
from api.v1.views.devices import *
from api.v1.views.atms import *
from api.v1.views.electronic_journals import *
from api.v1.views.events import *
from api.v1.views.transactions import *
from api.v1.views.atmDevice import *
from api.v1.views.groups_atms import *
