from rest_framework import serializers
from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = [
            'user'
        ]

    # converts to JSON
    # validations for data passed

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)   # including instance
        # if self.instance:
        #     qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
