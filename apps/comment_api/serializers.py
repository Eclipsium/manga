from rest_framework import serializers

from apps.comment_api.models import Comments
from apps.custom_user.serializers import UserDetailSerializer


class CommentPostSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Comments
        fields = [
           'id', 'created_by', 'create_time', 'manga', 'comment_text'
        ]


class CommentGetSerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer()

    class Meta:
        model = Comments
        fields = [
            'id', 'created_by', 'create_time', 'manga', 'comment_text'
        ]
