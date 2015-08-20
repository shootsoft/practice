__author__ = 'yinjun'

import os
import operator

from django.db import models

from factual import Factual
from factual.utils import circle

'''
FactualService call Factual API
'''
class FactualService:

    def __init__(self):
        '''
        Init the Facutal Service
        Prepare key and secret
        :return:
        '''
        if 'FACTUAL_KEY' not in os.environ or 'FACTUAL_SECRET' not in os.environ:
            raise ValueError('Missing Environment Variables: FACTUAL_KEY and FACTUAL_SECRET')
        else:
            self.factual = Factual(os.environ['FACTUAL_KEY'], os.environ['FACTUAL_SECRET'])
        #init country
        self.country = 'AU'

    def get_geo(self, location):
        '''
        parse the latitude,longitude data of the location
        :param location: name of the location
        :return: None or a geo data
        '''
        data = self.factual.table('world-geographies').filters(
            {'$and':
                 [
                     {'name':{'$eq': location}},
                     {'country':{'$eq': self.country}}
                 ]
            }
        ).select('latitude,longitude').data()

        if data != []:
            return data[0]
        else:
            return None

    def search(self, name, location, count=5, distance=5000):
        '''
        search the name around the location
        :param name: name of the places
        :param location: location name
        :param count: return count
        :param distance: default distance to the location
        :return: Factual places list or empty list
        :see http://developer.factual.com/api-docs/#full-text-search
        '''
        geo = self.get_geo(location)
        places = self.factual.table('places')
        data = []
        # if can not find the location, using general search
        if geo != None:
            data = places.search(name).geo(circle(geo['latitude'], geo['longitude'], distance)).limit(count).data()
        return data

    def recommend(self, location, group, count=5, distance=5000):
        '''
        Recommend places for a group of people
        :param name: name of places full-text search
        :param location: location name
        :param group: people
        :param count: return count
        :param distance: maximum distance
        :return:
        '''

        likes = dict()
        dislikes = dict()
        requirements = set()
        for p in group:
            if 'likes' in p:
                for l in p['likes']:
                    if l not in likes:
                        likes[l] = 1
                    else:
                        likes[l] += 1

            if 'dislikes' in p:
                for l in p['dislikes']:
                    if l not in dislikes:
                        dislikes[l] = 1
                    else:
                        dislikes[l] += 1

            if 'requirements' in p and p['requirements'] not in requirements:
                requirements.add(p['requirements'])

        for k,v in dislikes.items():
            if k in likes:
                del likes[k]

        likes_list =sorted(likes.items(), key=operator.itemgetter(1))
        likes_list.reverse()
        return self.recommend_with_condition(location, likes_list, dislikes.keys(), list(requirements), count, distance)




    def recommend_with_condition(self, location,
                                 likes=[], dislikes=[], requirements=[], count=5, distance=5000):
        '''
        Recommend the location for a group of people
        :param name: name of places full-text search
        :param location: name of the location
        :param likes: condition likes
        :param dislikes: condition dislikes
        :param requirements: condition requirements
        :param count: return count
        :param distance: maximum distance
        :return:
        '''
        geo = self.get_geo(location)
        places = self.factual.table('restaurants-au')
        common = [{'meal_lunch': True}, {'cuisine':{'$excludes_any': dislikes}}]
        data = []
        for r in requirements:
            common.append(self.convert_option(r))
        # if can not find the location, using general search
        if geo != None:
            # print requirements
            # print likes
            # print dislikes
            #starts from most like ones
            if len(likes) > 0:
                for like in likes:
                    data += places.geo(circle(geo['latitude'], geo['longitude'], distance)).filters(
                                    {
                                        '$and': [{'cuisine':{'$eq': like[0]}}] + common
                                    }).limit(5).data()


                        #}).limit(count - len(data)).data()
                    if len(data) == count:
                        break
            else:
                #or just go without dislikes
                data = places.geo(circle(geo['latitude'], geo['longitude'], distance)).filters(
                        {
                            '$and': common
                        }).limit(count).data()

        return data


    def convert_option(self, name):
        '''
        convert option to search condition
        :param name: name of the option
        :return: dict object
        '''
        return {'options_' + name.replace(' ', ''): True}