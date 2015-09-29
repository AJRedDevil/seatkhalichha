# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carpool_Requests'
        db.create_table(u'carpools_carpool_requests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carpoolreqref', self.gf('django.db.models.fields.CharField')(default='20c55dc769564491b97fa7f4e26baaeb', unique=True, max_length=100)),
            ('carpool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requests', to=orm['carpools.Carpools'])),
            ('rider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carpool_rider', to=orm['users.UserProfile'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('ishidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'carpools', ['Carpool_Requests'])


    def backwards(self, orm):
        # Deleting model 'Carpool_Requests'
        db.delete_table(u'carpools_carpool_requests')


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
            'carpoolreqref': ('django.db.models.fields.CharField', [], {'default': "'a1e4d15ed19d49899c5abe8398af3113'", 'unique': 'True', 'max_length': '100'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ishidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'rider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carpool_rider'", 'to': u"orm['users.UserProfile']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
        },
        u'carpools.carpools': {
            'Meta': {'object_name': 'Carpools'},
            'carpoolref': ('django.db.models.fields.CharField', [], {'default': "'9b8a7786a2ec4f5a91c95f7e7e65cc40'", 'unique': 'True', 'max_length': '100'}),
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
            'userref': ('django.db.models.fields.CharField', [], {'default': "'f71222edbef34254a13d1b74f6b862ee'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['carpools']