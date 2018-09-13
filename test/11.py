
class cl:
    BASE_URL = 'www.mnet.com'

    def direct_node_connect(self, end_point):
        # 페이지를 링크로 이동하기 위해서 사용
        return "/".join([self.BASE_URL, str(end_point)])


    def make_url(self, node=None, end_point=None):
        # 외부에서 그냥 호출 가능한 함수...
        return "/".join([self.BASE_URL, str(node) if node !=None else str(end_point), str(end_point) if node != None and end_point != None else ''])

a = 123
b = 'asdasd'

c = cl()
print(c.direct_node_connect(a))

print(c.make_url(node = b, end_point=a))
print(c.make_url(end_point=a))
print(c.make_url(node=a))