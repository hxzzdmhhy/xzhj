import time
from django.db import connection
from django.shortcuts import render

# Create your views here.
import MySQLdb
import MySQLdb.cursors
import datetime
DB_HOST='localhost'
DB_NAME_MYSQL='zsky'
DB_PORT_MYSQL=3306
DB_NAME_SPHINX='film'
DB_PORT_SPHINX=9306
DB_USER='root'
DB_PASS='123456'
DB_CHARSET='utf8mb4'


def get_cursor():
    return connection.cursor()


def index(request):
    curosr = get_cursor()
    curosr.execute('select id,name,author from book')
    books = curosr.fetchall()
    context = {
        'books': books
    }
    return render(request, '../templates/index.html')

thisweek = int(time.mktime(datetime.datetime.now().timetuple())) - 86400 * 7

def weekhot():

    return render('weekhot.html')


def new():

    return render('new.html')



def tag():
    return render('tag.html')



def index():

    return render_template('index.html', form=form, keywords=keywords, total=total, today=today, sitename=sitename)





def search_results(query, page=1):

    return render('list.html')



def search_results_bylength(query, page=1):

    return render('list_bylength.html')



def search_results_bycreate_time(request, page=1):


    return render('list_bycreate_time.html')


@app.route('/main-search-kw-<query>-requests-<int:page>.html', methods=['GET', 'POST'])
# @cache.cached(timeout=60*60,key_prefix=make_cache_key)
def search_results_byrequests(query, page=1):

    return render('list_byrequests.html')


@app.route('/hash/<info_hash>.html', methods=['GET', 'POST'])
# @cache.cached(timeout=60*60,key_prefix=make_cache_key)
def detail(info_hash):
    conn, curr = sphinx_conn()
    querysql = 'SELECT * FROM film WHERE info_hash=%s'
    curr.execute(querysql, [info_hash])
    result = curr.fetchone()
    sphinx_close(curr, conn)
    # hash=Search_Hash.query.filter_by(id=id).first()
    if not result:
        return redirect(url_for('index'))
    fenci_list = jieba.analyse.extract_tags(result['name'], 4)
    tags = Search_Tags.query.order_by(Search_Tags.id.desc()).limit(20)
    form = SearchForm()
    return render_template('detail.html', form=form, tags=tags, hash=result, fenci_list=fenci_list, sitename=sitename)


@app.route('/sitemap.xml')
def sitemap():
    conn, curr = sphinx_conn()
    querysql = 'SELECT info_hash,create_time FROM film order by create_time desc limit 100'
    curr.execute(querysql)
    rows = curr.fetchall()
    sphinx_close(curr, conn)
    sitemaplist = []
    for row in rows:
        info_hash = row['info_hash']
        mtime = datetime.datetime.fromtimestamp(int(row['create_time'])).strftime('%Y-%m-%d')
        url = domain + 'hash/{}.html'.format(info_hash)
        url_xml = '<url><loc>{}</loc><lastmod>{}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>'.format(
            url, mtime)
        sitemaplist.append(url_xml)
    xml_content = '<?xml version="1.0" encoding="UTF-8"?><urlset>{}</urlset>'.format("".join(x for x in sitemaplist))
    with open('static/sitemap.xml', 'wb') as f:
        f.write(xml_content)
        f.close()
    return send_from_directory(app.static_folder, request.path[1:])









def notfound(e):
    return render("404.html")
