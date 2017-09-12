# 2w个人教程

**目录**

    本章任务
    基本步骤
    参考资料
    复盘

## 本章任务

* 输入城市名， 调用第三方天气接口，返回该城市的实时天气数据；
* 输入指令，打印帮助文档（一般使用 h 或 help）；
* 输入指令，退出程序的交互（ exit）；
* 在退出程序之前，打印查询过的所有城市。

## 基本思路

1. 新任务在w1任务的基础上主要增加了从天气接口获取数据和解析数据的部分。基本思路：

    确定天气API。先看了百度的天气接口，发现需要实名认证，较复杂。搜索后决定用和风天气API。

    注册后拿到key,很快实现数据获取,较顺利。

2. 数据解析，难点

    JSON数据操作。数据处理时数据类型不匹配的错误花了一些时间。看StackOverflow的帖子发现原来有json.dumps和json.loads两个命令：dumps进的是词典，出的是string；loads则相反，进的string，出的词典。

    读取不同的字段数值时也遇到问题。后来发现原来数据返回的结果中是dictionary嵌套着list，两者的取值方式是不同的。

3. 整合原来的命令，加上输入判断，整合进新的函数。这里需要注意异常处理，还有参数传递的问题。

## 参考资料

* [heweather API doc](https://www.heweather.com/documents/api/v5/now)

* [apscheduler.triggers.cron](http://apscheduler.readthedocs.io/en/3.0/modules/triggers/cron.html#module-apscheduler.triggers.cron): Advanced Python Scheduler (APscheduler) is a Python library to schedule Python code to be executed later, either just once or periodically.

## 复盘

1. Configure platformio-ide-terminal in Atom. Installed the package yesterday but failed to get it working. After some tweaks, I found there was an error saying the package was built for an older version of Atom. Rebuilding the package fixes the issue.

2. Ran the weather_checker2.0.py and found there was issue when inputting an invalid command. Adding try .. except to the else part solved the problem.

3. Got tab/space mix issue when coding. Set tab to 4 spaces and use soft tab according to a StackOverflow post. But it doesn't seem to work. Ended with making invisible characters visible and then copy & paste.

4. How to get the server copy from Git and replace the local one

    ```
    git checkout path/to/file
    ```

5. Use [apscheduler.triggers.cron](http://apscheduler.readthedocs.io/en/3.0/modules/triggers/cron.html#module-apscheduler.triggers.cron) to trigger the whether check program every day.

6. How to get the current time in Python?
