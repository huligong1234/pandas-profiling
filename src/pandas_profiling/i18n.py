"""Configuration for the package is handled in this wrapper for confuse."""
import argparse
from pathlib import Path
from typing import Union

import confuse

from pandas_profiling.config import config
from pandas_profiling.utils.paths import get_i18n


class I18N:
    """This is a wrapper for the python confuse package, which handles setting and getting configuration variables via
    various ways (notably via argparse and kwargs).
    """

    i18n = None
    """The confuse.Configuration object."""

    def __init__(self):
        """The config constructor should be called only once."""
        if self.i18n is None:
            self.clear()
        else:
            self.set_file(str(get_i18n(config["i18n"])))

    def set_file(self, file_name: Union[str, Path]) -> None:
        """
        Set the i18n from a file

        Args:
            file_name: file name
        """
        if self.i18n is not None:
            self.i18n.set_file(str(file_name))

    def __getitem__(self, item):
        return self.i18n[item]

    def __setitem__(self, key, value):
        value = self._handle_shorthand(key, value)
        self.i18n[key].set(value)

    def clear(self):
        self.i18n = confuse.Configuration("PandasProfilingI18N", __name__, read=False)
        self.set_file(str(get_i18n(config["i18n"])))

    @property
    def is_default(self):
        default_i18n = I18N()
        return self == default_i18n


i18n = I18N()
