from rest_framework import serializers

from fb_backend.models import Feedback


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback', 'author']
