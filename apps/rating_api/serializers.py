from rest_framework import serializers

from apps.custom_user.serializers import UserDetailSerializer
from apps.rating_api.models import Vote


class VoteViewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nickname'
    )

    class Meta:
        model = Vote
        fields = [
            'id', 'user', 'vote_int', 'vote_time', 'manga'
        ]


class VoteUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Vote
        fields = [
            'id', 'user', 'vote_int', 'vote_time', 'manga'
        ]
