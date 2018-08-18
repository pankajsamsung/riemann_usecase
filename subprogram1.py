from random import random
import structlog

def random_log():
    log = structlog.getLogger(__name__)
    if random() > 0.7   :
        log.error("Fatal error")
    else:
        log.info("I'm fine")