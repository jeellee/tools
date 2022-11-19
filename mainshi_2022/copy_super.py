# encoding: utf-8


class Hello():
    def hello(self, name):
        print 'hello, %s' % name

h = Hello()
h.hello('jeellee')

print type(Hello)
print type(h)

print "-----------------------------"

# type 创建类


def fn(self, name):
    print 'hello, %s' % name

Hello2 = type('Hello', (object,), dict(hello=fn))

h = Hello2()
h.hello('jeellee')
print type(Hello2)
print type(h)


# metalclass 控制类的创建行为(允许创建类和修改类)

if __name__ == "__main__":
    import os
    import shutil
    import datetime
    s_path = "E:\da"
    # s_path = "E:\\test"
    t_path = "E:\other"
    # files = os.listdir(s_path)
    # for f in files:
    #     try:
    #         print unicode(f, "utf-8")
    #     except:
    #         print f
    all_file_type = set()
    data = os.walk(s_path)
    is_move = False
    for root, dirs, files in data:
        for file in files:
            # print "1111111", root
            # print "------", file
            file_type = str(file.split(".")[-1]).lower()
            all_file_type.add(file_type)
            if file_type in ("jpg", "mp4", "zip"):
                s_file_path = os.path.join(root, file)
                print s_file_path
                if is_move:
                    if os.path.exists(os.path.join(t_path, file)):
                        new_file = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')+"."+file_type
                        new_s_file_path = os.path.join(root, new_file)
                        shutil.move(s_file_path, new_s_file_path)
                        s_file_path = new_s_file_path
                    shutil.move(s_file_path, t_path)
    # print data.next()
    print all_file_type

