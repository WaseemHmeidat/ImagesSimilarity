from images_similarity.helpers.images_similarity_helper import ImageSimilarityHelper


class ImageSimilarityComponent(object):

    def get_similarity_by_path1_and_path2(self, path1, path2):
        return ImageSimilarityHelper.get_similarity_by_path1_and_path2(path1=path1, path2=path2)

