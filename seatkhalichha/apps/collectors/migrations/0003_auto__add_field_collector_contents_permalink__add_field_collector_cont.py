# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Collector_Contents.permalink'
        db.add_column(u'collectors_collector_contents', 'permalink',
                      self.gf('django.db.models.fields.URLField')(default='', unique=True, max_length=200),
                      keep_default=False)

        # Adding field 'Collector_Contents.shortlink'
        db.add_column(u'collectors_collector_contents', 'shortlink',
                      self.gf('django.db.models.fields.URLField')(default='', unique=True, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Collector_Contents.permalink'
        db.delete_column(u'collectors_collector_contents', 'permalink')

        # Deleting field 'Collector_Contents.shortlink'
        db.delete_column(u'collectors_collector_contents', 'shortlink')


    models = {
        u'collectors.collector_contents': {
            'Meta': {'object_name': 'Collector_Contents'},
            'content': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'}),
            'permalink': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'shortlink': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collectors.Collectors']"})
        },
        u'collectors.collectors': {
            'Meta': {'object_name': 'Collectors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sourceref': ('django.db.models.fields.CharField', [], {'default': "'e55dbd590ae540b98e14ef60a7ee9ee1'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['collectors']