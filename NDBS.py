# Network Device Backup Solution
#
# Copyright 2016 DNA SERVICES B.V.
# Written by Jan de Witte
#
# NDBS Version 0.0

# Indexen:

# Klant ID: check module connections
# Device ID: check module connections
# Type ID: check module commandos
# Backup location ID: check module ftpsettings
# Job ID: define as the fifth value in bck.runbck(x,x,x,x,x)

import makesshcon as bck

bck.runbck(0,0,0,0,1)
