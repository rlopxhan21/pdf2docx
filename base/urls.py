from django.urls import path

from .views import PDF2DOCXView

app_name = 'base'

urlpatterns = [
    path('pdf2docx/', PDF2DOCXView.as_view(), name="pdf2docx")
]