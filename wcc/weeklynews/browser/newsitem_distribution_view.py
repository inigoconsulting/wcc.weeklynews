from five import grok
from Products.ATContentTypes.interfaces.news import IATNewsItem
grok.templatedir('templates')

class NewsItemDistributionView(grok.View):
    grok.name('distribution_view')
    grok.template('newsitem_distribution_view')
    grok.context(IATNewsItem)

    def newsletter(self):
        return None
