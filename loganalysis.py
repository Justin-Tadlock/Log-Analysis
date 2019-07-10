#!/usr/bin/env python3
# Log Analysis Project.

import psycopg2

# Query the database using the query string passed in.
# Returns the query result set if the query is successful,
#  a null query result set otherwise.
def get_query_result_set(query):
    query_result_set = None;

    try:
        dbConn = psycopg2.connect('dbname=news')
    except Exception as e:
        dbConn = None;
        print('Error -- Could not connect to the database')

    if dbConn is not None:
        cursor = dbConn.cursor()
        cursor.execute(query);
        query_result_set = cursor.fetchall()
        dbConn.close()

    return query_result_set 

# Method for collecting the most popular articles of all time
# Returns the query results
def get_top_three_articles_all_time():
    query = (
        "select "
        "  articles.title, count(log.path) as views "
        "from "
        "  log left join articles "
        "on "
        "  log.path like '%' || articles.slug || '%' "
        "where "
        "  articles.title is not null "
        "group by "
        "  articles.title "
        "order by "
        "  views desc;"
    )

    return get_query_result_set(query)

# Method for collecting the most popular authors of all time
# Returns the query results
def get_most_popular_authors_all_time():
    query = (
        "select "
        "  authors.name, "
        "  count(log.path) as views "
        "from "
        "  authors, "
        "  articles left join log on log.path like '%' || "
        "  articles.slug || '%' "
        "where "
        "  authors.id = articles.author "
        "group by "
        "  authors.name, articles.author "
        "order by "
        "  views desc;"
    )

    return get_query_result_set(query)

# Method for collecting the days where more
#   than 1% of the requests resulted in errors
# Returns the query results
def get_days_high_error_requests():
    query = (
        "select "
        "  to_char(total.time::date, 'Month DD, YYYY') as day, "
        "  to_char((err.status / total.status::float) * 100, "
        "          '999.00') as err_percent "
        "from "
        "  (select log.time::date, count(log.status) as status "
        "   from log group by log.time::date, status) as total "
        "join "
        "  (select log.time::date, count(log.status) as status "
        "   from log where log.status != '200 OK' "
        "   group by log.time::date, status) as err "
        "on "
        "  total.time::date = err.time::date "
        "where "
        "  total.status != err.status "
        "group by "
        "  total.time::date, err.status, total.status "
        "having "
        "  err.status / total.status::float * 100 > 1.0;"
    )
    
    return get_query_result_set(query)


# Begin the script to start printing out the data from the database
print("Welcome to Log Analysis\n")

print("What are the most popular top three articles of all time?")
top_articles = get_top_three_articles_all_time()
if top_articles is not None:
    for result in enumerate(top_articles):
        title = result[1][0]
        views = result[1][1]
        print("   %-35s --- %6d views" % (title, views))
else:
    print("Error -- The query returned a null result set\n")

print("\nWho are the most popular authors of all time?")
rank_popular_authors = get_most_popular_authors_all_time()
if rank_popular_authors is not None:
    for result in enumerate(rank_popular_authors):
        author = result[1][0]
        views = result[1][1]
        print("   %-25s --- %6d views" % (author, views))
else:
    print("Error -- The query returned a null result set\n")

print("\nOn which days did more than 1% of requests result in errors?")
day_high_err_request = get_days_high_error_requests()
if day_high_err_request is not None:
    for result in enumerate(day_high_err_request):
        day = result[1][0]
        percent = float(result[1][1])
        print("   %s --- %6.2f%% errors" % (day, percent))
else:
    print("Error -- The query returned a null result set\n")
