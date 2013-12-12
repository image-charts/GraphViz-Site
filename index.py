import logging
import os
import webapp2
import jinja2

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname('resources/templates/')))

# Truly this is a silly function
def get_navigation_links(current):
  navs = [
    {'title': 'Home', 'url': '/', 'classes': ''},
    {'title': 'Documentation', 'url': '/documentation', 'classes': ''},
    #{'title': 'Examples', 'url': '/example', 'classes': ''},
    #{'title': 'Reference', 'url': '/reference', 'classes': ''},
    {'title': 'Make a Graph', 'url': '/graph', 'classes': ''},
    {'title': 'About this Site', 'url': '/about', 'classes': ''},
    {'title': 'Related Links', 'url': '/links', 'classes': ''},
    {'title': 'Contact Me', 'url': '/contact', 'classes': ''},
  ]

  for n in navs:
    if current == 'index' and n['title'] == 'Home':
      n['classes'] = 'current'
    if current in ['reference','example'] and n['title'] == 'Documentation':
      n['classes'] = 'current'
    if current in n['url']:
      n['classes'] = 'current'

  return navs

class StaticPageHandler(webapp2.RequestHandler):
  def get(self, name): 
    template_values = {}
    template_values['main_nav'] = get_navigation_links(name)
    template = jinja_environment.get_template('%s.html' % name)
    self.response.out.write(template.render(template_values))

class GraphPageHandler(webapp2.RequestHandler):
  def get(self, graph_id=None):
    pass

  def post(self):
    pass

APP = webapp2.WSGIApplication([
    webapp2.Route(r'/', StaticPageHandler, name='index', defaults={'name': 'index'}),
    webapp2.Route(r'/about', StaticPageHandler, name='about', defaults={'name': 'about'}),
    webapp2.Route(r'/contact', StaticPageHandler, name='contact', defaults={'name': 'contact'}),
    webapp2.Route(r'/links', StaticPageHandler, name='links', defaults={'name': 'links'}),
    webapp2.Route(r'/documentation', StaticPageHandler, name='documentation', defaults={'name': 'documentation'}),
    webapp2.Route(r'/example', StaticPageHandler, name='example', defaults={'name': 'example'}),
    webapp2.Route(r'/reference', StaticPageHandler, name='reference', defaults={'name': 'reference'}),
    webapp2.Route(r'/graph', GraphPageHandler, name='graph'),
], debug=True)

