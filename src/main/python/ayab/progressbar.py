# -*- coding: utf-8 -*-
# This file is part of AYAB.
#
#    AYAB is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AYAB is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AYAB.  If not, see <http://www.gnu.org/licenses/>.
#
#    Copyright 2014 Sebastian Oliva, Christian Obersteiner,
#       Andreas Müller, Christian Gerbrandt
#    https://github.com/AllYarnsAreBeautiful/ayab-desktop

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ayab import GuiMain
    from .engine.status import ColorSymbolType


class ProgressBar(object):
    """Methods for the progress bar."""

    def __init__(self, parent: GuiMain):
        self.__row_label = parent.ui.label_current_row
        self.__color_label = parent.ui.label_current_color
        self.__status_label = parent.engine.status.ui.label_progress
        self.reset()

    def reset(self) -> None:
        self.row = -1
        self.total = -1
        self.repeats = -1
        self.color = ""
        self.__row_label.setText("")
        self.__color_label.setText("")
        self.__status_label.setText("")

    def update(
        self,
        row: int,
        total: int = 0,
        repeats: int = 0,
        color_symbol: ColorSymbolType = "",
    ) -> bool:
        if row < 0:
            return False
        self.row = row
        self.total = total
        self.repeats = repeats
        self.color = color_symbol
        self.refresh()
        return True

    def refresh(self) -> None:
        """Updates the color and row in progress bar"""
        if self.row < 0 or self.total < 0:
            return

        if self.color == "":
            color_text = ""
        else:
            color_text = "Color " + self.color
        self.__color_label.setText(color_text)

        # Update labels
        if self.total == 0:
            row_text = ""
        else:
            row_text = f"Row {self.row}/{self.total}"
            if self.repeats >= 0:
                row_text += f" ({self.repeats} repeats completed)"
        self.__row_label.setText(row_text)
        self.__status_label.setText(f"{self.row}/{self.total}")
