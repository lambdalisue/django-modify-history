# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2010/11/11
#
class HistoryError(Exception):
    """A generic exception for all others to extend."""
    pass
class AlreadyRegistered(HistoryError):
    """Raised when a model is already registered with a site."""
    pass

class NotRegistered(HistoryError):
    """Raised when a model is not registered with a site."""
    pass