# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carpools'
        db.create_table(u'carpools_carpools', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carpoolref', self.gf('django.db.models.fields.CharField')(default='d8fc86bf5b70468b844be1d961d049c9', unique=True, max_length=100)),
            ('driver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carpool_driver', to=orm['users.UserProfile'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('vehicle_type', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('occupancy', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=10)),
            ('ishidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('remarks', self.gf('django.db.models.fields.TextField')()),
            ('route', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'carpools', ['Carpools'])


    def backwards(self, orm):
        # Deleting model 'Carpools'
        db.delete_table(u'carpools_carpools')


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
        u'carpools.carpools': {
            'Meta': {'object_name': 'Carpools'},
            'carpoolref': ('django.db.models.fields.CharField', [], {'default': "'70463c93de8e4806a273a778191619f7'", 'unique': 'True', 'max_length': '100'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carpool_driver'", 'to': u"orm['users.UserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ishidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupancy': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '10'}),
            'remarks': ('django.db.models.fields.TextField', [], {}),
            'route': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
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
            'displayname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '254'}),
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
            'userref': ('django.db.models.fields.CharField', [], {'default': "'973deed215be40f0a8e3c00f7097cb68'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['carpools']