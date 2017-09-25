# -*- coding: utf-8 -*-
"""
Configuration values for worker processes.
"""

# Broker settings ------------------------------------------------------------
BROKER_URL = 'amqp://amqp'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Result backend settings ----------------------------------------------------
CELERY_RESULT_BACKEND = "amqp"
CELERY_RESULT_SERIALIZER = 'json'

# Worker settings ------------------------------------------------------------
CELERYD_PREFETCH_MULTIPLIER = 1

# Logging settings -----------------------------------------------------------
CELERYD_TASK_LOG_FORMAT = ("[%(asctime)s: %(levelname)s/%(processName)s] "
                           "[%(task_name)s(%(task_id)s)] - %(name)s - "
                           "%(message)s")

CELERYD_LOG_FORMAT = ("[%(asctime)s: %(levelname)s/%(processName)s] "
                      "- %(name)s - %(message)s")
