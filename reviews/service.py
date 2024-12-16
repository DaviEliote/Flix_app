import requests
from reviews.repository import ReviewsRepository


class ReviewService:

    def __init__(self):
    
        self.review_service = ReviewsRepository()




    def get_review(self):

        return self.review_service.get_reviews()
    

    def create_review(self, movie, stars, comments):

        review = dict (
            movie=movie,
            stars=stars,
            comments=comments
        )
        return self.review_service.create_review(review)