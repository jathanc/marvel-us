import webapp2
import jinja2
import os
from models import Movie
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import json
import urllib



the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/homepage.html')
        self.response.write(welcome_template.render())
        print("welcomeget")

    def post(self):
        print("WelcomePost")
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(welcome_template.render())


if(isset($_FILES['image'])){//Checks if file is set
  $errors= array();
  $file_name = $_FILES['image']['name'];
  $file_size =$_FILES['image']['size'];
  $file_tmp =$_FILES['image']['tmp_name'];
  $file_type=$_FILES['image']['type'];
  $file_ext=strtolower(end(explode('.',$_FILES['image']['name'])));
  //(above) checks file extension by getting text after last dot

  $expensions= array("jpeg","jpg","png");//supported file types

  if(in_array($file_ext,$expensions)=== false){//is the extension in the supported types
     $errors[]="extension not allowed, please choose a JPEG or PNG file.";
  }

  if($file_size > 2097152){//PHP only supports files under 2MB
     $errors[]='File size must be excately 2 MB';
  }

class ResultPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(welcome_template.render())
        print("resultget")

    def post(self):
        print("resultPost")
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(welcome_template.render())

 app = webapp2.WSGIApplication([
     ('/', WelcomePage),
     ('/result', ResultPage),
     ('/about', AboutPage),
 ], debug=True)
