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
        y = self.catalog.searchResults(portal_type='News Item')
        return [x for x in y if self.date_range(x.getObject())]

    @property
    def allevents(self):
        y = self.catalog.searchResults(portal_type='Event')
        end = self.context.endDate.date()
        return [x for x in y if self.get_date(x.getObject()) > end]

    @property
    def allprayer(self):
        y = self.catalog.searchResults(
                portal_type='wcc.prayercycle.prayercycle')
        end = self.context.endDate.date()
        return [x for x in y if self.get_date(x.getObject())]

    def convert_date(self, value):
        return parse(value).strftime("%d %B %Y")

    def get_date(self, data):
        return parse(data.Date()).date()

    def date_title(self):
        start = self.context.startDate.strftime("%d %b %y")
        end = self.context.endDate.strftime("%d %b %y")
        return "<span> %s - %s </span>" % (start, end)

    def prayerdate(self, prayerobject):
        start = prayerobject.startDate.strftime("%d %b")
        end = prayerobject.endDate.strftime("%d %b %y")
        return "<span> %s - %s </span>" % (start, end)


    def date_range(self, data):
        objectdate = self.get_date(data)
        start = self.context.startDate.date()
        end = self.context.endDate.date()
        return start <= objectdate <= end
