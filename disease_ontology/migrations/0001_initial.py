# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Term'
        db.create_table(u'disease_ontology_term', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doid', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('definition', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_obsolete', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'disease_ontology', ['Term'])

        # Adding model 'CrossReference'
        db.create_table(u'disease_ontology_crossreference', (
            ('ref', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128, primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(default='NA', max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(default='0000', max_length=60)),
        ))
        db.send_create_signal(u'disease_ontology', ['CrossReference'])

        # Adding M2M table for field term on 'CrossReference'
        m2m_table_name = db.shorten_name(u'disease_ontology_crossreference_term')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crossreference', models.ForeignKey(orm[u'disease_ontology.crossreference'], null=False)),
            ('term', models.ForeignKey(orm[u'disease_ontology.term'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crossreference_id', 'term_id'])

        # Adding model 'Synonym'
        db.create_table(u'disease_ontology_synonym', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('scope', self.gf('django.db.models.fields.CharField')(default='EXACT', max_length=10)),
        ))
        db.send_create_signal(u'disease_ontology', ['Synonym'])

        # Adding M2M table for field term on 'Synonym'
        m2m_table_name = db.shorten_name(u'disease_ontology_synonym_term')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('synonym', models.ForeignKey(orm[u'disease_ontology.synonym'], null=False)),
            ('term', models.ForeignKey(orm[u'disease_ontology.term'], null=False))
        ))
        db.create_unique(m2m_table_name, ['synonym_id', 'term_id'])

        # Adding M2M table for field cross_reference on 'Synonym'
        m2m_table_name = db.shorten_name(u'disease_ontology_synonym_cross_reference')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('synonym', models.ForeignKey(orm[u'disease_ontology.synonym'], null=False)),
            ('crossreference', models.ForeignKey(orm[u'disease_ontology.crossreference'], null=False))
        ))
        db.create_unique(m2m_table_name, ['synonym_id', 'crossreference_id'])

        # Adding model 'TermRelationship'
        db.create_table(u'disease_ontology_termrelationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Term_child', to=orm['disease_ontology.Term'])),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Term_parent', to=orm['disease_ontology.Term'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'disease_ontology', ['TermRelationship'])


    def backwards(self, orm):
        # Deleting model 'Term'
        db.delete_table(u'disease_ontology_term')

        # Deleting model 'CrossReference'
        db.delete_table(u'disease_ontology_crossreference')

        # Removing M2M table for field term on 'CrossReference'
        db.delete_table(db.shorten_name(u'disease_ontology_crossreference_term'))

        # Deleting model 'Synonym'
        db.delete_table(u'disease_ontology_synonym')

        # Removing M2M table for field term on 'Synonym'
        db.delete_table(db.shorten_name(u'disease_ontology_synonym_term'))

        # Removing M2M table for field cross_reference on 'Synonym'
        db.delete_table(db.shorten_name(u'disease_ontology_synonym_cross_reference'))

        # Deleting model 'TermRelationship'
        db.delete_table(u'disease_ontology_termrelationship')


    models = {
        u'disease_ontology.crossreference': {
            'Meta': {'object_name': 'CrossReference'},
            'domain': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '60'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'0000'", 'max_length': '60'}),
            'ref': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['disease_ontology.Term']", 'null': 'True', 'blank': 'True'})
        },
        u'disease_ontology.synonym': {
            'Meta': {'object_name': 'Synonym'},
            'cross_reference': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['disease_ontology.CrossReference']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'scope': ('django.db.models.fields.CharField', [], {'default': "'EXACT'", 'max_length': '10'}),
            'term': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['disease_ontology.Term']", 'symmetrical': 'False'})
        },
        u'disease_ontology.term': {
            'Meta': {'object_name': 'Term'},
            'children': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'_parents'", 'to': u"orm['disease_ontology.Term']", 'through': u"orm['disease_ontology.TermRelationship']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'definition': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'doid': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_obsolete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'disease_ontology.termrelationship': {
            'Meta': {'object_name': 'TermRelationship'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Term_parent'", 'to': u"orm['disease_ontology.Term']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Term_child'", 'to': u"orm['disease_ontology.Term']"})
        }
    }

    complete_apps = ['disease_ontology']