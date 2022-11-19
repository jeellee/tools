## 浅谈Python 中 __getattr__与__getattribute__的区别


__getattr__与__getattribute__均是一般实例属性截取函数（generic instance attribute interception method），其中，__getattr__可以用在python的所有版本中，而__getattribute__只可以用到新类型类中(New-style class)，其主要的区别是__getattr__只截取类中未定义的属性，而__getattribute__可以截取所有属性，下面用代码进行说明：

（1）__getattr__

从上面可以看出，对于类c中已定义的实例属性data，p，均显示了出来，而对于未定义的a,b都进行了拦截。

（2）__getattribute__函数

将上面的代码中的__getattr__换成__getattribute__，其他的不做变动

调用实例的属性，可以发现，全部被__getattrbute__予以了拦截。

https://blog.csdn.net/weixin_30675967/article/details/96286645?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-3-96286645-blog-125584307.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-3-96286645-blog-125584307.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=4