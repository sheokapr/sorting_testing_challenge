@pytest.fixture(scope='function', autouse=True)
def testcase_result(request):
    print("Test '{}' STARTED".format(request.node.nodeid))
    def fin():
        print("Test '{}' COMPLETED".format(request.node.nodeid))
        print("Test '{}' DURATION={}".format(request.node.nodeid,request.node.rep_call.duration))
    request.addfinalizer(fin)


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep