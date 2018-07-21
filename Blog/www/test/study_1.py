"""practise logging

practise using logging in *.py.

Variables:
    if __name__ {[type]} -- [description]
"""

import logging
import logging.config

config = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'short': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'short',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'plugins': {
            'handlers': ['console'],
            'level': 'INFO',
            'progagate': False
        },
    },
}

logging.config.dictConfig(config)


def do_magic(param):
    pass


def sample_function(secret_parameter):
    logger = logging.getLogger(__name__)  # __name__=projectA.moduleB
    logger.debug("Going to perform magic with '%s'", secret_parameter)
    try:
        result = do_magic(secret_parameter)
        raise IndexError
    except IndexError:
        logger.exception("OMG it happened again, someone please tell Laszlo")
    except Exception:
        logger.info("Unexpected exception", exc_info=True)
        raise
    else:
        logger.info(
            "Magic with '%s' resulted in '%s'",
            secret_parameter,
            result,
            stack_info=True)


def main():
    """[summary]

    [description]
    """
    sample_function("hello")


if __name__ == '__main__':
    # import sys
    # sys.path.append("../")
    main()
