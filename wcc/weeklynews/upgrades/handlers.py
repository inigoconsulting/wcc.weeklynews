from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.weeklynews to 1001',
                description=u'Upgrade wcc.weeklynews to 1001',
                source='1', destination='1001',
                sortkey=1, profile='wcc.weeklynews:default')
def to1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.weeklynews.upgrades:to1001')
