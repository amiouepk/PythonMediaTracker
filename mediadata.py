import typing


CATEGORY_DEFAULT = ''
NAME_DEFAULT = ''
RATING_DEFAULT = "not rated"


class MediaData:
    # 
    # name = ''
    # description = ''
    # month = 0
    # day = ''
    # year = ''
    # genre = ''
    # complete = False
    # Episodes = 0
    # Seasons = 0

    #string, string, partial
    def __init__ (self, category, name, description, complete = False, rating = "not rated", rating_scale):
        self.category = category
        self.name = name
        self.description = description
        self.complete = complete
        self.rating = rating
        
    def dipslay_media_category(self):
        if self.category is '':
            print("Category: (Left Blank)")
        else:
            print(f"Category: {self.category}")

    def display_media_name(self):
        if self.name is '':
            print("Name: (Left Blank)")
        else:
            print(f"Name: {self.name}")

    def display_media_description(self):
        if self.description is '':
            print("Description: (Left Blank)")
        else:
            print(f"Description: {self.description}")

    def display_media_complete(self):
        if self.complete is False:
            print("Complete: No")
        else:
            print("Complete: Yes")

    def display_media_rating(self):
        if self.rating_scale is '':
            if self.rating is "not rated":

        if self.rating is "not rated":


    
 
    
class TvShow(MediaData):

    def __init__ (self, name = '', description = '', complete = False, rating = "not rated", rating_scale = '', seasons = 1, episodes = 1, genre = 'none'):
        super().__init__('movie', name, description, complete, rating, rating_scale)

        TvShow.seasons = seasons
        TvShow.episodes = 1
        TvShow.genre = genre


class Movie(MediaData):
    def __init__ (self, name = '', description = '', complete = False, rating = "not rated", rating_scale = '', runtime = '', genre = 'none'):
        super().__init__('tvshow', name, description, complete, rating, rating_scale)

        Movie.runtime = runtime
        Movie.genre = genre






if __name__ == '__main__':
    print()