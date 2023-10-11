<div align="center">

# 正方课表推送 / ZhengFangCoursePush

</div>

<hr>

###### 本项目使用于“正方”教务系统的课表解析

###### 别的系统欢迎 pr(

<hr>

## Feature / 特点

使用 playwright 爬取课表，防止因为教务系统的反爬虫导致的爬取失败
<br>
使用 pushplus 推送课表，简单易用

<hr>

## Install / 部署

clone 所有文件后<br>
需要在<span style="color:blue">``GetPage.py``</span>中更改 `LoginSite`[教务系统登录页面],`CourseSite`[教务系统课表页面],`Account`[教务系统账号],`SecretKey`[教务系统密码]
<br>需要在<span style="color:blue">``run.py``</span>中更改 `Token`[pushplus 的 token],`Topic`[pushplus 的群组代码],`initialTime`[开学日期]

<hr>

## Run / 运行

### python run.py
