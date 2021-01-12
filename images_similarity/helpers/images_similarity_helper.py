import cv2

from images_similarity.constants import ImagesSimilarityConstants


class ImageSimilarityHelper(object):

    @staticmethod
    def get_similarity_by_path1_and_path2(path1, path2):
        try:
            original = cv2.imread(path1)
        except Exception:
            raise Exception("Error, unable to read image at path1")

        try:
            image_to_compare = cv2.imread(path2)
        except Exception:
            raise Exception("Error, unable to read image at path2")

        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(original, None)
        kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)
        good_points = []
        ratio = ImagesSimilarityConstants.RATIO
        for m, n in matches:
            if m.distance < ratio * n.distance:
                good_points.append(m)

        if len(kp_1) <= len(kp_2):
            lower_kp = len(kp_1)
        else:
            lower_kp = len(kp_2)

        return len(good_points) / lower_kp * 100
