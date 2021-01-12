from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework_api_key.permissions import HasAPIKey
from images_similarity.components.images_similarity_component import ImageSimilarityComponent


class ImageSimilarityViewSet(ViewSet):
    permission_classes = [HasAPIKey]

    def __init__(self, **kwargs):
        self.images_similarity_component = ImageSimilarityComponent()

    def list(self, request):

        path1 = request.query_params.get('path1')
        path2 = request.query_params.get('path2')

        if not path1 and not path2:
            raise Exception("Error, path1 and path2 are required fields")
        percentage = self.images_similarity_component.get_similarity_by_path1_and_path2(path1=path1,
                                                                                        path2=path2)
        return JsonResponse({"Result": "Percentage of similarity = {percentage} ".format(percentage=percentage)})
