from django import forms  #引入forms模块
from .models import Comments
#继承forms.ModelForm
class CommentsForm(forms.ModelForm):
    #表单内部类
    class Meta:
        model = Comments    #表单对应的数据库模型为Comments类
        fields = ["name", "email", "url", "content"]  #指定表单显示的字段

