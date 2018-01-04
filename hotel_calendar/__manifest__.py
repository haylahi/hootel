# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Solucións Aloxa S.L. <info@aloxa.eu>
#                       Alexandre Díaz <dev@redneboa.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Hotel Calendar',
    'version': '1.0',
    'author': "Alexandre Díaz (Aloxa Solucións S.L.) <alex@aloxa.eu>",
    'website': 'https://www.eiqui.com',
    'category': 'eiqui/hotel',
    'summary': "Hotel Calendar",
    'description': "Hotel Calendar",
    'depends': [
        'bus',
        'web',
        'hotel',
        'web_widget_color',
    ],
    'external_dependencies': {
        'python': []
    },
    'data': [
        'views/general.xml',
        'views/actions.xml',
        'views/res_config_views.xml',
        'views/inherited_res_users_views.xml',
        'views/virtual_room_pricelist_cached_views.xml',
        'data/views.xml',
        'data/menus.xml',
	    'security/ir.model.access.csv',
        'data/records.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'test': [
    ],

    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
