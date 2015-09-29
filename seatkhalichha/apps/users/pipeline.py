
import logging
from django.shortcuts import redirect

from social.pipeline.partial import partial

@partial
def update_user_details(strategy, details, user=None, is_new=False, *args, **kwargs):
    backend=kwargs.get('backend')
    if user and user.phone:
        return
    elif is_new and not details.get('phone'):
        phone=strategy.request_data().get('phone')

        if phone:
            details['phone']=phone
            details['address']={
                    'streetaddress':strategy.request_data().get('streetaddress'), 
                    'city':strategy.request_data().get('city')
                }
            details['name']=strategy.request_data().get('name')
            details['address_coordinates']=strategy.request_data().get('address_coordinates')
        else:
            return redirect('fetch_info')