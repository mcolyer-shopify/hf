import unittest
from unittest.mock import patch
from hf.cli import Discussions, Tags

class TestDiscussions(unittest.TestCase):

    @patch('hf.cli.HfApi')
    def test_list_discussions(self, MockHfApi):
        mock_api = MockHfApi.return_value
        mock_api.get_repo_discussions.return_value = [
            type('Discussion', (object,), {'num': 1, 'title': 'Test Discussion', 'created_at': '2024-08-23T12:31:11-0700'})
        ]
        discussions = Discussions()
        discussions.list('org/repo')
        mock_api.get_repo_discussions.assert_called_once_with(repo_id='org/repo', discussion_status='open')

    @patch('hf.cli.HfApi')
    def test_close_discussion(self, MockHfApi):
        mock_api = MockHfApi.return_value
        discussions = Discussions()
        discussions.close('org/repo', 1)
        mock_api.change_discussion_status.assert_called_once_with(repo_id='org/repo', discussion_num=1, new_status='closed')

class TestTags(unittest.TestCase):

    @patch('hf.cli.HfApi')
    def test_list_tags(self, MockHfApi):
        mock_api = MockHfApi.return_value
        mock_api.list_repo_tags.return_value = [
            type('Tag', (object,), {'tag': 'v1.0', 'sha': 'abc123', 'message': 'Version 1.0'})
        ]
        tags = Tags()
        tags.list('org/repo')
        mock_api.list_repo_tags.assert_called_once_with(repo_id='org/repo')

if __name__ == '__main__':
    unittest.main()
