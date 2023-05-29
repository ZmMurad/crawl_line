from django.forms import ModelForm, Textarea
from .models import Text_Crawl_Line

class Text_Form(ModelForm):
    class Meta:
        model=Text_Crawl_Line
        fields=["text",]
        widgets={
            "text":Textarea(attrs={"class":"form-check-input","rows":5})
        }
        labels={
            "text":"Текст"
        }