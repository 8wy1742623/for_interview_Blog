import logging
import logging.config
import logging.handlers

# logging config


def init_logging(log_file_name):
    """Init for logging
    """
    config = {
        'disable_existing_loggers': False,
        'version': 1,
        'formatters': {
            'short': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s %(levelname)s %(name)s: %(message)s',
                'datefmt': '%H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'formatter': 'short',
                'class': 'logging.StreamHandler',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': log_file_name,
                'mode': 'w',
                'formatter': 'short',
            }
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                # 'level': 'ERROR',
                'level': 'DEBUG',
            },
            'plugins': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
    }
    logging.config.dictConfig(config)
    logger = logging.getLogger('')
    return logger


# logging
logger = init_logging(
    'D:/ch_download/skill_doc/data/dailyRecord/2018/for_interview'
    + '/for_interview_Blog/Blog/www/test/proj.log'
)

if __name__ == '__main__':
    logger.info('hello')
