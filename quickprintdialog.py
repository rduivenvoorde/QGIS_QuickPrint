# -*- coding: utf-8 -*-
"""
/***************************************************************************
 nmQuickPrintDialog
                                 A QGIS plugin
 Een snel printje maken
                             -------------------
        begin                : 2014-05-28
        copyright            : (C) 2017 by Marco Duiker (MD-kwadraat)
        email                : md@md-kwadraat.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

# create the di# this magic let compile Qt the ui files on the fly (if path known)
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui_quickprint.ui'))

class QuickPrintDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(QuickPrintDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
