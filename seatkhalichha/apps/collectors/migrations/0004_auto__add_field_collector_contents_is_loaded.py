# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Collector_Contents.is_loaded'
        db.add_column(u'collectors_collector_contents', 'is_loaded',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Collector_Contents.is_loaded'
        db.delete_column(u'collectors_collector_contents', 'is_loaded')


    models = {
        u'collectors.collector_contents': {
            'Meta': {'object_name': 'Collector_Contents'},
            'content': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'}),
            'is_loaded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permalink': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'shortlink': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collectors.Collectors']"})
        },
        u'collectors.collectors': {
            'Meta': {'object_name': 'Collectors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sourceref': ('django.db.models.fields.CharField', [], {'default': "'bf8013ac47e241b5ac3cd9c04de16f7d'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['collectors']