import unittest

from repo_parser import get_repos, get_commit_count

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRepos(self): 
        self.assertEqual(get_repos('yborai')[-1],'zephyr','First repo created should be zephyr')

    def testCommits(self): 
        self.assertEqual(get_commit_count('yborai', 'helloworld'), 4, 'Response should be 4.')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()