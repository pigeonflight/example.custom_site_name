# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import example.custom_site_name


class ExampleCustomSiteNameLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=example.custom_site_name)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.custom_site_name:default')


EXAMPLE_CUSTOM_SITE_NAME_FIXTURE = ExampleCustomSiteNameLayer()


EXAMPLE_CUSTOM_SITE_NAME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_CUSTOM_SITE_NAME_FIXTURE,),
    name='ExampleCustomSiteNameLayer:IntegrationTesting',
)


EXAMPLE_CUSTOM_SITE_NAME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_CUSTOM_SITE_NAME_FIXTURE,),
    name='ExampleCustomSiteNameLayer:FunctionalTesting',
)


EXAMPLE_CUSTOM_SITE_NAME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_CUSTOM_SITE_NAME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ExampleCustomSiteNameLayer:AcceptanceTesting',
)
