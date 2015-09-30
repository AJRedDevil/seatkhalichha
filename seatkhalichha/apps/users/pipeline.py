
import logging
from django.shortcuts import redirect

from social.pipeline.partial import partial

@partial
def update_user_details(strategy, details, user=None, is_new=False, *args, **kwargs):
    backend=kwargs.get('backend')
    if user and user.phone:
        return
    elif is_new:
        if not strategy.session_get('user_valid'):
            return redirect('fetch_info')
        else:
            details['phone']=strategy.session_get('phone')
            details['address']={
                    'streetaddress':strategy.session_get('streetaddress'), 
                    'city':strategy.session_get('city')
                }
            details['name']=strategy.session_get('name')
            details['email']=strategy.session_get('email')
            # details['displayname']=strategy.session_get('displayname')
            details['address_coordinates']=strategy.session_get('address_coordinates')
            return
            