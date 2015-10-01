# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Carpools.tp_url'
        db.add_column(u'carpools_carpools', 'tp_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Carpools.tp_url'
        db.delete_column(u'carpools_carpools', 'tp_url')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'carpools.carpool_requests': {
            'Meta': {'object_name': 'Carpool_Requests'},
            'carpool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requests'", 'to': u"orm['carpools.Carpools']"}),
            'carpoolreqref': ('django.db.models.fields.CharField', [], {'default': "'34de2450d31d4e58ae01810ef92b1a27'", 'unique': 'True', 'max_length': '100'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ishidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'rider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carpool_rider'", 'to': u"orm['users.UserProfile']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
        },
        u'carpools.carpools': {
            'Meta': {'object_name': 'Carpools'},
            'carpoolref': ('django.db.models.fields.CharField', [], {'default': "'c3e99fcf8bd343158e17350edf8ad118'", 'unique': 'True', 'max_length': '100'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carpool_driver'", 'to': u"orm['users.UserProfile']"}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ishidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupancy': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '10'}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'route': ('django.db.models.fields.TextField', [], {}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'tp_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'vehicle_type': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('jsonfield.fields.JSONField', [], {'default': "{'city': 'Kathmandu', 'streetaddress': 'Tripureshwore'}", 'max_length': '9999', 'blank': 'True'}),
            'address_coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'current_address': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True'}),
            'extrainfo': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('phonenumber_field.modelfields.PhoneNumberField', [], {'unique': 'True', 'max_length': '16'}),
            'phone_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'userref': ('django.db.models.fields.CharField', [], {'default': "'3432cd347e504e6093cab26cf5a00a5c'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['carpools']