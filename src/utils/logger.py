import os
import logging
import logging.config
import colorlog
from tools.ansi_configs import colors as COLORS

log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_format = (
    '%(levelname_log_color)s%(levelname)s%(reset)s : '
    '%(asctime_log_color)s%(asctime)s%(reset)s - '
    '%(name_log_color)s%(name)s%(reset)s : '
    '%(message_log_color)s%(message)s%(reset)s'
)

class CustomColoredFormatter(colorlog.ColoredFormatter):
    def format(self, record):
        record.levelname_log_color = COLORS.get(record.levelname, '\033[0m')  # Default to no color
        record.asctime_log_color = '\033[34m'
        record.name_log_color = '\033[36m'
        record.message_log_color = '\033[37m'
        record.reset = '\033[0m'
        return super(CustomColoredFormatter, self).format(record)

log_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(levelname)s : %(asctime)s - %(name)s : %(message)s',
        },
        'colored': {
            '()': CustomColoredFormatter,
            'format': log_format,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
        },
        'file_general': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_directory, 'app.log'),
            'formatter': 'standard',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_directory, 'error.log'),
            'formatter': 'standard',
        },
    },
    'loggers': {
        'QWENZIE': {
            'handlers': ['console', 'file_general', 'file_error'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'prisma': {
            'handlers': ['console', 'file_general', 'file_error'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}


logging.config.dictConfig(log_config)


def get_logger(name: str):
    return logging.getLogger(name)

logger = get_logger("QWENZIE")
