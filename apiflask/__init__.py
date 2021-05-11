# flake8: noqa
# temp fix for https://github.com/django/asgiref/issues/143
import sys
if sys.platform == 'win32' and (3, 8, 0) <= sys.version_info < (3, 9, 0):  # pragma: no cover
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # pragma: no cover

from marshmallow import pre_load as before_load
from marshmallow import post_load as after_load
from marshmallow import pre_dump as before_dump
from marshmallow import post_dump as after_dump
from marshmallow import validates as validate
from marshmallow import validates_schema as validate_schema
from marshmallow import ValidationError

from . import fields
from . import validators
from .app import APIFlask
from .blueprint import APIBlueprint
from .decorators import auth_required
from .decorators import doc
from .decorators import input
from .decorators import output
from .exceptions import abort
from .exceptions import HTTPError
from .schemas import Schema
from .schemas import PaginationSchema
from .security import HTTPBasicAuth
from .security import HTTPTokenAuth
from .utils import get_reason_phrase
from .utils import pagination_builder

__version__ = '0.6.0dev'
