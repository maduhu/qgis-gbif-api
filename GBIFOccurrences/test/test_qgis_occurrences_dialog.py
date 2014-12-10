# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'n.noe@biodiversity.be'
__date__ = '2014-11-18'
__copyright__ = 'Copyright 2014, Nicolas Noé - Belgian Biodiversity Platform'

import unittest


from PyQt4 import QtCore, QtTest

from qgis.core import QgsMapLayerRegistry

from qgis_occurrences_dialog import GBIFOccurrencesDialog

from utilities import get_qgis_app

from httmock import HTTMock
from gbif_mock import gbif_v1_response

QGIS_APP = get_qgis_app()


class GBIFOccurrencesDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.dialog = GBIFOccurrencesDialog(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_basic_tetraodon(self):
        """ Ensure we have a new layer with 51 features when searching for T. fluviatilis."""

        with HTTMock(gbif_v1_response):
            existing_layers = QgsMapLayerRegistry().instance().mapLayers().values()

            self.dialog.scientific_name.setText("Tetraodon fluviatilis")
            QtTest.QTest.mouseClick(self.dialog.loadButton, QtCore.Qt.LeftButton)

            timeout = 20
            count = 0
            while count < timeout:
                QtTest.QTest.qWait(1000)

                if len(QgsMapLayerRegistry().instance().mapLayers()) + 1 == len(existing_layers):
                    # A new layer has been created
                    break
                count += 1

            # everything went OK, get the new layer
            current_layers = QgsMapLayerRegistry().instance().mapLayers().values()
            new_layer = list(set(current_layers).difference(set(existing_layers)))[0]
            
            # We should have 51 feature on this layer
            self.assertEqual(new_layer.featureCount(), 51)

    def test_return_shortcut(self):
        """Ensure the return key also work to launch search."""
        pass

    def test_basisofrecord_filter(self):
        pass

    def test_country_filter(self):
        pass

    def test_layer_name(self):
        pass

    def test_always_have_coordinates(self):
        """Ensure we only ask GBIF records with coordinates."""
        pass

    def test_coordinates(self):
        """Ensure the POINTS are respecting lat/long from returned data"""
        pass

    def test_attributes_creation(self):
        """Ensure we have an attribute created for each field returned in data"""
        pass

    def test_attributes_content(self):
        """Ensure the correct values are set in feature attributes (or null)"""




if __name__ == "__main__":
    suite = unittest.makeSuite(GBIFOccurrencesDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
