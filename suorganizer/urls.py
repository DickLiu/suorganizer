"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from .settings import base, production
from django.contrib import admin
from django.contrib.sitemaps.views import (
    index as site_index_view,
    sitemap as sitemap_view)

from blog import urls as blog_urls
from blog.feeds import (AtomPostFeed, Rss2PostFeed)
from contact import urls as contact_urls
from organizer.urls import (tag as tag_urls,
                            startup as startup_urls,)
from user import urls as user_urls
from .sitemaps import sitemaps as sitemaps_dict

from django.views.generic import RedirectView, TemplateView

admin.site.site_header = 'Startup Organizer Admin'
admin.site.site_title = 'Startup Organizer Site Admin'

sitenews = [
        url(r'^atom/$',
            AtomPostFeed(),
            name='blog_atom_feed'),
        url(r'^rss/$',
            Rss2PostFeed(),
            name='blog_rss_feed'),
        ]

urlpatterns = [
    url(r'^mimi/', admin.site.urls),
    url(r'^blog/', include(blog_urls) ), # blog_post_list or blog_post_detail
    url(r'^$', RedirectView.as_view(
        pattern_name='blog_post_list',
        permanent=False)),
    url(r'^contact/', include(contact_urls)),
    url(r'^sitemap\.xml$',
        site_index_view,
        {'sitemaps': sitemaps_dict,},
        name='sitemap'),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap_view,
        {'sitemaps': sitemaps_dict},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^sitenews/', include(sitenews)),
    url(r'^tag/', include(tag_urls)),
    url(r'^startup/', include(startup_urls)),
    url(r'^about/$', TemplateView.as_view(
        template_name='site/about.html'),
        name='about_site', ),
    url(r'^user/', include(
            user_urls,
            app_name='user',
            namespace='dj-auth')),
]

if production.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


