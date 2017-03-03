# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from runShell import ssh_qa_server


def index(req):
    return render(req, "index.html", {})


def ssh_info(req):
    return render(req, "ssh_info.html", {})


def ssh_qa(req):
    # tr:生成数列
    tr = range(1, 11)
    context = {"tr": tr}
    return render(req, "ssh_qa_front.html", context=context)


def ssh_qa_runshell(req):
    if req.method == "POST":
        print req.POST["btn_text"]
        results = ssh_qa_server(command='sh /usr/local/my_shell/1.sh')
        # print results
        return HttpResponse(results)
