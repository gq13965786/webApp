import os.path
import torndb
import tornado.ioloop
import tornado.web
<<<<<<< HEAD
import common.libs as common
=======
>>>>>>> 3d067bfbe8cb4debb94cce1e91c280a494d7b360


class Application(tornado.web.Application):
    def __init__(self):
        handlers =[
        (r"/",HomeHandler),
        ]
        settings = dict(#settings
        template_path=os.path.join(os.path.dirname(__file__),"templates"),
        static_path=os.path.join(os.path.dirname(__file__),"static"),
        )
        super(Application,self).__init__(handlers,**settings)
        self.db =torndb.Connection(charset="utf8",max_idle_time=3600,connect_timeout=1000,
<<<<<<< HEAD
        host=common.MYSQL_HOST,database=common.MYSQL_DB,
        user=common.MYSQL_USER,password=common.MYSQL_PWD)
=======
        host="localhost:3306",database="stock_data",
        user="root",password="password")
>>>>>>> 3d067bfbe8cb4debb94cce1e91c280a494d7b360
        #self.db.query("CREATE TABLE `stock_data`.`authors` (id INT,name VARCHAR(20),email VARCHAR(20))")
        #no iterable

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    port = 8888
    print("start web application at port:8888")
    http_server.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
