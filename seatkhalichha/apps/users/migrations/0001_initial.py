# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'users_userprofile', (
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userref', self.gf('django.db.models.fields.CharField')(default='9ebe40ecdda14d29bf44e81cfe8ee3b0', unique=True, max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('displayname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('phone_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone', self.gf('phonenumber_field.modelfields.PhoneNumberField')(unique=True, max_length=16)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('profile_image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=1024, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('address', self.gf('jsonfield.fields.JSONField')(default={'city': 'Kathmandu', 'streetaddress': 'Tripureshwore'}, max_length=9999, blank=True)),
            ('address_coordinates', self.gf('django.contrib.gis.db.models.fields.PointField')(default='', null=True, blank=True)),
            ('current_address', self.gf('django.contrib.gis.db.models.fields.PointField')(default='', null=True, blank=True)),
            ('extrainfo', self.gf('jsonfield.fields.JSONField')(default='{}', max_length=9999)),
        ))
        db.send_create_signal(u'users', ['UserProfile'])

        # Adding model 'UserEvents'
        db.create_table(u'users_userevents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile'])),
            ('event', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=2)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('extrainfo', self.gf('jsonfield.fields.JSONField')(default='{}', max_length=9999)),
        ))
        db.send_create_signal(u'users', ['UserEvents'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'users_userprofile')

        # Deleting model 'UserEvents'
        db.delete_table(u'users_userevents')


    models = {
        u'users.userevents': {
            'Meta': {'object_name': 'UserEvents'},
            'event': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '2'}),
            'extrainfo': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('jsonfield.fields.JSONField', [], {'default': "{'city': 'Kathmandu', 'streetaddress': 'Tripureshwore'}", 'max_length': '9999', 'blank': 'True'}),
            'address_coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'current_address': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'displayname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'extrainfo': ('jsonfield.fields.JSONField', [], {'default': "'{}'", 'max_length': '9999'}),
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
            'userref': ('django.db.models.fields.CharField', [], {'default': "'d6ba5dc4f0b04fb2b91aaf216ab9ac06'", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['users']