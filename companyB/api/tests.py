import os

from django.test import TestCase
from factual import Factual
from .models import FactualService
# Create your tests here.

class FactualTests(TestCase):

    def setUp(self):
        try:
            self.factualService = FactualService()
            #print 'Environment Variable Pass'
        except ValueError as err:
            #print(err.args)
            self.fail(err.args)

    def test_get_geo(self):
        '''
        Test how to convert location in to geo
        :return:
        '''
        geo = self.factualService.get_geo('Woolloomooloo')
        self.assertEqual(True, 'latitude' in geo)
        self.assertEqual(True, 'longitude' in geo)

        self.assertEqual(-33.869068, geo['latitude'])
        self.assertEqual(151.219788, geo['longitude'])
        #print geo


        empty = self.factualService.get_geo('XYZABC')
        self.assertEqual(None, empty)
        #print empty


    def test_search(self):

        data = self.factualService.search('coffee', 'Woolloomooloo')
        self.assertEqual(True, data != [])
        #print data

        data = self.factualService.search('coffee', 'XYZABC')
        self.assertEqual(True, data == [])
        #print data

    # def test_recommend2(self):
    #     factual = Factual(os.environ['FACTUAL_KEY'], os.environ['FACTUAL_SECRET'])
    #     places = factual.table('restaurants-au')
    #     data = places.filters(
    #                 {
    #                     '$and':
    #                         [
    #                             {'meal_lunch': True},
    #                             {'cuisine':{'$includes_any': requirements}},
    #                             {'cuisine':{'$includes_any': list(likes)}},
    #                             {'cuisine':{'$excludes_any': list(dislikes)}}
    #                         ]
    #                 }).limit(5).data()
    #     print data
    def test_recommend(self):

        data = self.factualService.recommend('Surry Hills',
                [
                    {
                        "name": "Bob",
                        "title": "executive",
                        "likes": [
                            "indian",
                            "chinese",
                            "malaysian"
                        ],
                        "dislikes": [
                            "Australian"
                        ],
                        "requirements": "gluten free"
                    },
                    {
                        "name": "Jose",
                        "title": "developer",
                        "likes": [
                            "indian",
                            "chinese"
                        ],
                        "dislikes": [
                            "thai"
                        ]
                    },
                    {
                        "name": "Aloysia",
                        "title": "evangelist",
                        "likes": [
                            "chinese"
                        ],
                        "dislikes": [
                            "Australian"
                        ],
                        "requirements": "gluten free"
                    }
                ])
        self.assertEqual(True, data != [])
       # print data