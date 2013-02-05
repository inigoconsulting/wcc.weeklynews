from five import grok
from plone.directives import dexterity, form
from wcc.weeklynews.content.lyrisnewsletterfolder import ILyrisNewsletterFolder

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ILyrisNewsletterFolder)
    grok.require('zope2.View')
    grok.template('lyrisnewsletterfolder_view')
    grok.name('view')

