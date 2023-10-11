from Parse import *
from constant import ClassTimeDict
import datetime
import requests
import json
import os
import re
import time


token = ''
topic = ''
initialTime = datetime.datetime.strptime('2023-9-4',"%Y-%m-%d")
sendCheck = {}
while True:
    
    for filename in os.listdir("./"):
        if 'TodayCourse' in filename:
            fileTime = datetime.datetime.strptime(re.compile('TodayCourse(.*).json').search(filename).groups()[0],"%Y-%m-%d")
            break

    week = (datetime.datetime.strptime(str(datetime.date.today()),"%Y-%m-%d") - initialTime).days//7+1
    weekDay = datetime.date.today().isoweekday()

    if fileTime != datetime.datetime.strptime(str(datetime.date.today()),"%Y-%m-%d"):
        os.remove(filename)
        sendCheck = {}
        with open(f'TodayCourse{str(datetime.date.today())}.json','w',encoding='utf-8') as f:
            json.dump(GetTodayCourse(weekDay),f)
        
    with open(f'TodayCourse{str(datetime.date.today())}.json','r+',encoding='utf-8') as f:
        courseData = json.load(f)

    #以上的代码均为初始化代码
    #检查课表文件是否需要更新，需要更新则更新

    #计算单双周
    if week % 2 == 0:
        singleWeek = '双'
    else:
        singleWeek = '单'

    for course in courseData:
        startLevel = int(course['courseLevel'].split('-')[0])
        startTime = ClassTimeDict[startLevel]
        reResult = re.compile('周数：(.*)周(.*)').search(course['courseWeek']).groups()
        courseWeek = reResult[0]
        courseSingle = reResult[1]
        if reResult[1] != '':
            weekJudge = (singleWeek == re.compile('\((.*)\)').search(courseSingle).groups()[0])
        else:
            weekJudge = True
        if '-' not in courseWeek:
            courseWeek = courseWeek + '-' + courseWeek
        if int(courseWeek.split('-')[0]) <= week <= int(courseWeek.split('-')[1]) and weekJudge:
            print(course['courseName'],course['courseTeacher'])

            if startLevel not in sendCheck:sendCheck[startLevel]=False#初始化

            if int((datetime.datetime.strptime(f"{str(datetime.date.today())} {startTime}","%Y-%m-%d %H:%M") - datetime.datetime.today()).seconds/60) <= 10 \
                and not sendCheck[startLevel]:
                print('！推送信息！')
                #推送操作
                push=requests.get(f'http://www.pushplus.plus/send?token={token}&title=新的上课通知！&content='
                         +f"课室:{course['courseLocation']}|课程:{course['courseName']}|授课老师:{course['courseTeacher'].replace('教师：','')}"
                         +'&template=html'
                         +f'&topic={topic}')
                push_result=json.loads(push.text)
                if push_result['code'] == 200:
                    print(push_result['msg'])
                else:
                    print(push_result['msg'])

                sendCheck[startLevel] = True



    time.sleep(60)


