#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (c) 2016 wjika, Inc. All Rights Reserved
    @author: xuchu(xuchu@acfun.tv)
"""
import paramiko


def ssh_qa_server(command):
    """ssh登陆测试服务器并执行shell命令"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname='192.168.71.101', port=22, username='root', password='hostkeeper')
        stdin, stdout, stderr = ssh.exec_command(command)
        results = stdout.readlines()
        # print type(results)
        # print results
        # for i in results:
        #     print i
        ssh.close()
        results = ["<kbd>"+x+"<br>"+"</kbd>" for x in results]
        return results
    except Exception as e:
        return "ssh失败:%s" %e


# Go
if __name__ == '__main__':
    ssh_qa_server(command='sh /usr/local/my_shell/1.sh')
