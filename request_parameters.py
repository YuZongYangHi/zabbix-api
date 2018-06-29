#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
This is zabbix api parame json requests param
'''

GetHostTo_id = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "filter": {
            "host": [
            ]
        }
    },
    "id": 1
}

GetHostGroups = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
            ]
        }
    },
    "id": 1
}

GetHostTemplates =  {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectParentTemplates": [
            "templateid",
            "name"
        ],
        "hostids": []
    },
    "id": 1,
}

Group ={
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
            ]
        }
    },
    "id": 1
}

Template = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
            ]
        }
    },
    "id": 1
}

add = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        #"host": "",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                #"ip": "192.168.3.1",
                "dns": "",
                #"port": "10050"
            }
        ],
        "groups": [
        ],
        "templates": [
        ],

    },
    "id": 1
}

update = {
    "jsonrpc": "2.0",
    "method": "host.update",
    "params": {
        "hostid": [],
    },
    "id": 1
}

delete = {
    "jsonrpc": "2.0",
    "method": "host.delete",
    "params": [],
    "id": 1
}
get_items = {
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "search": {
        },
        "sortfield": "name"
    },
    "id": 1
}

set_items = {
    "jsonrpc": "2.0",
    "method": "item.update",
    "params": {
    },
    "id": 1
}

graph_get = {
    "jsonrpc": "2.0",
    "method": "graph.get",
    "params": {
        "output": "extend",
        "hostids":[],
        "sortfield": "name"
    },
    "id": 1
}


screen_add = {
    "jsonrpc": "2.0",
    "method": "screen.create",
    "params": {
        "hsize": 2,
        "vsize": 20,
        "screenitems": [
        ]
    },
    "id": 1
}
