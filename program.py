import logging.config

import time
import sys

from structlog import configure, processors, stdlib, threadlocal

import subprogram1
import subprogram2

#config from: https://blog.sneawo.com/blog/2017/07/28/json-logging-in-python/
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'format': '%(message)s %(lineno)d %(pathname)s',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        }
    },
    'handlers': {
        'json': {
            'class': 'utils.kafka_logging.KafkaHandler',
            'formatter': 'json'
        }
    },
    'loggers': {
        '': {
            'handlers': ['json'],
            'level': logging.DEBUG
        }
    }
})

configure(
    context_class=threadlocal.wrap_dict(dict),
    logger_factory=stdlib.LoggerFactory(),
    wrapper_class=stdlib.BoundLogger,
    processors=[
        stdlib.filter_by_level,
        stdlib.add_logger_name,
        stdlib.add_log_level,
        stdlib.PositionalArgumentsFormatter(),
        processors.TimeStamper(fmt="iso"),
        processors.StackInfoRenderer(),
        processors.format_exc_info,
        processors.UnicodeDecoder(),
        stdlib.render_to_log_kwargs]
)


while True:
    print("Logging loop start")
    sys.stdout.flush()
    subprogram1.random_log()
    subprogram2.random_log()
    print("Logging loop end")
    sys.stdout.flush()
    time.sleep(0.01)