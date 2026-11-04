import math as m

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    _n = round(sum(movie["rating"] for movie in movies) / len(movies), 1)

    return _n


def catalog_age_stats(movies, current_year=2026):
    _average = m.ceil(
        sum((current_year - movie["year"]) for movie in movies) / len(movies)
    )
    _new = max((current_year - movie["year"]) for movie in movies)
    _old = min((current_year - movie["year"]) for movie in movies)

    return tuple([_old, _new, _average])


def duration_in_hours(minutes):
    _hour = minutes // 60
    _minute = minutes % 60
    return f"{_hour}ч {_minute}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif 7 >= rating >= 8.9:
        return "хорошо"
    else:
        return "средне" if 5 >= rating >= 6.9 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 > year > 2020:
            return "недавние"
        case _ if year > 2015:
            return "старые"


def genre(movies):
    for _movie in movies:
        if "comedy" in _movie["genres"]:
            continue
        print(_movie["title"])


def high_rating(movies):
    _n = 0
    while _n < len(movies):
        _movie = movies[_n]
        if _movie["rating"] > 9.0:
            print(f"Шедевр: {_movie['title']}, оценка: {_movie['rating']}")
            break
        _n += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    _n = 0
    for _movie in movies:
        _n += 1 if _movie["duration_min"] > threshold else 0
    return _n


def normalize_title(title):
    _words = title.split()
    if not _words:
        return ""

    _norm_words = []
    for word in _words:
        new_word = word[0].upper() + word[1:].lower()
        _norm_words.append(new_word)

    return " ".join(_norm_words)


def make_slug(title):
    _norm_title = normalize_title(title)

    return _norm_title.lower().replace(" ", "-")


def format_report_line(movie):
    return f"{normalize_title(movie["title"])} - {movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, жанры: {mov["genre"] for mov in movie}"


# вывод
def build_report(movies):
    print("Средний рейтинг: ", average_rating(movies))
    print("Средний возраст фильмов: ", catalog_age_stats(movies)[2], " лет")


# build_report(movies)
print(format_report_line(movies))
"""
genre(movies)
high_rating(movies)
"""
