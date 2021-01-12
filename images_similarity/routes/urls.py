from rest_framework import routers

from images_similarity.views.images_similarity_controller import ImageSimilarityViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register("images_similarity", ImageSimilarityViewSet, basename="images-similarity")
urlpatterns = []
urlpatterns = router.urls
