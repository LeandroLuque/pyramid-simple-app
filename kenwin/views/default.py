from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget

from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from ..security import check_password

from sqlalchemy.exc import DBAPIError

from ..models import User



@view_defaults(renderer='../templates/mytemplate.jinja2')
class AplicacionViews:

    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='login', renderer='../templates/login.jinja2')
    def login(self):
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'  # never use login form itself as came_from
        came_from = '/'
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            query = self.request.dbsession.query(User)
            hashed_pw = query.filter(User.name == login).first().password
            if hashed_pw and check_password(password, hashed_pw):
                headers = remember(request, login)
                return HTTPFound(location=came_from,
                                 headers=headers)

        return dict(
            url=request.application_url + '/login',
            came_from=came_from,
            login='',
            password='',
        )

    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('home')
        return HTTPFound(location=url,
                         headers=headers)


    @view_config(route_name='home')
    def home(self):
        return {}



