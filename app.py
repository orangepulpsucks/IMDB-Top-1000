import csv
from flask import Flask, request, render_template
import psycopg2, random, datetime

from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

# Random Series Cache
random_series_cache = None
cache_date = None

# TEMPLATE
# @app.route("/about")
#  def render_sets4():
#     return render_template("about.html")
# Notes: "render_sets#" are buggy so just choose one that isn't buggy

@app.route("/about")
def render_sets4():
    return render_template("about.html")

@app.route("/random-film")
def render_sets5():
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
    limit = request.args.get("limit", 1000, type=int)

    from_where_clause5 = """
        from movie
        where %(series_title)s is null or series_title ilike %(series_title)s
        and ( %(released_year)s is null or released_year = %(released_year)s )
        and ( %(runtime)s is null or runtime = %(runtime)s )
        and ( %(genre)s is null or genre ilike %(genre)s )
        and ( %(imdb_rating)s is null or imdb_rating = %(imdb_rating)s )
        and ( %(director)s is null or director ilike %(director)s )
    """

    params5 = {
        "poster_link": f"%{poster_link}%",
        "series_title": f"%{series_title}%",
        "released_year": int(released_year) if released_year and released_year.isdigit() else 0
        if released_year and not released_year.isdigit() else None,
        "certificate": f"%{certificate}%",
        "runtime": int(runtime) if runtime and runtime.isdigit() else 0
        if runtime and not runtime.isdigit() else None,
        "genre": f"%{genre}%",
        "imdb_rating": float(imdb_rating) if imdb_rating and imdb_rating.replace('.', '').isdigit() else 0
        if imdb_rating and not imdb_rating.isdigit() else None,
        "overview": f"%{overview}%",
        "meta_score": f"%{meta_score}%",
        "director": f"%{director}%",
        "star1": f"%{star1}%",
        "star2": f"%{star2}%",
        "star3": f"%{star3}%",
        "star4": f"%{star4}%",
        "no_of_votes": int(no_of_votes) if no_of_votes and no_of_votes.isdigit() else 0
        if no_of_votes and not no_of_votes.isdigit() else None,
        "gross": f"%{gross}%",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit
}

    def get_sort_dir5(col):
        if col== sort_by:
            return "desc" if sort_dir == "asc" else "asc"
        else:
            return "asc"
        
    with conn.cursor() as cur:
        cur.execute(f"""select series_title, released_year, runtime, genre, imdb_rating, director, poster_link, certificate, overview, meta_score, star1, star2, star3, star4, no_of_votes, gross 
                        {from_where_clause5} 
                        order by {sort_by} {sort_dir} 
                        limit %(limit)s 
                    """,
                    params5)
        results5 = list(cur.fetchall())  
       
        # Select a random movie name from the results
        random_series = random.choice(results5)


    return render_template("random-film.html",
                           result_random_series=random_series, 
                           params3=request.args
                           )


@app.route("/directory")
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
    limit = request.args.get("limit", 1000, type=int)

    from_where_clause = """
        from movie
        where %(series_title)s is null or series_title ilike %(series_title)s
        and ( %(released_year)s is null or released_year = %(released_year)s )
        and ( %(runtime)s is null or runtime = %(runtime)s )
        and ( %(genre)s is null or genre ilike %(genre)s )
        and ( %(imdb_rating)s is null or imdb_rating = %(imdb_rating)s )
        and ( %(director)s is null or director ilike %(director)s )
    """

    params = {
        "poster_link": f"%{poster_link}%",
        "series_title": f"%{series_title}%",
        "released_year": int(released_year) if released_year and released_year.isdigit() else 0
        if released_year and not released_year.isdigit() else None,
        "certificate": f"%{certificate}%",
        "runtime": int(runtime) if runtime and runtime.isdigit() else 0
        if runtime and not runtime.isdigit() else None,
        "genre": f"%{genre}%",
        "imdb_rating": float(imdb_rating) if imdb_rating and imdb_rating.replace('.', '').isdigit() else 0
        if imdb_rating and not imdb_rating.isdigit() else None,
        "overview": f"%{overview}%",
        "meta_score": f"%{meta_score}%",
        "director": f"%{director}%",
        "star1": f"%{star1}%",
        "star2": f"%{star2}%",
        "star3": f"%{star3}%",
        "star4": f"%{star4}%",
        "no_of_votes": int(no_of_votes) if no_of_votes and no_of_votes.isdigit() else 0
        if no_of_votes and not no_of_votes.isdigit() else None,
        "gross": f"%{gross}%",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit
}

    def get_sort_dir(col):
        if col== sort_by:
            return "desc" if sort_dir == "asc" else "asc"
        else:
            return "asc"
        
    with conn.cursor() as cur:
        cur.execute(f"""select series_title, released_year, runtime, genre, imdb_rating, director, poster_link, certificate, overview, meta_score, star1, star2, star3, star4, no_of_votes, gross 
                        {from_where_clause} 
                        order by {sort_by} {sort_dir} 
                        limit %(limit)s 
                    """,
                    params)
        results = list(cur.fetchall())  

        cur.execute(f"select count(*) as count {from_where_clause}", params)
        count = cur.fetchone()["count"]

    return render_template("Directory.html",
                           movie=results, 
                           params=request.args, 
                           get_sort_dir=get_sort_dir,
                           result_count =count,
                           )

@app.route("/old-boy")
def render_sets2():
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
    limit = request.args.get("limit", 1000, type=int)

    from_where_clause2 = """
        from movie
        where %(series_title)s is null or series_title ilike %(series_title)s
        and ( %(released_year)s is null or released_year = %(released_year)s )
        and ( %(runtime)s is null or runtime = %(runtime)s )
        and ( %(genre)s is null or genre ilike %(genre)s )
        and ( %(imdb_rating)s is null or imdb_rating = %(imdb_rating)s )
        and ( %(director)s is null or director ilike %(director)s )
    """

    params2 = {
        "poster_link": f"%{poster_link}%",
        "series_title": f"%{series_title}%",
        "released_year": int(released_year) if released_year and released_year.isdigit() else 0
        if released_year and not released_year.isdigit() else None,
        "certificate": f"%{certificate}%",
        "runtime": int(runtime) if runtime and runtime.isdigit() else 0
        if runtime and not runtime.isdigit() else None,
        "genre": f"%{genre}%",
        "imdb_rating": float(imdb_rating) if imdb_rating and imdb_rating.replace('.', '').isdigit() else 0
        if imdb_rating and not imdb_rating.isdigit() else None,
        "overview": f"%{overview}%",
        "meta_score": f"%{meta_score}%",
        "director": f"%{director}%",
        "star1": f"%{star1}%",
        "star2": f"%{star2}%",
        "star3": f"%{star3}%",
        "star4": f"%{star4}%",
        "no_of_votes": int(no_of_votes) if no_of_votes and no_of_votes.isdigit() else 0
        if no_of_votes and not no_of_votes.isdigit() else None,
        "gross": f"%{gross}%",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit
    }

    def get_sort_dir2(col):
        if col== sort_by:
            return "desc" if sort_dir == "asc" else "asc"
        else:
            return "asc"
        
    with conn.cursor() as cur:
        cur.execute(f"""select series_title, released_year, runtime, genre, imdb_rating, director, poster_link, certificate, overview, meta_score, star1, star2, star3, star4, no_of_votes, gross 
                        {from_where_clause2} 
                        order by {sort_by} {sort_dir} 
                        limit %(limit)s 
                    """,
                    params2)
        results2 = list(cur.fetchall())  

        # Manually setting what I want to display for my old-boy.html page

        # Director
        cur.execute(f"select director as old_boy_director from movie where series_title ilike '%old boy%'")
        old_boy_director = cur.fetchone()["old_boy_director"]

        # Year
        cur.execute(f"select released_year as old_boy_year from movie where series_title ilike '%old boy%'")
        old_boy_year = cur.fetchone()["old_boy_year"]

        # Poster
        cur.execute(f"select poster_link as old_boy_poster from movie where series_title ilike '%old boy%'")
        old_boy_poster = cur.fetchone()["old_boy_poster"]

        # Starring
        cur.execute(f"select star1 as old_boy_star1 from movie where series_title ilike '%old boy%'")
        old_boy_star1 = cur.fetchone()["old_boy_star1"]

        cur.execute(f"select star2 as old_boy_star2 from movie where series_title ilike '%old boy%'")
        old_boy_star2 = cur.fetchone()["old_boy_star2"]

        cur.execute(f"select star3 as old_boy_star3 from movie where series_title ilike '%old boy%'")
        old_boy_star3 = cur.fetchone()["old_boy_star3"]

        cur.execute(f"select star4 as old_boy_star4 from movie where series_title ilike '%old boy%'")
        old_boy_star4 = cur.fetchone()["old_boy_star4"]

        # Overview
        cur.execute(f"select overview as old_boy_overview from movie where series_title ilike '%old boy%'")
        old_boy_overview = cur.fetchone()["old_boy_overview"]


        return render_template("old-boy.html",
                           movie=results2,
                           result_old_boy_director=old_boy_director,
                           result_old_boy_year=old_boy_year,
                           result_old_boy_poster=old_boy_poster,
                           result_old_boy_star1=old_boy_star1,
                           result_old_boy_star2=old_boy_star2,
                           result_old_boy_star3=old_boy_star3,
                           result_old_boy_star4=old_boy_star4,
                           result_old_boy_overview=old_boy_overview
                           )


@app.route("/")
def render_sets6():
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
    limit = request.args.get("limit", 1000, type=int)

    from_where_clause6 = """
        from movie
        where %(series_title)s is null or series_title ilike %(series_title)s
        and ( %(released_year)s is null or released_year = %(released_year)s )
        and ( %(runtime)s is null or runtime = %(runtime)s )
        and ( %(genre)s is null or genre ilike %(genre)s )
        and ( %(imdb_rating)s is null or imdb_rating = %(imdb_rating)s )
        and ( %(director)s is null or director ilike %(director)s )
    """

    params6 = {
        "poster_link": f"%{poster_link}%",
        "series_title": f"%{series_title}%",
        "released_year": int(released_year) if released_year and released_year.isdigit() else 0
        if released_year and not released_year.isdigit() else None,
        "certificate": f"%{certificate}%",
        "runtime": int(runtime) if runtime and runtime.isdigit() else 0
        if runtime and not runtime.isdigit() else None,
        "genre": f"%{genre}%",
        "imdb_rating": float(imdb_rating) if imdb_rating and imdb_rating.replace('.', '').isdigit() else 0
        if imdb_rating and not imdb_rating.isdigit() else None,
        "overview": f"%{overview}%",
        "meta_score": f"%{meta_score}%",
        "director": f"%{director}%",
        "star1": f"%{star1}%",
        "star2": f"%{star2}%",
        "star3": f"%{star3}%",
        "star4": f"%{star4}%",
        "no_of_votes": int(no_of_votes) if no_of_votes and no_of_votes.isdigit() else 0
        if no_of_votes and not no_of_votes.isdigit() else None,
        "gross": f"%{gross}%",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit
    }

    def get_sort_dir6(col):
        if col == sort_by:
            return "desc" if sort_dir == "asc" else "asc"
        else:
            return "asc"

    with conn.cursor() as cur:
        cur.execute(f"""select series_title, released_year, runtime, genre, imdb_rating, director, poster_link, certificate, overview, meta_score, star1, star2, star3, star4, no_of_votes, gross 
                        {from_where_clause6} 
                        order by {sort_by} {sort_dir} 
                        limit %(limit)s 
                    """,
                    params6)
        results6 = list(cur.fetchall())

    def get_random_series():
        global random_series_cache, cache_date

        # Check if the cache is empty or it's a new day
        if random_series_cache is None or cache_date != datetime.date.today():
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM movie")
                count = cur.fetchone()["count"]

                # Select a random offset
                random_offset = random.randint(0, count - 1)

                # Get the random series
                cur.execute("SELECT series_title FROM movie OFFSET %s LIMIT 1", (random_offset,))
                random_series_cache = cur.fetchone()["series_title"]

            cache_date = datetime.date.today()

        return random_series_cache

    # Get the random series
    random_series = get_random_series()

    # Manually setting what I want to display for MOTD
    with conn.cursor() as cur:

        # Director
        cur.execute("SELECT director AS motd_director FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_director = cur.fetchone()["motd_director"]

        # Year
        cur.execute("SELECT released_year AS motd_year FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_year = cur.fetchone()["motd_year"]

        # Poster
        cur.execute("SELECT poster_link AS motd_poster FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_poster = cur.fetchone()["motd_poster"]

        # Star1
        cur.execute("SELECT star1 AS motd_star1 FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_star1 = cur.fetchone()["motd_star1"]

        # Star2
        cur.execute("SELECT star2 AS motd_star2 FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_star2 = cur.fetchone()["motd_star2"]

        # Star3
        cur.execute("SELECT star3 AS motd_star3 FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_star3 = cur.fetchone()["motd_star3"]

        # Star4
        cur.execute("SELECT star4 AS motd_star4 FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_star4 = cur.fetchone()["motd_star4"]

        # Overview
        cur.execute("SELECT overview AS motd_overview FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_overview = cur.fetchone()["motd_overview"]

        # Rating
        cur.execute("SELECT imdb_rating AS motd_rating FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_rating = cur.fetchone()["motd_rating"]

        # Title
        cur.execute("SELECT series_title AS motd_title FROM movie WHERE series_title ILIKE %s", (f"%{random_series}%",))
        motd_title = cur.fetchone()["motd_title"]


    return render_template("home.html",
                           result_motd_title=motd_title,
                           result_random_series=random_series,
                           result_motd_director=motd_director,
                           result_motd_year=motd_year,
                           result_motd_poster=motd_poster,
                           result_motd_star1=motd_star1,
                           result_motd_star2=motd_star2,
                           result_motd_star3=motd_star3,
                           result_motd_star4=motd_star4,
                           result_motd_overview=motd_overview,
                           result_motd_rating=motd_rating
                           )


if __name__ == "__main__":
    app.run()

