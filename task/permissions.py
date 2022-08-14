from rest_framework import permissions
from dotenv import load_dotenv
import os

load_dotenv()

KEY_NAME = "Api-Key"
VALID_API_KEY = os.environ.get("VALID_API_KEY")

class HasApiKey(permissions.BasePermission):
    def has_permission(self, request, view):
        user_key = request.headers.get(KEY_NAME)
        
        if user_key == VALID_API_KEY:  
            return True
        return False
