import unittest
import mock
from check import check_maintainer_review, changed_paths


class TestMaintainerReview(unittest.TestCase):

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_non_maintainer(self, paths, reviewers):
        '''
        Only reviewer for a path is a non-maintainer.
        '''
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
        ]
        reviewers.return_value = ['non-maintainer@redhat.com']
        self.assertEqual(check_maintainer_review(), False)

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_maintainer(self, paths, reviewers):
        '''
        Reviewer for a path is a maintainer.
        '''
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
        ]
        reviewers.return_value = ['pkarampu@redhat.com']
        self.assertEqual(check_maintainer_review(), True)

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_architect(self, paths, reviewers):
        '''
        Top-level architect has reviewed.
        '''
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
        ]
        reviewers.return_value = ['jdarcy@redhat.com']
        self.assertEqual(check_maintainer_review(), (True, 'Architect Review'))

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_path_not_specified(self, paths, reviewers):
        '''
        Changed paths are not part of the pre-defined set of paths.
        '''
        paths.return_value = [
                'foo/bar/',
        ]
        reviewers.return_value = ['non-maintainer@redhat.com']
        self.assertEqual(check_maintainer_review(), None)

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_two_paths_one_acked(self, paths, reviewers):
        '''
        Two paths are defined and only one has maintainer ack.
        '''
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
                'xlators/features/bit-rot/src/bitd/bit-rot.c'
        ]
        reviewers.return_value = ['pkarampu@redhat.com']
        self.assertEqual(check_maintainer_review(), False)

    @mock.patch('check.get_reviewers')
    @mock.patch('check.changed_paths')
    def test_two_paths_one_acked_one_undefined(self, paths, reviewers):
        '''
        One of two paths is undefined, and the other has maintainer ack.
        '''
        paths.return_value = [
                'xlators/cluster/afr/src/afr-common.c',
                'foo/bar'
        ]
        reviewers.return_value = ['pkarampu@redhat.com']
        self.assertEqual(check_maintainer_review(), True)

