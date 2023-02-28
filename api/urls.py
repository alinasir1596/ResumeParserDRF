from django.urls import path
from api.views import ParserView, KeywordView, KeywordManagementView, TaggerListView, \
    TaggerRetrieveView, TaggerCreateView, TaggerDestroyView, TaggerUpdateView

urlpatterns = [
    path('parser/', ParserView.as_view()),
    path('keywords-management/', KeywordView.as_view()),
    path('keywords-management/<int:pk>/', KeywordManagementView.as_view()),
    path('keyword-tags/list/', TaggerListView.as_view()),
    path('keyword-tag/create/', TaggerCreateView.as_view()),
    path('keyword-tag/retrieve/<int:pk>/', TaggerRetrieveView.as_view()),
    path('keyword-tag/update/<int:pk>/', TaggerUpdateView.as_view()),
    path('keyword-tag/delete/<int:pk>/', TaggerDestroyView.as_view()),
]
