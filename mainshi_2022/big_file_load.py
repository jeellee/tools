# coding: utf-8
import http.server


def read_file(filename, buf_size=8192):
    with open(filename, "rb") as f:
        while True:
            content = f.read(buf_size)
            if content:
                yield content
            else:
                break


def big_file_download(request):
    filename = "filename"
    read_file(filename)


def test():
    filename = "filename"
    data = read_file(filename, buf_size=4)
    return data


if __name__ == "__main__":
    ret = test()
    for i in ret:
        print(i)
