#  IRIS Source Code
#  Copyright (C) 2023 - DFIR-IRIS
#  contact@dfir-iris.org
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from unittest import TestCase
from iris import Iris


class TestsRestSeverities(TestCase):

    def setUp(self) -> None:
        self._subject = Iris()

    def test_get_severities_should_return_canonical_order(self):
        response = self._subject.get('/api/v2/manage/severities')
        self.assertEqual(200, response.status_code)
        self.assertEqual(['Unspecified', 'Informational', 'Low', 'Medium', 'High', 'Critical'],
                         [row['severity_name'] for row in response.json()['data']])
