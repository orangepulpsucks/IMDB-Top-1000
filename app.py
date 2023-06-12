import csv
from flask import Flask, request, render_template
import psycopg2, random

from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

# TEMPLATE
# @app.route("/about")
#  def render_sets4():
#     return render_template("about.html")
# Note: "render_sets#" are buggy so just choose one that isn't buggy

@app.route("/about")
def render_sets4():
    return render_template("about.html")

@app.route("/browse-by-directors")
def render_sets11():
    return render_template("browse-by-dir.html")

@app.route("/browse-by-category")
def render_sets6():
    return render_template("browse-by-cat.html")

@app.route("/category-by-year")
def render_sets9():
    return render_template("by-year.html")

@app.route("/category-by-genre")
def render_sets8():
    return render_template("by-genre.html")



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
def render_sets3():
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

    from_where_clause3 = """
        from movie
        where %(series_title)s is null or series_title ilike %(series_title)s
        and ( %(released_year)s is null or released_year = %(released_year)s )
        and ( %(runtime)s is null or runtime = %(runtime)s )
        and ( %(genre)s is null or genre ilike %(genre)s )
        and ( %(imdb_rating)s is null or imdb_rating = %(imdb_rating)s )
        and ( %(director)s is null or director ilike %(director)s )
    """

    params3 = {
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

    def get_sort_dir3(col):
        if col== sort_by:
            return "desc" if sort_dir == "asc" else "asc"
        else:
            return "asc"
        
    with conn.cursor() as cur:
        cur.execute(f"""select series_title, released_year, runtime, genre, imdb_rating, director, poster_link, certificate, overview, meta_score, star1, star2, star3, star4, no_of_votes, gross 
                        {from_where_clause3} 
                        order by {sort_by} {sort_dir} 
                        limit %(limit)s 
                    """,
                    params3)
        results3 = list(cur.fetchall())  
       
        # Select a random movie name from the results
        random_series = random.choice(results3)


    return render_template("home.html",
                           result_random_series=random_series, 
                           params3=request.args
                           )
 