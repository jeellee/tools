#! coding=utf-8
"""
NC388 砖墙的垂线
描述
牛牛有一堵砖墙，墙上有 n 行砖块，所有砖的高度都是一样的，尽管整面墙的宽度是一样，但是每块砖的宽度可能不一样。你要在这堵墙上放置一条平行
于砖墙垂直于地面的垂线，请问这个垂线最少需要经过几块砖。如果你画的线只是从砖块边缘经过则不算是经过。

数据范围： 1 \le n \le 1000 \1≤n≤1000  ，整面墙的宽度满足 1 \le val \le 1000 \1≤val≤1000

6
[[1, 2, 3],
 [1, 2, 3]
]

{1: 1, 3: 2, 6: 3}

[[1, 2, 3],
 [3, 3]
]
123

1）不能在墙两端4
2）切破砖的次数越少越好  找一个位置
"""
#  2 3
# -- - ---
# 1  3
# - -- ---


def func():
    """计算每行砖可以切的位置index
    然后将每行砖可以切的位置都累加， 可以切的位置最多的一个，就是结果
    """
    # arrays = [[1, 2, 3],
    #          [1, 2, 3]
    #          ]
    # arrays = [[1, 2, 3],
    #           [3, 3]

    #           ]
    arrays = [[1, 2, 3],
              [3, 3],
              [1, 2, 3]
              ]
    arrays = [[1, 2, 3],
              [3, 3],
              [3, 2, 1]
              ]
    data_dict = {}
    for array in arrays:
        row_sum = 0
        for v in array[:-1]:   # [1, 2, 3]
            row_sum += v
            if row_sum not in data_dict:
                data_dict[row_sum] = 1
            else:
                data_dict[row_sum] += 1

    print data_dict
    ret = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)[0][0]
    print ret
    return ret


if __name__ == "__main__":
    func()


