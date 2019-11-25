from typing import Any
from chroma_feedback import wording

API = None


def get_api() -> Any:
	global API

	if not API:
		API = api_factory()
	return API


def api_factory() -> Any:
	api = None

	try:
		from blinkstick import blinkstick
		from blinkstick.blinkstick import VENDOR_ID, PRODUCT_ID

		try:
			api = blinkstick
			api.find_all()
		except OSError:
			exit(wording.get('connection_no').format('AGILE INNOVATIVE BLINKSTICK') + wording.get('exclamation_mark'))
		return api
	except ImportError:
		exit(wording.get('package_no').format('BLINKSTICK') + wording.get('exclamation_mark'))
