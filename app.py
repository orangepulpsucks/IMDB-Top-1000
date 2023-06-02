import csv
from flask import Flask, request, render_template
import psycopg2, random

from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route("/home")
def render_sets():
    poster_link = request.args.get("poster_link", "")
    series_title = request.args.get("series_title", "")
    released_year = request.args.get("released_year", "")
    certificate = request.args.get("certificate", "") 
    runtime = request.args.get("runtime", "")
    genre = request.args.get("genre", "")
    imdb_rating = request.args.get('imdb_rating')
    overview = request.args.get("overview", "")
    meta_score = request.args.get("meta_score", "")
    director = request.args.get("director", "")
    star1 = request.args.get("star1", "")
    star2 = request.args.get("star2", "")
    star3 = request.args.get("star3", "")
    star4 = request.args.get("star4", "")
    no_of_votes = request.args.get("no_of_votes", "")
    gross = request.args.get("gross", "")

    sort_by = request.args.get("sort_by", "series_title")
    sort_dir = request.args.get("sort_dir", "asc")
    limit = request.args.get("limit", 10, type=int)

    from_where_clause = """
        from movie
        where %(series_title)s is null or series_title name ilike %(series_title)s
        and ( %(released_year)s is null or released_year = %(released_year)s )
        and ( %(runtime)s is null or runtime = %(runtime)s )
        and ( %(genre)s is null or genre ilike %(genre)s )
        and ( %(imdb_rating)s is null or imdb_rating = %(imdb_rating)s )
        and ( %(director)s is null or director ilike %(director)s )
    """

    params = {
        "poster_link": f"%{poster_link}%",
        "series_title": f"%{series_title}%",
        "released_year": int(released_year) if released_year else None,
        #"year": int(year) if year and year.isdigit() else 0 
        # if year and not year.isdigit() else None,
        "certificate": f"%{certificate}%",
        "runtime": f"%{runtime}%",
        "genre": f"%{genre}%",
        "imdb_rating": float(imdb_rating) if imdb_rating else None,
        "overview": f"%{overview}%",
        "meta_score": f"%{meta_score}%",
        "Director": f"%{director}%",
        "star1": f"%{star1}%",
        "star2": f"%{star2}%",
        "star3": f"%{star3}%",
        "star4": f"%{star4}%",
        "no_of_votes": f"%{no_of_votes}%",
        "gross": f"%{gross}%",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit


        #  params = {
        # "name": f"%{name}%",
        # "year": int(year) if year and year.isdigit() else 0 
        # if year and not year.isdigit() else None,
        # "casts": f"%{casts}%",
        # "genre": f"%{genre}%",
        # "rating": float(rating) if rating and rating.replace('.', '').isdigit() else 0
        # if rating and not rating.isdigit() else None,
        # "episode": int(episode) if episode and episode.isdigit() else 0
        # if episode and not episode.isdigit() else None,
        # "duration": int(duration) if duration and duration.isdigit() else 0
        # if duration and not duration.isdigit() else None,
        # "network": f"%{network}%",
    }
    
    return render_template("Home.html", params=request.args)
