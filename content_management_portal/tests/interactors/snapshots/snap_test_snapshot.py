# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_mything_when_both_positive_values gpg_response'] = 13

snapshots['test_mything_when_both_float_values gpg_response'] = 13.0

snapshots['test_mything_when_both_negative_values gpg_response'] = -13

snapshots['test_mything_when_both_positive_and_negative_given gpg_response'] = 1
