#!/usr/bin/env python
import yaml


# Get the paths that were changed
def changed_paths():
    return []


# Get people who gave Code-Review:+1
def get_reviewers():
    return []


# Get maintainer information
def get_maintainer_info():
    with open('maintainer.yml') as f:
        return yaml.load(f)


def check_maintainer_review():
    paths = changed_paths()
    reviewers = get_reviewers()
    maintainers = get_maintainer_info()
    # In case an architect has reviewed, return True immediately
    if len(set(reviewers).intersection(maintainers['paths']['/'])) > 0:
        return True, 'Architect Review'
    review_status = {}
    for p in paths:
        for i in xrange(0, len(p.split('/'))):
            defined_path = '/'.join(p.split('/')[:i])
            if defined_path in maintainers['paths']:
                if len(set(reviewers).intersection(maintainers['paths'][defined_path])) > 0:
                    review_status[defined_path] = True
                else:
                    review_status[defined_path] = False
    # If any paths do not have reviewer ack fail
    if False in review_status.values():
        return False
    # If all paths have reviewer ack and
    if False not in review_status.values() and len(review_status) > 0:
        return True
