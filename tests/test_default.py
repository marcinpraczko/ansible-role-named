import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_named_running_and_enabled(Service):
    named = Service("named")
    assert named.is_running
    # assert named.is_enabled


def test_included_conf_file(File):
    f = File('/etc/named/included.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'named'
