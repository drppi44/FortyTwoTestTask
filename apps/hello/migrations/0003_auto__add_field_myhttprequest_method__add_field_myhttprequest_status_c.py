# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MyHttpRequest.method'
        db.add_column(u'hello_myhttprequest', 'method',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'MyHttpRequest.status_code'
        db.add_column(u'hello_myhttprequest', 'status_code',
                      self.gf('django.db.models.fields.IntegerField')(default='200', max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MyHttpRequest.method'
        db.delete_column(u'hello_myhttprequest', 'method')

        # Deleting field 'MyHttpRequest.status_code'
        db.delete_column(u'hello_myhttprequest', 'status_code')


    models = {
        u'hello.modelsignal': {
            'Meta': {'object_name': 'ModelSignal'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'hello.myhttprequest': {
            'Meta': {'ordering': "['-priority', '-time']", 'object_name': 'MyHttpRequest'},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'default': "'200'", 'max_length': '3'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'hello.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django_resized.forms.ResizedImageField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
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