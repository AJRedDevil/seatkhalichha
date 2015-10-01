# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collectors'
        db.create_table(u'collectors_collectors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sourceref', self.gf('django.db.models.fields.CharField')(default='83cf135005d34888b73340182fac9112', unique=True, max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'collectors', ['Collectors'])


    def backwards(self, orm):
        # Deleting model 'Collectors'
        db.delete_table(u'collectors_collectors')


    models = {
        u'collectors.collectors': {
            'Meta': {'object_name': 'Collectors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sourceref': ('django.db.models.fields.CharField', [], {'default': "'b132ef3cc24745089cabe86de39babeb'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['collectors']