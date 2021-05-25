from django.db import models
from django.conf import settings

# 채팅방 목록을 구성하고, 누가 참여하고 있는지 데이터를 만들고 방이 파괴되거나 사람이 나가면 제거

class Room(models.Model):
    count_users = models.PositiveSmallIntegerField()
    room_name = models.CharField(max_length=255) # 채팅방 이름
    # subject = models.CharField(max_length=255) # 채팅방에 대한 간략한 설명


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)



    