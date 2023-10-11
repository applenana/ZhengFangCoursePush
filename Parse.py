from GetPage import *
from bs4 import BeautifulSoup
import json
import re



'''
for weekDay in range(1,6):#从星期一遍历到星期五
    print(weekDay)
'''

def GetTodayCourse(weekDay:[int,str] = 1):
    debug = False#测试开关，工作时请关闭

    if debug:
        with open('test.html','r+',encoding='utf-8') as f:
            content = f.read()
    else:
        content = GetPagef()
    soup = BeautifulSoup(str(content),'lxml')
    tabel = soup.find('tbody',attrs = {'id' : 'xq_' + str(weekDay)})#某一天的所有课程

    returnJson = []
    for course in tabel.find_all('tr')[1::]:
        #print(course)
        try:courseLevel = course.find_all('td')[0].find('span',{'class':"festival"}).get_text()
        except:courseLevel = courseLevel

        try:courseContent = course.find_all('td')[1]
        except:courseContent = course.find_all('td')[0]

        #print(courseContent)
        contentSplit = courseContent.find_all('font',{'color':'blue'})
        courseName = contentSplit[0].get_text()
        courseWeek = contentSplit[1].get_text()
        courseLocation = contentSplit[2].get_text()
        courseTeacher = contentSplit[3].get_text()
        #print(courseName,courseWeek,courseLocation,courseTeacher,courseLevel)
        courseDict = {}
        courseDict['courseName'] = courseName
        courseDict['courseWeek'] = courseWeek
        courseDict['courseLocation'] = courseLocation
        courseDict['courseTeacher'] = courseTeacher
        courseDict['courseLevel'] = courseLevel
        returnJson.append(courseDict)
    
    return returnJson
