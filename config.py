# -*- coding: utf-8 -*-
# @Author  : hanzilong
import os
#log目录地址
def logs():
    pathlog=os.getcwd() +"\\logs\\test.log"
    return  pathlog
#测试用例文档地址
def  cases():
    path1=os.getcwd() +"\\case\\testcase.xlsx"
    return path1
#发送测试报告到邮箱
def  dirs():
    dir =os.getcwd() +'\\reports'  # 指定文件目录
    return dir
