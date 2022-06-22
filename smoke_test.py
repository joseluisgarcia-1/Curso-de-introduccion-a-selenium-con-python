from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assetions import AssertionTest
from searchtests import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, search_test])
kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)