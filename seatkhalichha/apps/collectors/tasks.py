import os
import facebook
from libs.url_shortener import UrlShortener
from apps.collectors.models import Collector_Contents, Collectors
from apps.carpools.models import Carpools
from apps.users.models import UserProfile


def grabOffers():
    """
    Grabs all offers from facebook page
    """
    collector = Collectors.objects.get(name='Facebook')
    shortener = UrlShortener()
    mytoken = os.environ.get('FB_PAGE_APP_TOKEN')
    graph = facebook.GraphAPI(access_token=mytoken)
    recent_posts = graph.request('183696891965171/feed/')
    posts = recent_posts['data']
    for post in posts:
        fb_content = Collector_Contents()
        if '#offer' in post['message']:
                gid_uid = post['id'].split('_')
                permalink = 'https://www.facebook.com/groups/{0}/permalink/{1}/'.format(gid_uid[0], gid_uid[1])
                short_url = shortener.get_short_url(dict(longUrl=permalink))
                fb_content.content = post
                fb_content.identifier = post['id']
                fb_content.permalink = permalink
                fb_content.shortlink = short_url
                fb_content.source = collector
                try:
                    fb_content.save()
                except Exception, e:
                    # this shall pass quietly
                    print "exists already!"
                    pass


def loadFBCarpool():
    """
    Load carpools from facebook onto system
    """
    contents = Collector_Contents.objects.filter(is_loaded=False)
    for content in contents:
        carpool = Carpools()
        try:
            message_clean = str(content.content['message'].replace('\n', ' '))
        except Exception, e:
            continue
        finally:
            content.is_loaded = True
            content.save()
        carpool.route = ''.join([str(x) for x in message_clean.split("#offer") if x != ''])
        # this driver is temporary, later it would be one of the admins
        carpool.driver = UserProfile.objects.get(phone="+9779802036633")
        carpool.tp_url = content.shortlink
        carpool.save()
