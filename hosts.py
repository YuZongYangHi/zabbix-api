#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import requests 
import json 
import config  as config 
import parameter as params
import sys,os
import config as self 

headers = {'Content-Type': 'application/json'}
def gettoken(func):
    
    auth = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.zabbix_user,
                "password":self.zabbix_pass
            },
            "id": 1,
            "auth":None,
        }
    response = requests.post(self.zabbix_address,data=json.dumps(auth),headers=headers)
    try:
        auth_id = json.loads(response.text)['result']
    except Exception as e:
        return 0 

    def wrapper(*args,**kwargs):
        
        return func(auth_id,**kwargs)
    return wrapper


def gethost_all(group=None):
    conn = mysql.connect(
        host = self.mysql_host,
        port = 3306,
        user = self.mysql_user,
        passwd = self.mysql_pass,
        db = 'zabbix',
        )
    cur = conn.cursor()
    response = cur.execute('select host,hostid from hosts')
    result = [ i for i in cur.fetchmany(response)]
    cur.close()
    conn.commit()
    conn.close()
    return result 

@gettoken
def gethost(id,host=None):
    hosts = gethost_all()
    if host:
        hosts = host
    params.GetHostTo_id['auth'] = id
    params.GetHostTo_id['params']['filter']['host'] = []

    if host:
        params.GetHostTo_id['params']['filter']['host'].append(hosts)
    else:
        for i in hosts:
            params.GetHostTo_id['params']['filter']['host'].append(i[0])

    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(params.GetHostTo_id),headers=headers).text)
    return html['result']

@gettoken
def getgroup(id,hostname=None):
    params.GetHostGroups['auth'] = id
    params.GetHostGroups['params']['filter']['host'] = []
    for i in hostname:
        params.GetHostGroups['params']['filter']['host'].append(i)

    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(params.GetHostGroups),headers=headers).text)
    return html['result']

@gettoken
def gettemplate(id,hostid=None):
    params.GetHostTemplates['auth'] = id
    params.GetHostTemplates['params']['hostids'] = []
    for i in hostid:
        params.GetHostTemplates['params']['hostids'].append(i)
    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(params.GetHostTemplates),headers=headers).text)
    return html['result']

def Input(hostlist=None):
    #获取主机id,主机名称,监控状态
    status = []
    hosts = []
    host_ids = []
    hosts_response = gethost(host=hostlist)
    for i in hosts_response:
        status.append(i['status'])
        hosts.append(i['host'])
        host_ids.append(i['hostid'])
    #获取主机群组
    groups_response = getgroup(hostname=hosts)
    groups = []
    for x in groups_response:
        group = ""
        for y in x['groups']:
            group += y['name'] + ','
        group = group.rstrip(',')
        groups.append(group)
    #获取主机模版
    templates_response = gettemplate(hostid=host_ids)
    templates = []

    for x in templates_response:
        template = ""
        for y in  x['parentTemplates']:
            template += y['name']  + ','
       
        templates.append(template.rstrip(','))

    result = []
    for i in range(len(hosts)):
        temp = {}
        temp['id'] = host_ids[i]
        temp['host_name'] = hosts[i]
        temp['host_groups'] = groups[i]
        temp['host_template'] = templates[i]
        temp['status'] = status[i]
        temp['operation'] = host_ids[i] + ',' + status[i]
        result.append(temp)
    return result

@gettoken
def host_disable(id,hostid,status):
    data = {
        "1": 0,
        "0": 1
    }

    code = data[str(status)]
    params.update['params']['status'] = code
    params.update['auth'] = id
    params.update['params']['hostid'] = hostid
    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(params.update),headers=headers).text)
    return True 

@gettoken
def host_deleted(id,hostid):
    params.delete['params'] = []
    params.delete['auth'] = id
    params.delete['params'].append(hostid)
    html = json.loads(requests.post(self.zabbix_address,data=json.dumps(params.delete),headers=headers).text)
    return 1

if __name__ == '__main__':
   Input()
