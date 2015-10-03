
import logging
from django.shortcuts import redirect
from django.core.validators import ValidationError
from apps.users.models import UserProfile

from social.pipeline.partial import partial


@partial
def update_user_details(strategy, details, user=None, is_new=False, *args, **kwargs):
    backend=kwargs.get('backend')
    if user and user.phone:
        return

    if backend.name == 'twitter':
        logging.warn(strategy)
        if is_new:
            required_fields = [ 'name', 'phone' ,'email']
            if not strategy.session_get('user_valid'):
                return redirect('fetch_info')
            else:
                for field in required_fields:
                    logging.warn(strategy.session_get(field))
                    details[field] = strategy.session_pop(field)
                # details['address']={
                #         'streetaddress':strategy.session_get('streetaddress'),
                #         'city':strategy.session_get('city')
                #     }
                # details['name']=strategy.session_get('name')
                # details['displayname']=strategy.session_get('displayname')
                # details['address_coordinates'] = strategy.session_get(
                #     'address_coordinates')
                return

    if backend.name == 'facebook':
        if UserProfile.objects.filter(email=details.get('email')):
            # raise ValidationError({'email': ["Email exists already!", ]})
            return redirect('signin')
        if is_new:
            required_fields = ['name', 'phone']
            if not strategy.session_get('user_valid'):
                return redirect('fetch_info')
            else:
                for field in required_fields:
                    details[field] = strategy.session_pop(field)
                # details['address']={
                #         'streetaddress':strategy.session_get('streetaddress'),
                #         'city':strategy.session_get('city')
                #     }
                # details['name']=strategy.session_get('name')
                # details['email']=strategy.session_get('email')
                # details['displayname']=strategy.session_get('displayname')
                # details['address_coordinates'] = strategy.session_get(
                #     'address_coordinates')
                return