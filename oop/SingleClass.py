class MusicPlayer:

    isUsed = None

    def __new__(cls, *args, **kwargs):
        if(cls.isUsed == None):
            cls.isUsed = super().__new__(cls)
            print("新建对象")
            return cls.isUsed
        return cls.isUsed


if __name__ == '__main__':
    mp3 = MusicPlayer()
    mp4 = MusicPlayer()
    print(mp4 is mp3)


