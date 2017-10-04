"""
Updated values for ServiceGateway in Vesta context.
"""

SECURITY = {"BYPASS_SECURITY": True}

CELERY = {
    'BROKER_URL': "amqp://amqp",
    "CELERY_RESULT_BACKEND": "amqp",
    'CELERY_TASK_SERIALIZER': "json",
    'CELERY_RESULT_SERIALIZER': "json",
    'CELERY_ACCEPT_CONTENT': ["json"]}

# DATABASES = {
#     'Invocations': {
#         'filename': "/mnt/volume/service_invocations.db",
#         'schema_filename':
#             "/usr/lib/python2.7/site-packages/"
#             "ServiceGateway/static/"
#             "service_invocations_schema.sql"
#         },
#     'Requests': {
#         'filename': "/mnt/volume/requests.db",
#         'schema_filename':
#             "/usr/lib/python2.7/site-packages/"
#             "ServiceGateway/static/"
#             "requests_schema.sql"
#         }
#     }

CELERY_PROJ_NAME = "worker"

WORKER_SERVICES = {
    'stub': {
        # Keyword used in the rest api to access this service
        # (ex.: http://server/<route_keyword>/info)
        # Set to '.' to access this service without keyword
        # (ex.: http://server/info)
        'route_keyword': 'stub',

        # The celery task name.
        # Must match the task in the worker app name : <proj_name>.<task_name>
        # (ex.: diarisation)
        'celery_task_name': 'stub',

        # The celery queue name.
        # Must match the queue name specified when starting the worker
        # (by the -Q switch)
        'celery_queue_name': 'stub',

        # Following parameters are required by the CANARIE API (info request)
        'name': 'Stub service',
        'synopsis': "RESTful service providing service stub.",
        'version': "0.2.0",  # Expected version - will check!
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'info-cra@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "system integration",
        'tags': "stub",

        # The following parameters are used to respond to some CANARIE API
        # request.
        #
        # They must be one of the following:
        #  - A valid URL to perform a redirection
        #  - A relative template file that will be used to generate the HTML
        #    page (relative to the templates directory)
        #  - A response string and the html status separated by a comma that
        #    will be used  to make a response to the requested element. Ex.:
        #    'Not available,404'

        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",

        'noparams': False,

        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image':
                    'docker-registry.crim.ca/vesta/service-stub:latest',
                    'instance_type': 'm1.tiny'},
        'rubber_params': {'spawn_ratio': 0.01}
    },
}
