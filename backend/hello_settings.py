import os, json

# are we local?
LOCAL = os.environ.get('LOCAL')
DEBUG = LOCAL

# project path
# TODO: fix this so that it is the same for local and prod
if LOCAL:
    PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
else:
    PROJECT_PATH = '/srv/hello_webapp'
BACKEND_PATH = os.path.join(PROJECT_PATH, 'backend')
print 'PROJECT_PATH: {}'.format(PROJECT_PATH)
print 'BACKEND_PATH: {}'.format(BACKEND_PATH)

# secrets dict
SECRETS_PATH = os.path.join(BACKEND_PATH, 'devops/secret_files/secret.json')
SECRETS_DICT = json.loads(open(SECRETS_PATH, "r").read())


# temporary settings below


# configure database url dynamically
def get_db_url():
    return SECRETS_DICT['TEST_DB_CONNECTION']
