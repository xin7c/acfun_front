#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (c) 2016 wjika, Inc. All Rights Reserved
    @author: xuchu(xuchu@acfun.tv)
"""
import paramiko
import time


def ssh_qa_server(shell_path, shell_name):
    """ssh登陆测试服务器并执行shell命令"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c_time = "=" * 10 + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "=" * 10 + "\n"
    log_name = str(shell_path) + "logs/" + str(shell_name) + ".log"
    print log_name
    try:
        ssh.connect(hostname='192.168.60.226', port=22, username='root', password='acfun-ops')
        print "已连接...正在执行[%s]..." % str(shell_name)
        stdin, stdout, stderr = ssh.exec_command("sh " + shell_path + shell_name)
        results = stdout.readlines()
        # print results
        for i in results:
            #     print i.strip("\n")
            ssh.exec_command("echo -n \"%s\">>%s" % (i, log_name))
        ssh.exec_command("echo -n \"%s\">>%s" % (c_time, log_name))

        results = ["<kbd>" + x + "<br>" + "</kbd>" for x in results]
        print results
        ssh.close()
        return results

    except Exception as e:
        return "ssh失败:%s" % e

def ssh_qa_printLogs(shell_path, shell_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    log_name = str(shell_path) + "logs/" + str(shell_name) + ".log"
    try:
        ssh.connect(hostname='192.168.60.226', port=22, username='root', password='acfun-ops')
        print "已连接...正在执行[%s]..." % str(shell_name)
        stdin, stdout, stderr = ssh.exec_command("tail -n 50 " + log_name)
        results = stdout.readlines()
        results = ["<kbd>" + x + "<br>" + "</kbd>" for x in results]
        print results
        ssh.close()
        return results
    except Exception as e:
        return "ssh失败:%s" % e
# Go
if __name__ == '__main__':
    # ssh_qa_server(command='sh /root/deploy/front/node-source/acfun-cms-app.master.sh')
    ssh_qa_server(shell_path="/root/deploy/front/node-source/", shell_name='acfun-cms-app.master.sh')
