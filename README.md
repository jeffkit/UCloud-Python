#UCloud-Python

UCloud.cn API的非官方Python实现。官方的实现稍啰嗦，且使用方法不够pythonic,遂自个撸一个更简单的。

安装：

    pip install ucloud-py

使用方法:
    
    >>>from UCloud import UCloudClient
    >>>cli = UCloudClient('public_key', 'private_key')
    >>>cli.DescribeUHostInstance(Region='cn-north-02')  # 获取所有UHost信息

看到这里，应该懂了吧？API参数中的Action就是用来调用cli的方法，参数名全按照API说明文档中的。

好吧，还有一种恶心的传参方式要注意：例如：DescribeUHostInstance接口中的UHostIds.n。遇到这种参数时，调用函数时，只需要以.号前面的部份作为参数名，参数值则需要是一个list或tuple。举例：

    >>> rsp = cli.DescribeUHostInstance(Region='cn-north-02', UHostIds=['myhostid', 'yourhostid'])

UCloud接口文档[在此](http://docs.ucloud.cn/api/apilist.html)
