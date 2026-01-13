
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
    def __init__ (category, name, complete):
        mediaData.category = category
        mediaData.name = name
        mediaData.complete = complete

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