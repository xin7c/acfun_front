# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from runShell import ssh_qa_server
from front_shell_list import front_shell_list


def index(req):
    return render(req, "index.html", {})


def req(req):
    print req.GET
    return HttpResponse(req.GET)


def ssh_info(req):
    return render(req, "ssh_info.html", {})


def ssh_qa(req):
    context = {}
    for i, j in enumerate(front_shell_list):
        # print i+1, j
        context[str(i + 1)] = j
    tr = range(1, len(front_shell_list) + 1)
    shell_list = front_shell_list
    context_zip = zip(tr, shell_list)

    context["context_zip"] = context_zip
    # print context
    return render(req, "ssh_qa_front.html", context=context)


def ssh_qa_runshell(req):
    if req.method == "POST":
        btn_text = req.POST["btn_text"]
        results = ssh_qa_server(shell_path='/root/deploy/front/node-source/',
                                shell_name=btn_text)
        # print results
        return HttpResponse(results)
