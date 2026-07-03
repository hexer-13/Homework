# Виконавець
# Жанр
# Назва альбому
# Тираж
# Вивести дані про платівки, тираж яких перевищує 10000 примірників.

class Song:
    def __init__(self, singer, genre, album, sold):
        self.__singer = singer
        self.__genre = genre
        self.__album = album
        self.__sold = sold

    @property
    def singer(self):
        return self.__singer

    @property
    def genre(self):
        return self.__genre

    @property
    def album(self):
        return self.__album

    @property
    def sold(self):
        return self.__sold

    @singer.setter
    def singer(self, singer):
        try:
            if singer.type == str:
                self.__singer = singer
            else:
                raise TypeError
        except TypeError:
            print("Singer name must be a string")
        except Exception as e:
            print(e)

    @genre.setter
    def singer(self, genre):
        try:
            if genre.type == str:
                self.__genre = genre
            else:
                raise TypeError
        except TypeError:
            print("Genre must be a string")
        except Exception as e:
            print(e)


    @album.setter
    def singer(self, album):
        try:
            if album.type == str:
                self.__album = album
            else:
                raise TypeError
        except TypeError:
            print("Album must be a string")
        except Exception as e:
            print(e)


    @sold.setter
    def sold(self, sold):
        try:
            if sold.type == int or sold.type == float:
                self.__sold = sold
            else:
                raise TypeError
        except TypeError:
            print("Sold amount must be a number")
        except Exception as e:
            print(e)


    def __str__(self):
        return f'||{self.singer} | {self.genre} | {self.album} | {self.sold} ||'

song1 = Song("Name1","genre1", "album1", 2000)
song2 = Song("Name2","genre2", "album2", 4000)
song3 = Song("Name3","genre3", "album3", 6000)
song4 = Song("Name4","genre4", "album4", 8000)
song5 = Song("Name5","genre5", "album5", 10000)
song6 = Song("Name6","genre6", "album6", 12000)
song7 = Song("Name7","genre7", "album7", 14000)
song8 = Song("Name8","genre8", "album8", 16000)

songs_list = [song1, song2, song3, song4, song5, song6, song7, song8]

def songs_with_higher_sales_than_x(list,number):
    res_list = []
    try:
        for song in list:
            if song.sold >= number:
                res_list.append(str(song))
        return res_list
    except TypeError:
        print ("Sales must be a number")
    except Exception as e:
        print(e)

songs_with_higher_sales_than_x(songs_list,10000)
print(songs_with_higher_sales_than_x(songs_list,10000))