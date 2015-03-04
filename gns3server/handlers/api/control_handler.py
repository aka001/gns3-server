# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ...web.route import Route
from ...config import Config
from aiohttp.web import HTTPForbidden

import asyncio


class ControlHandler:

    @classmethod
    @Route.post(
        r"/control/shutdown",
        description="Shutdown the remote server",
        status_codes={
            201: "Shutdown started",
            403: "Shutdown refused"
        })
    def shutdown(request, response):

        if Config.instance().get_section_config("Server").getboolean("local", False) is False:
            raise HTTPForbidden(text="You can only shutdown the local server")
        response.set_status(201)
        asyncio.get_event_loop().stop()
