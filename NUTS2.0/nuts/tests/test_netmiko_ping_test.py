import pytest
import nuts.testcreation.concretetests.netmiko_ping_test as pingtest


class TestNetmikoPingTest:
    @pytest.mark.parametrize(
        "platform, hostname, username, password",
        [
            ("cisco_ios", "10.20.0.31", "cisco", "cisco"),
            ("cisco_ios", "10.20.0.32", "cisco", "cisco"),
            ("cisco_ios", "10.20.0.33", "cisco", "cisco"),
            ("cisco_ios", "10.20.0.34", "cisco", "cisco"),
            ("cisco_ios", "10.20.0.35", "cisco", "cisco"),
        ],
    )
    def test_netmiko_ping_test_instantiation(self, platform, hostname, username, password):
        host = pingtest.NetmikoPingTest(platform, hostname, username, password, "192.168.0.1")
        inventory = host.nr.inventory.hosts.get("host1")
        assert inventory.platform == platform
        assert inventory.hostname == hostname
        assert inventory.username == username
        assert inventory.password == password

