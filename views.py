from django.conf import settings
from django.core.cache import cache
from django.views.generic.simple import direct_to_template

import random

def index(request):
    """Homepage"""
    
    session_key = random.getrandbits(256)
    private_key = random.getrandbits(256)
    cache.set(session_key, private_key)
    A = pow(settings.G, private_key, settings.P)
    print "session_key = %s\nprivate_key = %s\nA = %s" % (session_key, private_key, A)
    response = direct_to_template(
        request,
        'index.html',
        {   'p': settings.P,
            'g': settings.G,
            'A': A,
            'session_key': session_key
        }
    )
    return response

def finish_dh(request):
    """Get B and compute K"""
    B = long(request.POST['B'])
    ciphertext = request.POST['password']
    session_key = request.POST['session_key']
    private_key = cache.get(session_key)
    K = pow(B, private_key, settings.P)
    print "password = %s\nsession_key = %s\nprivate_key = %s\nB = %s\nK = %s" % (ciphertext, session_key, private_key, B, K)
    response = direct_to_template(
        request,
        'finished.html',
        {   'K': K,
            'ciphertext': ciphertext,
        }
    )
    return response
