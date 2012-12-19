from collective.grok import gs
from wcc.weeklynews import MessageFactory as _

@gs.importstep(
    name=u'wcc.weeklynews', 
    title=_('wcc.weeklynews import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.weeklynews.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
