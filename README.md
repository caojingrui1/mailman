# MAILMAN:

## 项目介绍

​	本项目负责管理邮件列表的源码和相关构建任务，架构设计如下：

![1653801153999](doc/assets/1653801153999.png)



## 服务介绍：

+ mailman-web: 主要是web服务，负责与人打交道，主要是架构图中的Web Interface。
+ mailman-core: 主要是对发送的邮件列表进行处理，负责与邮件列表打交道， 主要是架构图的Mailman Core。
+ mailman-exim: 主要是负责邮件的传递，负责与邮件打交道， 主要是架构图中的MTA。



## 安装部署:

![1653801153999](doc/assets/部署图.png)



## 测试用例：

详细测试用例见: [测试用例](https://github.com/opensourceways/mailman/blob/main/doc/%E9%82%AE%E4%BB%B6%E5%88%97%E8%A1%A8%E7%9A%84%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B.xlsx)

