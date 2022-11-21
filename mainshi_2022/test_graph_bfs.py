# coding=utf-8


class Solution:
    """广度优先搜索 算法图解6.4章节"""
    def is_seller(self, person):
        if person.endswith('m'):
            return True
        return False

    def search(self):
        graph = dict()
        graph['you'] = ['alice', 'bob', 'claire']
        graph['bob'] = ['anuj', 'peggy']
        graph['anuj'] = []
        graph['peggy'] = []
        graph['alice'] = ['peggy']
        graph['claire'] = ['thom', 'jonny']
        graph['thom'] = []
        graph['jonny'] = []

        import copy
        is_searched = []
        search_list = copy.deepcopy(graph['you'])
        while search_list:
            search_person = search_list.pop(0)
            if search_person in is_searched:
                continue
            if self.is_seller(search_person):
                return search_person
            else:
                search_list.extend(graph[search_person])
            is_searched.append(search_person)
        return None


if __name__ == '__main__':
    s = Solution()
    ret = s.search()
    print(ret)
