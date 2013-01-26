#! /usr/bin/python

from bottle import route, run, view, static_file, url, request
from bottle import jinja2_template as template
import datetime
import sqlite3
import urllib2
from BeautifulSoup import BeautifulSoup





DATABASE = 'song_tracker.db'
INDEX = 'static/index.tpl'
VHOST = "79.133.201.94" #orion.shellmix.com
PORT=1881


def add_to_sqlite(artist,song,date_added,link):
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("insert into songs (artist,song,date_added,link) values ('"+str(artist)+"','"+str(song)+"','"+str(date_added)+"','"+str(link)+"');")
  conn.commit()
  cur.close()
  
def get_youtube_title(link):
  #<meta property="og:title" content="Mac Miller - Thoughts From A Balcony">
  #self.title = soup.find('meta', {'property' : 'og:title'})['content']
  html = urllib2.urlopen(link)
  soup = BeautifulSoup(html)
  title = soup.find('meta', attrs={'property':'og:title'})['content']
  return title
  
  
@route('/static/:filename#.*#')
def server_static(filename):
    return static_file(filename, root='static/')

@route('/')
@route('/add')
def add():
  form = '<form method="POST">'
  form += '<table><tr><td>Artist</td><td><input name="artist" type="text" /></td></tr>'
  form += '<tr><td>Song</td><td><input name="song" type="text" /></td></tr>'
  form += '<tr><td>Link</td><td><input name="link" type="text" /></td></tr>'
  form += '<tr><td></td><td><input type="submit" value="Submit" /></td></table>'
  form += '</form>'
  title = 'Add a song'
  return template(INDEX,content=form,title=title)
  
@route('/', method='POST')
@route('/add', method='POST')
def added():
  artist = request.forms.artist
  song = request.forms.song
  date_added = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
  link = request.forms.link
  add_to_sqlite(artist,song,date_added,link)
  title = 'Song added'
  content = artist + ': ' + song + ' ('+date_added+')' + '<a target="_blank" href="'+link+'">link</a>'
  content += '<br/>'
  content += '<a href="/add">Add another song</a>'
  return template(INDEX,title=title,content=content)
  
@route('/view')
def view():
  title = 'View all songs'
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("select * from songs where visible is null order by id;")
  content = '<table class="view"><tr><td>ID</td><td>Artist</td><td>Song</td><td>Date added</td><td><img src="static/img/youtube.png" height="32" width="32" /></td><td>Edit</td><td>Done</td></tr>'
  for row in cur:
    content += '<tr><td>'+str(row[0])+'</td><td>'+row[1]+'</td><td>'+row[2]+'</td><td>'+row[3]+'</td><td><a target="_blank" href="'+unicode(row[4])+'">'+get_youtube_title(row[4])+'</a></td><td><a href="/edit/'+str(row[0])+'"><img height="32" width="32" src="static/img/edit-icon.png" /></a></td><td><a href="/done/'+str(row[0])+'"><img src="/static/img/done.png" height="32" width="32" /></a></td></tr>'
  content += '</table>'
  
  return template(INDEX,title=title,content=content)
  
@route('/edit/:id')
def edit(id):
  title = "Edit "+id
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("select * from songs where id="+id+";")
  content = '<form method="POST"><table>'
  for row in cur:
    content += '<tr><td>Artist</td><td><input name="artist" type="text" value="'+row[1]+'" /></td></tr>'
    content += '<tr><td>Song</td><td><input name="song" type="text" value="'+row[2]+'" /></td></tr>'
    content += '<tr><td>Date added</td><td><input name="date_added" type="text" value="'+row[3]+'" /></td></tr>'
    content += '<tr><td>Link</td><td><input name="link" type="text" value="'+row[4]+'" /></td></tr>'
  content += '<tr><td></td><td><input type="submit" value="Submit" /></td></tr></table></form>'
  cur.close()
  return template(INDEX, title=title, content=content)
  
@route('/edit/:id', method='POST')
def edit(id):
  title = "Succesfully edited "+id
  artist = request.forms.artist
  song = request.forms.song
  date_added = request.forms.date_added
  link = request.forms.link
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("update songs set artist='"+artist+"',song='"+song+"',date_added='"+date_added+"',link='"+link+"' where id="+id+";")
  conn.commit()
  cur.close()
  content = '<table class="view"><tr><td>ID</td><td>Artist</td><td>Song</td><td>Date added</td><td>Link</td></tr>'
  content += '<tr><td>'+id+'</td><td>'+artist+'</td><td>'+song+'</td><td>'+date_added+'</td><td><a target="_blank" href="'+link+'">'+song+'</a></td></tr></table><br/>'
  content += '<a href="/view">Back to view</a>'
  return template(INDEX, title=title, content=content)

@route('/done/:id')
def done(id):
  title='Done '+id
  content = "Status is set to invisible. <br/>"
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("update songs set visible='false' where id="+id+";")
  conn.commit()
  cur.close()
  content += '<a href="/view">Back to view</a>'
  return template(INDEX, title=title, content=content)

run(host='localhost',port=8080,debug=True)
#run(port=PORT, host=VHOST, debug=True)
#url='http://www.youtube.com/watch?v=nxufWf7dEcM&feature=g-all-u&context=G2c880eaFAAAAAAAAAAA'
#get_youtube_title(url)
