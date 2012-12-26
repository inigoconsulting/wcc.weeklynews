from five import grok
from plone.directives import dexterity, form
from wcc.weeklynews.content.weeklynews import IWeeklyNews
from Products.CMFCore.utils import getToolByName
from dateutil.parser import parse

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IWeeklyNews)
    grok.require('zope2.View')
    grok.template('weeklynews_view')
    grok.name('view')


    def update(self):
        self.catalog = getToolByName(self.context, 'portal_catalog')

    @property
    def allnews(self):
        return self.catalog.searchResults(portal_type='News Item')

    def convertdate(self, value):
        return parse(value).strftime("%d, %B %Y")
