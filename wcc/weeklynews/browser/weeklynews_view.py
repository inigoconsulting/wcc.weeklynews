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
        end = self.context.endDate.date()
        increment = timedelta(days=1)

        result = self.catalog.searchResults({
                'portal_type': 'wcc.prayercycle.prayercycle',
                'sort_on': 'start'
                })

        for idx, brain in enumerate(result):
            start = self.context.startDate.date()
            while start <= end:
                if brain.start.date() <= start <= brain.end.date():
                    return [result[idx], result[idx + 1]]
                start += increment

#        upper = {'query': end + extra2, 'range': 'min'}
#        lower = {'query': start - extra2, 'range': 'max'}
#        first = self.catalog.searchResults({
#                'portal_type': 'wcc.prayercycle.prayercycle',
#                'start': date_range_query,
#                })
#        second = self.catalog.searchResults({
#                'portal_type': 'wcc.prayercycle.prayercycle',
#                'end': date_range_query,
#                })
#
#        third = self.catalog.searchResults({
#                'portal_type': 'wcc.prayercycle.prayercycle',
#                'end': upper,
#                'start': lower,
#                })
#
#
#        result = list(set(first + second))

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
        return "%s - %s" % (start, end)

    def prayerdate(self, prayerobject):
        start = prayerobject.startDate.strftime("%d %b")
        end = prayerobject.endDate.strftime("%d %b %y")
        return "%s - %s" % (start, end)
