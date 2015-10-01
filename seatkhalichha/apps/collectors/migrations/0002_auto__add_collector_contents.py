# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collector_Contents'
        db.create_table(u'collectors_collector_contents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collectors.Collectors'])),
            ('identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=254)),
            ('content', self.gf('jsonfield.fields.JSONField')()),
        ))
        db.send_create_signal(u'collectors', ['Collector_Contents'])


    def backwards(self, orm):
        # Deleting model 'Collector_Contents'
        db.delete_table(u'collectors_collector_contents')


    models = {
        u'collectors.collector_contents': {
            'Meta': {'object_name': 'Collector_Contents'},
            'content': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collectors.Collectors']"})
        },
        u'collectors.collectors': {
            'Meta': {'object_name': 'Collectors'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sourceref': ('django.db.models.fields.CharField', [], {'default': "'ef603a1af90d4cb19d27f944dc8d90c2'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['collectors']