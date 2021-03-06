# Copyright (c) 2014 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from flask.ext import gravatar as gravatar_ext


INFINITY_HTML = '&#x221E;'

gravatar = gravatar_ext.Gravatar(None, size=64, rating='g', default='wavatar')


def format_datetime(timestamp):
    return datetime.datetime.utcfromtimestamp(
        timestamp).strftime('%d %b %Y %H:%M:%S')


def format_date(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%d-%b-%y')
