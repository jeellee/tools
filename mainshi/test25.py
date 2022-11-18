# -*- coding: utf-8 -*-

"""
RESTFul:
RESTful架构，目前是比较流行的一种互联网软件架构。REST，即Representational State Transfer的缩写。


REST的六个特性：
客户端-服务器: 客户端和服务器之间隔离，服务器提供服务，客户端进行消费。
无状态: 从客户端到服务器的每个请求都必须包含理解请求所必需的信息。换句话说， 服务器不会存储客户端上一次请求的信息用来给下一次使用。
可缓存: 服务器必须明示客户端请求能否缓存。
分层系统: 客户端和服务器之间的通信应该以一种标准的方式，就是中间层代替服务器做出响应的时候，客户端不需要做任何变动。
统一的接口: 服务器和客户端的通信方法必须是统一的。
按需编码: 服务器可以提供可执行代码或脚本，为客户端在它们的环境中执行。这个约束是唯一一个是可选的。


RESTful web services 概念的核心就是“资源”。
资源可以用 URI 来表示。
客户端使用 HTTP 协议定义的方法来发送请求到这些 URIs，当然可能会导致这些被访问的”资源“状态的改变。

说白点就是网站即软件，再白点就是一个服务软件支持http的四种方法：
GET用来获取资源(返回html页面)，POST用来新建资源、更新资源(不用返回html页面, 只有数据)，PUT用来更新资源，DELETE用来删除资源
HTTP 标准的方法有如下:
==========  =====================  ==================================
HTTP 方法   行为                   示例
==========  =====================  ==================================
GET         获取资源的信息         http://example.com/api/orders
GET         获取某个特定资源的信息  http://example.com/api/orders/123
POST        创建新资源             http://example.com/api/orders
PUT         更新资源               http://example.com/api/orders/123
DELETE      删除资源               http://example.com/api/orders/123
==========  ====================== ==================================

REST 设计不需要特定的数据格式。在请求中数据可以以 JSON 形式, 或者有时候作为 url 中查询参数项。
"""

class Node():
  __slots__=['_item', '_next']    # 限定Node实例的属性
  def __init__(self,item):
    self._item=item
    self._next=None              # Node的指针部分默认指向None
  def getItem(self):
    return self._item
  def getNext(self):
    return self._next
  def setItem(self,newitem):
    self._item=newitem
  def setNext(self,newnext):
    self._next=newnext


class SingleLinkedList():
  def __init__(self):
    self._head=None  # 初始化链表为空表
    self._size=0

  def isEmpty(self):
      return self._head == None

  def add(self, item):
      temp = Node(item)
      temp.setNext(self._head)
      self._head = temp

  def append(self, item):
      temp = Node(item)
      if self.isEmpty():
          self._head = temp  # 若为空表，将添加的元素设为第一个元素
      else:
          current = self._head
          while current.getNext() != None:
              current = current.getNext()  # 遍历链表
          current.setNext(temp)  # 此时current为链表最后的元素

  def search(self, item):
      current = self._head
      founditem = False
      while current != None and not founditem:
          if current.getItem() == item:
              founditem = True
          else:
              current = current.getNext()
      return founditem


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# def create_linked_list(arr=None, n):


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next
        return pre









