# Copyright 2023, tfuxu <https://github.com/tfuxu>
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk, Adw

from pixely.constants import rootdir


@Gtk.Template(resource_path=f"{rootdir}/ui/report_page.ui")
class PixelyReportPage(Gtk.Box):
    __gtype_name__ = "PixelyReportPage"

    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)

        self.parent = parent
        self.settings = parent.settings

        self.app = self.parent.get_application()
        self.win = self.app.get_active_window()

        self.setup_signals()
        self.setup()

    def setup_signals(self):
        pass

    def setup(self):
        pass
