# coding: utf-8

"""
Default configuration values for service gateway package.

Copy this file, rename it if you like, then edit to keep only the values you
need to override for the keys found within.

To have the programs in the package override the values with the values
found in this file, you need to set the environment variable named
"VRP_CONFIGURATION" to the path of your own copy before launching the program.
"""

CELERY = {
    'BROKER_URL': "amqp://amqp//",
    'CELERY_RESULT_BACKEND': "amqp://",
    'CELERY_TASK_SERIALIZER': "json",
    'CELERY_RESULT_SERIALIZER': "json",
    'CELERY_ACCEPT_CONTENT': ["json"],
    'CELERY_TASK_RESULT_EXPIRES': 7200}

WORKER_SERVICES = {
    'transcoder': {
        # Keyword used in the rest api to access this service
        # (ex.: http://server/<route_keyword>/info)
        # Set to '.' to access this service without keyword
        # (ex.: http://server/info)
        'route_keyword': 'transcoder',

        # The celery task name.
        # Must match the task in the worker app name : <proj_name>.<task_name>
        # (ex.: worker.my_service)
        'celery_task_name': 'transcoder',

        # The celery queue name.
        # Must match the queue name specified when starting the worker
        # (by the -Q switch)
        'celery_queue_name': 'transcoder',

        # Following parameters are required by the CANARIE API (info request)
        'name': 'My service',
        'synopsis': "RESTful service providing multimedia document "
                    "transcoding.",
        'version': "0.2.8",  # Expected version - will check.
        'institution': 'My Organisation',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'support@my-organisation.ca',
        'category': "Data Manipulation",
        'researchSubject': "My research subject",
        'tags': "my_service, research",

        # The following parameters are used to respond to some CANARIE API
        # request.
        #
        # They must be one of the following:
        #  - A valid URL to perform a redirection
        #  - A relative template file that will be used to generate the html
        #    page
        #    (relative to the templates directory)
        #  - A response string and the html status separated by a comma that
        #    will
        #    be used  to make a response to the requested element. Ex.: 'Not
        #    available,404'

        'home': "http://services.vesta.crim.ca/docs/mss/latest/"
                "user_guide.html#transcode",

        'doc': "http://services.vesta.crim.ca/docs/mss/latest/"
               "user_guide.html#transcode",
        'releasenotes': "http://services.vesta.crim.ca/docs/mss/latest/"
                        "user_guide.html#transcode",
        'support': "http://services.vesta.crim.ca/docs/mss/latest/"
                   "user_guide.html#transcode",

        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': ",204",
        'tryme': "http://services.vesta.crim.ca/docs/mss/latest/"
                 "user_guide.html#transcode",
        'licence': "http://services.vesta.crim.ca/docs/mss/latest/"
                   "user_guide.html#transcode",
        'provenance': "http://services.vesta.crim.ca/docs/mss/latest/"
                      "user_guide.html#transcode",
        'os_args': {'image':
                    'docker-registry.crim.ca/vesta/service-transcoding:0.2.8',
                    'instance_type': 'm1.large'},
        # Process-request to spawn VM ratio
        'rubber_params': {'spawn_ratio': 0.1}}
}

SECURITY = {"BYPASS_SECURITY": True}

MSS = {
    'SWIFT_AUTHENTIFICATION_OPTIONS': 'V1_LOCAL',
    'SWIFT_REDIRECT_URL': 'http://localhost:8080',
    'STORAGE_URL_IGNORE_PREFIX_FOR_TEMP_URL': 'swift',
    'SWIFT': {
        'os-auth-url': 'http://localhost:8080/auth/v1.0',
        'os-tenant-name': 'test',
        'os-username': 'tester',
        'os-password': 'crim1Log',
        },

    'STORAGE_SERVICE_CONTAINER': 'DockerMSSMultimedia',

    # Swift token renewal frequency (Twice a day)
    'TOKEN_RENEWAL_FREQ': 43200,

    # Temp url validity (One day)
    'TEMP_URL_DEFAULT_VALIDITY': 86400

    }
