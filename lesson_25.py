# Дополнительное практическое задание по модулю 5 "Классы и объекты"

from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(str(user.password)) == hash(str(password)):
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        self.current_user = self.users[-1]

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            for video_ in self.videos:
                if video_.title == video.title:
                    break
            else:
                self.videos.append(video)

    def get_videos(self, keyword):
        result = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video_title == video.title:
                if self.current_user.age < 18 and video.adult_mode:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=' ')
                    sleep(1)
                print("Конец видео")
                video.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')