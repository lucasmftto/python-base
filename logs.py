#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

import os
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()

logging ##root log

#nossa instancia
log = logging.Logger("logs.py", log_level)

### level
# ch = logging.StreamHandler() #Cosole/ terminal/ sdterr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meuLog.lod",
    maxBytes=700, #10**6, 
    backupCount=10
)
fh.setLevel(log_level)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino
# log.addHandler(ch)
log.addHandler(fh)

"""
log.debug("Log em DEBUGs tests")
log.info("Log INFOs tests")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro as fazer divisao: %s", str(e))