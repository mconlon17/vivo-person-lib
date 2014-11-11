"""
    test_get_degree.py -- Given a URI of a degree, return a python structure
    representing the attributes of the degree

    Version 0.1 MC 2013-12-30
    --  Initial version.
    Version 0.2 MC 2014-09-19
    --  Updated for tools 2.0, PEP 8
    
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivopeople import get_degree
from datetime import datetime

print datetime.now(), "Start"
degrees = \
    [
        "http://vivo.ufl.edu/individual/n195825",
        "http://vivo.ufl.edu/individual/n31642",
        "http://vivo.ufl.edu/individual/n142859",
        "http://vivo.ufl.edu/individual/n45279",
        "http://vivo.ufl.edu/individual/n111394",
        "http://vivo.ufl.edu/individual/n203974",
        "http://vivo.ufl.edu/individual/n101776",
        "http://vivo.ufl.edu/individual/n66611",
        "http://vivo.ufl.edu/individual/n489587",
        "http://vivo.ufl.edu/individual/n56190",
    ]
for degree in degrees:
    print "\n", get_degree(degree)
print datetime.now(), "Finish"
