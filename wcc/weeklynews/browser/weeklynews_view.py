from five import grok
from plone.directives import dexterity, form
from wcc.weeklynews.content.weeklynews import IWeeklyNews

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IWeeklyNews)
    grok.require('zope2.View')
    grok.template('weeklynews_view')
    grok.name('view')

