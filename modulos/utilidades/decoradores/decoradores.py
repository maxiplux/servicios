# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404,HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.conf import settings





def validar_rol(function=None, home_url=None, redirect_field_name=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if request.user.is_authenticated():
                perfil=request.user.get_profile()
                if not 'perfil_registro' in request.session:
                    if perfil.rol_id == 1:
                        return HttpResponseRedirect('/contenidos/mis-grupos/')

                    return HttpResponseRedirect('/contenidos/reglas/asignacion/%s/'%perfil.id)

                #return HttpResponseRedirect('/contenidos/salir/')
                    
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view
    if function is None:
        return _dec
    else:
        return _dec(function)


def registro_incompleto(function=None, home_url=None, redirect_field_name=None):
    def _dec(view_func):
        
        def _view(request, *args, **kwargs):
            
            try:
                perfil = Perfil.objects.get(user=request.user)
            except Perfil.DoesNotExist:
                request.session.flush()
                logout(request)
                return HttpResponseRedirect(reverse('login'))


            
            if perfil.segundo_paso_imcompleto():
                messages.warning(request, 'No has culminado todos los pasos tu registro, te invitamos a que termines de registrarte')
                return HttpResponseRedirect(reverse('second_step'))
            
            elif perfil.tercer_paso_imcompleto():            
                messages.warning(request, 'No has culminado todos los pasos tu registro, te invitamos a que termines de registrarte')
                return HttpResponseRedirect(reverse('third_step'))
            
            elif perfil.cuarto_paso_imcompleto():
                messages.warning(request, 'No has culminado todos los pasos tu registro, te invitamos a que termines de registrarte')
                return HttpResponseRedirect(reverse('fourth_step'))
                    
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view
    if function is None:
        return _dec
    else:
        return _dec(function)
# consulta las investigaciones disponibles para un perfil
def consultar_investigacion(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                if 'presento_encuesta' not in request.session.keys():
                        investigacion=Investigacion.objects.get_encuesta(request.user.get_profile())
                        if investigacion:
                            request.session['presento_encuesta'] = 1
                            return HttpResponseRedirect(reverse('resolver_investigacion', args=[investigacion[0].id ]))

                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap


def ajax_requerido(function=None, home_url=None, redirect_field_name=None):
    def _dec(view_func):
        
        def _view(request, *args, **kwargs):            
            if not request.is_ajax():
                raise Http404        
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view
    if function is None:
        return _dec
    else:
        return _dec(function)
        
# esto solo validad la session y genera un mensaje no podemos redirecionar en ajax
# esto es para usar funciones que requieran de ajax
def session_validad(function=None, home_url=None, redirect_field_name=None):
    def _dec(view_func):
        
        def _view(request, *args, **kwargs):
            if not (request.user.is_authenticated()) :
                return HttpResponse("FALLO DE SESSION")            
            
                    
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view
    if function is None:
        return _dec
    else:
        return _dec(function)

# agregar pagina de exepcion de seguridad
def es_admin(function=None, home_url=None, redirect_field_name=None):
    def _dec(view_func):        
        def _view(request, *args, **kwargs):
            if not (request.user.is_authenticated) :
                if (request.user.is_superuser):
                    return HttpResponseRedirect('/admin/')            
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view
    if function is None:
        return _dec
    else:
        return _dec(function)        
        
def agencia_login_required(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                if '_auth_user_id' not in request.session.keys():
                        return HttpResponseRedirect(reverse('cliente_login'))
                        
                if Vendedor.objects.filter(user__id=request.user.id).count()!= 0  or Cliente.objects.filter(user__id=request.user.id).count()!= 0 or Perfil.objects.filter(user=request.user).count()!= 0:
                    if request.user.is_authenticated():
                        logout(request)
                    return HttpResponseRedirect(reverse('cliente_login'))
                        
                        
                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap

def vendedor_login_required(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login pagagencia/agencia-login/e
                if '_auth_user_id' not in request.session.keys():
                        return HttpResponseRedirect(reverse('cliente_login'))
                        
                        
                if Cliente.objects.filter(user__id=request.user.id).count()!= 0  or Agencia.objects.filter(user__id=request.user.id).count()!= 0 or Perfil.objects.filter(user=request.user).count()!= 0:
                    if request.user.is_authenticated():
                        logout(request)
                    return HttpResponseRedirect(reverse('cliente_login'))   
                
                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap

def cliente_login_required(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                if '_auth_user_id' not in request.session.keys():
                    return HttpResponseRedirect(reverse('cliente_login'))
                    
                if Perfil.objects.filter(user__id=request.user.id).count()!= 0:
                    if request.user.is_authenticated():
                        logout(request)
                    return HttpResponseRedirect(reverse('cliente_login'))                  
                       
                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap

def cliente_login_required_premiopromocional(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                if '_auth_user_id' not in request.session.keys():
                    return HttpResponseRedirect(reverse('cliente_login_premiopromocional'))

                if Perfil.objects.filter(user__id=request.user.id).count()!= 0:
                    if request.user.is_authenticated():
                        logout(request)
                    return HttpResponseRedirect(reverse('cliente_login_premiopromocional'))

                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap

def no_admin_user(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page
                user_id = str(request.user.id)
                query = """
                            SELECT 1 FROM DUAL WHERE 
                            EXISTS ( SELECT 1 from agencia_agencia WHERE agencia_agencia.user_id=""" + user_id + """)
                            or 
                            EXISTS ( SELECT 1 from cliente_cliente WHERE cliente_cliente.user_id=""" + user_id + """)
                            or 
                            EXISTS ( SELECT 1 from agencia_vendedor WHERE agencia_vendedor.user_id=""" + user_id + """)
                            OR
                            EXISTS (SELECT 1 from auth_user where auth_user.is_staff = 1 and auth_user.id=""" + user_id + """)
                            LIMIT  1
                        """                
                #cursor = connection.cursor()
                #cursor.execute(query)
                #rows = cursor.fetchall()
                #if rows:
                 #   if request.user.is_authenticated():
                  #      logout(request)
                   # return HttpResponseRedirect(reverse('login'))
                       
                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap

def navegador_autorizado(string ):
    #request.META['HTTP_USER_AGENT'].find('MSIE') > 0:
    if (len( re.findall('((Mozilla/4\.75)|(Netscape6)|(Mozilla/4\.08)|(Mozilla/4\.5)|(Mozilla/4\.6)|(Mozilla/4\.79)|MSIE 7\.[0-9]+)|(MSIE 6\.[0-9]+)|(MSIE 5\.[0-9]+)|(MSIE 4\.[0-9]+)', string )) != 0):
        return False
    return True


def validar_navegador(function):
        def wrap(request, *args, **kwargs):
                #this check the session if userid key exist, if not it will redirect to login page                
                if not navegador_autorizado(request.META['HTTP_USER_AGENT']):     
                    return HttpResponseRedirect(reverse('navegadores'))                
                       
                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap
    
def fin_juego(function):
        def wrap(request, *args, **kwargs):
                from datetime import datetime
                from django.contrib.auth import logout
                fecha_actual = datetime.now()                                
                if fecha_actual > settings.HORA_FIN_JUEGO and fecha_actual < settings.HORA_INICIO_JUEGO:
                    logout()
                    print request.user.is_authenticated()
                    return HttpResponseRedirect(reverse('login'))                    
                else:
                    request.session.set_expiry(None)              
                       
                return function(request, *args, **kwargs)
        wrap.__doc__=function.__doc__
        wrap.__name__=function.__name__
        return wrap
