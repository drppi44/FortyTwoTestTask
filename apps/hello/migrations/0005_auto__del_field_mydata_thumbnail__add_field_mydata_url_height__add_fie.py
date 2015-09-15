# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MyData.thumbnail'
        db.delete_column(u'hello_mydata', 'thumbnail')

        # Adding field 'MyData.url_height'
        db.add_column(u'hello_mydata', 'url_height',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=200),
                      keep_default=False)

        # Adding field 'MyData.url_width'
        db.add_column(u'hello_mydata', 'url_width',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MyData.thumbnail'
        db.add_column(u'hello_mydata', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'MyData.url_height'
        db.delete_column(u'hello_mydata', 'url_height')

        # Deleting field 'MyData.url_width'
        db.delete_column(u'hello_mydata', 'url_width')


    models = {
        u'hello.mydata': {
            'Meta': {'object_name': 'MyData'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '200'}),
            'url_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '200'})
        }
    }

    complete_apps = ['hello']