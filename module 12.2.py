from unittest import TestCase
from test12 import Runner, Tournament

class  TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)

    def test_first_tour(self):
        tournament = Tournament(90,self.first, self.third)
        res = tournament.start()
        TournamentTest.all_result.append(res)
        self.assertTrue(res[2] == 'Ник')

    def test_second_tour(self):
        tournament = Tournament(90,self.second, self.third)
        res = tournament.start()
        TournamentTest.all_result.append(res)
        self.assertTrue(res[2] == 'Ник')

    def test_third_tour(self):
        tournament = Tournament(90,self.first, self.second, self.third)
        res = tournament.start()
        TournamentTest.all_result.append(res)
        self.assertTrue(res[3] == 'Ник')


    @classmethod
    def tearDownClass(cls):
        for k, v in enumerate(cls.all_results):
            print(f'{k+1}: {v}')
