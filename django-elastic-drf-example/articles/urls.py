from rest_framework import routers 

from articles import views
 

app_name = 'articles' 

router = routers.DefaultRouter(trailing_slash=True)
router.register('articles', views.ArticleViewSet, basename='articles')

urlpatterns = router.urls