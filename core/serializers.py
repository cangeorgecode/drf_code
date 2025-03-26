from rest_framework import serializers
from .models import Task
import re

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        if not re.match(r'^[a-zA-Z0-9 ]+$', value):
            raise serializers.ValidationError("Title can only contain letters, numbers, and spaces—no special characters allowed.")
        return value

    # Add validation for description
    def validate_description(self, value):
        # Allow empty or null description since it's optional
        if value is None or value.strip() == "":
            return value  # Return as-is if empty or null
        
        # Strip whitespace and check length
        value = value.strip()
        if len(value) > 1000:  # Arbitrary limit to prevent abuse
            raise serializers.ValidationError("Description cannot exceed 1000 characters.")
        
        # Optional: Restrict special characters (less strict than title)
        if not re.match(r'^[a-zA-Z0-9 ,.!?-]+$', value):
            raise serializers.ValidationError("Description can only contain letters, numbers, spaces, and basic punctuation (,.!?-).")
        
        return value