# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MyData.url_height'
        db.delete_column(u'hello_mydata', 'url_height')

        # Deleting field 'MyData.url_width'
        db.delete_column(u'hello_mydata', 'url_width')


        # Changing field 'MyData.avatar'
        db.alter_column(u'hello_mydata', 'avatar', self.gf(u'sorl.thumbnail.fields.ImageField')(max_length=255))

    def backwards(self, orm):
        # Adding field 'MyData.url_height'
        db.add_column(u'hello_mydata', 'url_height',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=200),
                      keep_default=False)

        # Adding field 'MyData.url_width'
        db.add_column(u'hello_mydata', 'url_width',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=200),
                      keep_default=False)


        # Changing field 'MyData.avatar'
        db.alter_column(u'hello_mydata', 'avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=255))

    models = {
        u'hello.mydata': {
            'Meta': {'object_name': 'MyData'},
            'avatar': (u'sorl.thumbnail.fields.ImageField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']