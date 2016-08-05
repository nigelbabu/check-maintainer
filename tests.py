import unittest
import mock
from check import check_maintainer_review, changed_paths


class TestMaintainerReview(unittest.TestCase):

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_non_maintainer(self, paths, reviewers):
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
        ]
        reviewers.return_value = ['non-maintainer@redhat.com']
        self.assertEqual(check_maintainer_review(), False)

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_maintainer(self, paths, reviewers):
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
        ]
        reviewers.return_value = ['pkarampu@redhat.com']
        self.assertEqual(check_maintainer_review(), True)

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_architect(self, paths, reviewers):
        changed_paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
        ]
        reviewers.return_value = ['jdarcy@redhat.com']
        self.assertEqual(check_maintainer_review(), (True, 'Architect Review'))
