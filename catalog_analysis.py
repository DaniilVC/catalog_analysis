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


"""
2 этап
"""


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


"""
3 этап
"""


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


"""
4 этап
"""


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
    _sorted_genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{normalize_title(movie["title"])}"'
        f" ({movie['year']}) - {movie['rating']}/10, "
        f"{duration_in_hours(movie['duration_min'])}, "
        f"жанры: {_sorted_genres}"
    )


"""
5 этап
"""


def titles_sorted_by_rating(movies):
    _n = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    _list = [movie["title"] for movie in _n]

    return _list


def top_n_by_rating(movies, n=3):
    _k = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    _top_n = _k[:n]

    return [(movies["title"], movies["rating"]) for movies in _top_n]


"""
6 этап
"""


def count_by_genre(movies):
    _genre_count = {}
    for data in movies:
        for genre in data.get("genres", []):
            _genre_count[genre] = _genre_count.get(genre, 0) + 1

    return _genre_count


def actor_filmography(movies):
    _actor_films = {}
    for data in movies:
        title = data.get("title", "")
        for actor in data.get("actors", []):
            if actor not in _actor_films:
                _actor_films[actor] = []
            _actor_films[actor].append(title)

    return _actor_films


average = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average_rating(movies)
}

"""
7 этап
"""


def all_genres(movies):
    _genres = set()
    for movie in movies:
        _genres.update(movie.get("genres", set()))
    return _genres


def common_actors(movie1, movie2):
    _actors1 = set(movie1.get("actors", []))
    _actors2 = set(movie2.get("actors", []))

    return _actors1 & _actors2


def genres_only_in_one(movies_a, movies_b):
    _genres_a = all_genres(movies_a)
    _genres_b = all_genres(movies_b)

    return _genres_a - _genres_b


"""
8 этап
"""


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def top_films(movies):
    _top = sorted(
        iter_high_rated(movies), key=lambda movie: movie["rating"], reverse=True
    )[:3]
    for movie in _top:
        print(f"    {format_report_line(movie)}")


# print(sum(m["duration_min"] for m in movies if m["rating"] > 7))


"""
вывод / 9 этап
"""


def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print("Средний рейтинг: ", average_rating(movies))
    print("Средний возраст фильмов: ", catalog_age_stats(movies)[2], " лет\n")
    print("Топ-3 фильма:")
    top_films(movies)
    print("\nФильмов по жанрам:")
    for genre, count in count_by_genre(movies).items():
        print(f"    {genre} - {count}")
    print("\nВсе жанры каталога: ", ", ".join(sorted(all_genres(movies))), "\n")


if __name__ == "__main__":
    build_report(movies)
