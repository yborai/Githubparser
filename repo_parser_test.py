import unittest
from unittest.mock import patch

from repo_parser import get_repos, get_commit_count

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

@patch('repo_parser.get_repos')
def mock_get_repos(self, username):
    repos = [
        'ATTCodingChallenge', 'CodingChallengeATT', 'Githubparser',
        'Hello-World', 'helloworld', 'proj_euler', 'quaxo',
        'Triangle567', 'triangle_test', 'zephyr'
    ]

    return(repos)

@patch('repo_parser.get_commit_count')
def mock_get_commit_count(self, username, repo):
    commits = {
        "ATTCodingChallenge": 2,
        "CodingChallengeATT": 2,
        "Githubparser": 3,
        "Hello-World": 1,
        "helloworld": 4,
        "proj_euler": 30,
        "quaxo": 14,
        "Triangle567": 4,
        "triangle_test": 1,
        "zephyr": 30
    }

    return commits[repo]

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRepos(self): 
        self.assertEqual(mock_get_repos('yborai')[-1],'zephyr','First repo created should be zephyr')

    def testCommits(self): 
        self.assertEqual(get_commit_count('yborai', 'helloworld'), 4, 'Response should be 4.')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()