"""
    test_repair_phone_number.py -- given a phone number, attempt to improve it

    Version 0.1 MC 2013-12-21
    --  Initial version.
    Version 0.2 MC 2015-01-29
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2015, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.2"

from vivopeople import repair_phone_number
from datetime import datetime

print datetime.now(), "Start"
befores = [
    "27737",
    "2-7737",
    "352 484 2999",
    "377 9999",
    "3-4882 X 9943",
    "+1 352 388 2888",
    "888388",
    "272 2822 ext. 2999",
    "bd282"
    ]
for before in befores:
    print "Before",before.ljust(20), "After", \
        repair_phone_number(before).ljust(20)
print datetime.now(), "Finish"

