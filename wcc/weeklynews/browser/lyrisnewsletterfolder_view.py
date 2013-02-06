from five import grok
from plone.directives import dexterity, form
from wcc.weeklynews.content.lyrisnewsletterfolder import ILyrisNewsletterFolder

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ILyrisNewsletterFolder)
    grok.require('zope2.View')
    grok.template('lyrisnewsletterfolder_view')
    grok.name('view')

    def newsletter_types(self):
        result = []
        for i in self.context.newsletter_types:
            key, title = [k.strip() for k in i.split('|')]
            result.append({'title': title, 'value': key})
        return result

class Subscribed(grok.View):
    grok.context(ILyrisNewsletterFolder)
    grok.require('zope2.View')
    grok.template('message')
    grok.name('subscribed')

    def message(self):
        return self.context.subscribed_message

class Unsubscribed(grok.View):
    grok.context(ILyrisNewsletterFolder)
    grok.require('zope2.View')
    grok.template('message')
    grok.name('unsubscribed')

    def message(self):
        return self.context.unsubscribed_message
