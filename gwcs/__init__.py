# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This is an Astropy affiliated package.
"""

from __future__ import absolute_import, division, unicode_literals, print_function


# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

from .wcs import *
#from .coordinate_systems import *
from . import selector

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    #from example_mod import *
    pass

