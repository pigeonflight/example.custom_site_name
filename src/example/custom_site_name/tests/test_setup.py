# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from example.custom_site_name.testing import EXAMPLE_CUSTOM_SITE_NAME_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that example.custom_site_name is properly installed."""

    layer = EXAMPLE_CUSTOM_SITE_NAME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if example.custom_site_name is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'example.custom_site_name'))

    def test_browserlayer(self):
        """Test that IExampleCustomSiteNameLayer is registered."""
        from example.custom_site_name.interfaces import (
            IExampleCustomSiteNameLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IExampleCustomSiteNameLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EXAMPLE_CUSTOM_SITE_NAME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['example.custom_site_name'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if example.custom_site_name is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'example.custom_site_name'))

    def test_browserlayer_removed(self):
        """Test that IExampleCustomSiteNameLayer is removed."""
        from example.custom_site_name.interfaces import \
            IExampleCustomSiteNameLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IExampleCustomSiteNameLayer,
            utils.registered_layers())
