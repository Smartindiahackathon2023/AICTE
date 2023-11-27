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