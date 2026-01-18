import typing


class mediaData:
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
    def __init__ (self, category, name, description, complete = False, rating = "not rated"):
        self.category = category
        self.name = name
        self.description = description
        self.complete = complete
        self.rating = rating
        
        


        #if category is 'tvshow':

    def addTvshow(category, name, complete, seasons, episodes, genre):
        mediaData(category, name, complete)
        mediaData.seasons = seasons
        mediaData.episodes = episodes
        mediaData.episodes = genre

    def addMovie(category, name, complete, genre):
        mediaData(category, name, complete)
        mediaData.genre = genre

    





if __name__ == '__main__':
    print()