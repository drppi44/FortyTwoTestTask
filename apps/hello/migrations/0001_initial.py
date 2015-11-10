# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def __new__(cls, *args, **kwargs):
        from django.core.management import call_command
        call_command('flush', interactive=False, load_initial_data=False)
        return super(cls, Migration).__new__()

    def forwards(self, orm):
        # Adding model 'UserProfile'

        db.create_table(u'hello_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('avatar', self.gf('django_resized.forms.ResizedImageField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'hello', ['UserProfile'])

        # Adding model 'ModelSignal'
        db.create_table(u'hello_modelsignal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['ModelSignal'])

        # Adding model 'MyHttpRequest'
        db.create_table(u'hello_myhttprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('query_string', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('is_viewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'hello', ['MyHttpRequest'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'hello_userprofile')

        # Deleting model 'ModelSignal'
        db.delete_table(u'hello_modelsignal')

        # Deleting model 'MyHttpRequest'
        db.delete_table(u'hello_myhttprequest')


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
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
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