# coding: utf-8

from django.urls import path, re_path
from backend.api.views.tweets import *
from backend.api.views.tweet_pics import *
from backend.api.views.statistics import *


urlpatterns = [
    path('statistics/file/<str:resource>/', geo_file_router),
    path('tweet/pic/<str:resource>/', tweet_pic_router),
    path('tweet/pic/', tweet_pic_router),
    path('tweet/untrained/<int:resource>/', tweet_untrained_router),
    path('tweet/untrained/', tweet_untrained_router),
    path('tweet/untrained/text/<int:resource>/', tweet_untrained_text_router),
    path('tweet/untrained/text/', tweet_untrained_text_router),
    path('tweet/untrained/zone/<int:resource>/', tweet_untrained_zone_router),
    path('tweet/untrained/zone/', tweet_untrained_zone_router),
    path('tweet/untrained/zone/vic/<int:resource>/', tweet_untrained_zone_vic_router),
    path('tweet/untrained/zone/vic/', tweet_untrained_zone_vic_router),
    path('tweet/trained/', tweet_trained_router),
    path('tweet/trained/text/', tweet_trained_text_router),
    path('tweet/trained/zone/', tweet_trained_zone_router),
    path('tweet/trained/zone/vic/', tweet_trained_zone_vic_router),
    path('tweet/', tweet_router),
    path('tweet/<str:resource>/', tweet_router),
    path('statistics/time/', statistics_time_router),
    path('statistics/track/random/', statistics_track_router),
    path('statistics/track/random/<int:number>/', statistics_track_router),
    path('statistics/track/<str:user_id>/', statistics_track_router),
    path('statistics/text/', statistics_text_router),
    path('statistics/machine/', statistics_machine_router),
    path('statistics/vic/zone/', statistics_zone_vic_router),
    path('statistics/vic/zone/<str:zone>/', statistics_zone_vic_router),
    path('statistics/zone/', statistics_zone_router),
    path('statistics/zone/<str:zone>/', statistics_zone_router),
]
