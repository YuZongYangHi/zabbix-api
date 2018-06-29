#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests 
import json 
from   hosts import gettoken
import config  as config 
import parameter as params
import sys,os
import config as self

header = {
    "Content-Type": "application/json"
}

@gettoken
def groups_name(id):
    data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {},
    "auth": id,
    "id": 1
    }

    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(data),headers=header).text)
    data_list = []
    for i in  html['result']:
        temp = {}
        temp['id'] = i['groupid'] 
        temp['name'] = i['name']
        data_list.append(temp)
    return data_list

@gettoken 
def templates_name(id):
    data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {},
    "auth": id,
    "id": 1
    }
    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(data),headers=header).text)
    data_list = []
    for i in  html['result']:
        temp = {}
        temp['id'] = i['templateid'] 
        temp['name'] = i['name']
        data_list.append(temp)
    return data_list

@gettoken
def create_hosts(id,hostname,ip,groups,templates):
    params.add['params']['groups'] = []
    params.add['params']['templates'] = []
    params.add['auth'] = id 
    params.add['params']['host'] = hostname
    params.add['params']['interfaces'][0]['ip'] = ip
    params.add['params']['interfaces'][0]['port'] = 10060
    for g in groups:
        params.add['params']['groups'].append({'groupid':g})
    for t in templates:
        params.add['params']['templates'].append({'templateid':t})
    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(params.add),headers=header).text)
    print(html)

if __name__ == '__main__':
    groups_name()

