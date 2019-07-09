import requests
from .normalize import normalize_data

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--jenkins-host', required = True)
		program.add_argument('--jenkins-slug', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run():
	host = args.jenkins_host
	slugs = args.jenkins_slug
	result = []

	for slug in slugs:
		result.extend(fetch(host, slug))
	return result


def fetch(host, slug):
	response = None

	if host and slug:
		response = requests.get(host + '/job/' + slug + '/api/json')

	# process response

	if response and response.status_code == 200:
		data = response.json()

		if data:
			return normalize_data(data)
	return []