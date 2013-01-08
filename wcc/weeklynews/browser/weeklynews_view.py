from five import grok
from plone.directives import dexterity, form
from wcc.weeklynews.content.weeklynews import IWeeklyNews
from Products.CMFCore.utils import getToolByName
from dateutil.parser import parse
from datetime import timedelta

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
        start = self.context.startDate.date()
        end = self.context.endDate.date()
        date_range_query = {'query': (start, end), 'range': 'min:max'}
        return self.catalog.searchResults({
                'portal_type': 'News Item',
                'Date': date_range_query,
                'sort_on': 'Date'
                })

    @property
    def allevents(self):
        extra = timedelta(days=1)
        end = self.context.endDate.date() + extra
        date_range_query = {'query': end, 'range': 'min'}
        return  self.catalog.searchResults({
                'portal_type': 'Event',
                'start': date_range_query,
                'sort_on': 'start'
                })


    @property
    def allprayer(self):
        extra = timedelta(weeks=1)
        start = self.context.startDate.date()
        end = self.context.endDate.date() + extra
        date_range_query = {'query': (start, end), 'range': 'min: max'}
        return  self.catalog.searchResults({
                'portal_type': 'wcc.prayercycle.prayercycle',
                'start': date_range_query,
                'sort_on': 'start'
                })

    @property
    def newvideo(self):
        return self.catalog.searchResults({
                'portal_type': 'RTInternalVideo',
                'sort_on': 'created'
                })[-1]

    def convert_date(self, value):
        return parse(value).strftime("%d %B %Y")

    def date_title(self):
        start = self.context.startDate.strftime("%d %b %y")
        end = self.context.endDate.strftime("%d %b %y")
        return "<span> %s - %s </span>" % (start, end)

    def prayerdate(self, prayerobject):
        start = prayerobject.startDate.strftime("%d %b")
        end = prayerobject.endDate.strftime("%d %b %y")
        return "<span> %s - %s </span>" % (start, end)
