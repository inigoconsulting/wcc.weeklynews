from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.weeklynews import MessageFactory as _


# Interface class; used to define content-type schema.

class ILyrisNewsletterFolder(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    mlid = schema.TextLine(title=_(u'Lyris Mailing list ID'))
    siteid = schema.TextLine(title=_(u'Lyris Site ID'))
    newsletter_types = schema.List(
            title=_(u'Newsletter types'), required=False,
            description=_(u'Available newsletter types. 1 each line using the '
                'format <i>type_idenfitier|title</i>'),
            value_type=schema.TextLine(), default=[])

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


