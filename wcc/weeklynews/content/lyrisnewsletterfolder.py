from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid, Interface

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.z3cform.datagridfield import DictRow
from wcc.weeklynews import MessageFactory as _
from plone.multilingualbehavior import directives as pam


# Interface class; used to define content-type schema.

class INewsletterTypeSchema(Interface):
    identifier = schema.TextLine(title=_(u'Identifier'))
    label = schema.TextLine(title=_(u'Title'))

class ILyrisNewsletterFolder(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    pam.languageindependent('mlid')
    mlid = schema.TextLine(title=_(u'Lyris Mailing list ID'))
    
    pam.languageindependent('siteid')
    siteid = schema.TextLine(title=_(u'Lyris Site ID'))

    form.widget(newsletter_types='collective.z3cform.datagridfield.DataGridFieldFactory')

    pam.languageindependent('newsletter_types')
    newsletter_types = schema.List(
            title=_(u'Newsletter types'), required=False,
            description=_(u'Available newsletter types'),
            value_type=DictRow(schema=INewsletterTypeSchema), default=[])

    form.widget(subscribed_message="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    subscribed_message = schema.Text(
        title=_(u'Message to new subscribers'),
        description=_(u'Text to display to new subscribers')
    )

    form.widget(unsubscribed_message="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    unsubscribed_message = schema.Text(
        title=_(u'Message to unsubscribed user'),
        description=_(u'Text to display to user who just unsubscribed')
    )


