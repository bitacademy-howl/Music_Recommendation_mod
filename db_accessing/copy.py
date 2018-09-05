#
# # VO 객체 내 dict 로부터 객체 값 setting 하던 함수들....만들던거 따로 뺌
# # 나중에 사용....아직..
# def from_dict(self, kwargs):
#     # def from_dict(self, Music_ID, Title = None, Singer = None, Album = None, Genre = None,
#     #               Composer =  None, Lyricist =  None, Hash_Tags = None, Release_Date =  None):
#     self.Music_ID = kwargs["Music_ID"]
#     self.Title = kwargs["Title"]
#     self.Album_ID = ['Album_ID']
#     self.Singer = kwargs["Singer"]
#     self.Genre = kwargs["Genre"]
#     self.Composer = kwargs["Composer"]
#     self.Lyricist = kwargs["Lyricist"]
#     self.Hash_Tags = kwargs["Hash_Tags"]
#
#     # 아래는 앨범 속성으로 따로 뺄 것!!
#     #
#     self.Album = kwargs["Album"]  # 얘는 앨범 속성으로 뺄 것!
#     self.Release_Date = kwargs["Release_Date"]  # 얘는 앨범 속성으로 뺄 것!
#
#     # dict 로 받을 때 object 의 key 를 속성으로 value 를 값으로 하는 객체 생성
#     # from_dict_strict 함수는 외부 인자가 VO에 없어도 생성할 여지가 있음
#     def from_dict_strict(self, dict_data):
#         for a, b in dict_data.items():
#             if isinstance(b, (list, tuple)):
#                 setattr(self, a, [Music_VO(x) if isinstance(x, dict) else x for x in b])
#             else:
#                 setattr(self, a, Music_VO(b) if isinstance(b, dict) else b)