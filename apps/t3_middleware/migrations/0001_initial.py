# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyHttpRequest'
        db.create_table(u't3_middleware_myhttprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('query_string', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('is_viewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u't3_middleware', ['MyHttpRequest'])


    def backwards(self, orm):
        # Deleting model 'MyHttpRequest'
        db.delete_table(u't3_middleware_myhttprequest')


    models = {
        u't3_middleware.myhttprequest': {
            'Meta': {'object_name': 'MyHttpRequest'},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['t3_middleware']