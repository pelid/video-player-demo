from livereload import Server
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html'])
)


def render():

    template = env.get_template('index.html')

    html = template.render()

    with open('dist/index.html', 'w') as file:
        file.write(html)


server = Server()
render()  # should always render on startup before any source changes happens
server.watch('templates', render)
server.watch('dist')
server.serve(root='dist')