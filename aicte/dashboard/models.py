from django.db import models
from register.models import Developer
from django_editorjs_fields import (
    EditorJsJSONField, 
    EditorJsTextField
)

# Create your models here.
class Curriculumn(models.Model):
    user=models.ManyToManyField(Developer)
    
    body = EditorJsJSONField(
        plugins=[
            
            "@editorjs/header",
            "editorjs-github-gist-plugin",
            "@editorjs/code@2.6.0",  # version allowed :)
            "@editorjs/list@latest",
            "@editorjs/inline-code",
            '@editorjs/embed',
            '@editorjs/delimiter',
            
            '@editorjs/marker',
            "@editorjs/table",
        ],
        tools={
            "Gist": {
                "class": "Gist"
            },

            
        },
        null = True,
        blank = True,
    )
    
    
class Message(models.Model):
    sender = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.sender.username}-{self.thread_name}' if self.sender else f'{self.message}-{self.thread_name}'