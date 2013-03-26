from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.weeklynews to 1004',
                description=u'Upgrade wcc.weeklynews to 1004',
                source='1003', destination='1004',
                sortkey=1, profile='wcc.weeklynews:default')
def to1004(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.weeklynews.upgrades:to1004')


@gs.upgradestep(title=u'Upgrade wcc.weeklynews to 1003',
                description=u'Upgrade wcc.weeklynews to 1003',
                source='1002', destination='1003',
                sortkey=1, profile='wcc.weeklynews:default')
def to1003(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.weeklynews.upgrades:to1003')


@gs.upgradestep(title=u'Upgrade wcc.weeklynews to 1002',
                description=u'Upgrade wcc.weeklynews to 1002',
                source='1001', destination='1002',
                sortkey=1, profile='wcc.weeklynews:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.weeklynews.upgrades:to1002')


@gs.upgradestep(title=u'Upgrade wcc.weeklynews to 1001',
                description=u'Upgrade wcc.weeklynews to 1001',
                source='1', destination='1001',
                sortkey=1, profile='wcc.weeklynews:default')
def to1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.weeklynews.upgrades:to1001')
