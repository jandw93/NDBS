# Network Device Backup Solution
#
# Copyright 2016 DNA SERVICES B.V.
# Written by Jan de Witte
#
# NDBS 16 Version 0

# Indexes:

# Customer ID: check module connections
# Device ID: check module connections
# Type ID: check module commandos
# Backup location ID: check module ftpsettings
# Job ID: define as the fifth value in bck(x,x,x,x,x)

from main import *

bck(0,0,0,0,'Job #0001')
