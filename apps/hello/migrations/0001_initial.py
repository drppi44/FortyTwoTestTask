# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration, DataMigration
from django.db import models

db.delete_table(u'south_migrationhistory')
db.delete_table(u'hello_userprofile')
db.delete_table(u'hello_modelsignal')
db.delete_table(u'hello_myhttprequest')
db.delete_table(u'django_content_type')
