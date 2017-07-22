# coding:utf-8

import sys
import datetime
import io

leetcodeOrLintcodeNum = sys.argv[1]
problemNameArray = sys.argv[2].split()
problemName = '_'.join(problemNameArray)

onlineJudegeName = sys.argv[3] if len(sys.argv) >= 3 else "leetcode"

company = sys.argv[4] if len(sys.argv) >= 4 else ""

currentDate = datetime.date.today().strftime("%Y-%m-%d")
currentTime = datetime.datetime.now()

fileName = currentDate + "-" + onlineJudegeName + "-" + \
    leetcodeOrLintcodeNum + "-" + problemName + ".md"

with io.open(fileName, 'w', encoding='utf8') as file:

    file.write(u"---\n")
    file.write(u"layout: post\n")
    file.write(u"title:  \"" + onlineJudegeName + " " +
               leetcodeOrLintcodeNum + " - " + problemName + "\"\n")
    file.write(u"date:   " + str(currentTime) + "\n")
    file.write(u"categories: " + onlineJudegeName + ", " + company + "\n")
    file.write(u"---\n\n")

    file.write(u"# " + problemName + "\n\n")

    file.write(u"## 一刷\n\n")

    file.write(u"### 代码\n\n")

    file.write(u"```java\n\n```\n\n")

    file.write(u"### 笔记")

    file.close()
