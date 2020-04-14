import pytest
import nuts.testcreation.concretetests.netmiko_ping_test as pingtest
from unittest.mock import call


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

    @pytest.mark.parametrize(
        "mocked_result, expected",
        [
            ("Success rate is 100 percent (5/5)", True),
            ("Success rate is 100 percent (3/5)", False),
            ("Success rate is 100 percent (0/5)", False),
            ("Some String", False),
            (12, False),
        ],
    )
    def test_evaluate_result(self, mocked_result, expected):
        instance = pingtest.NetmikoPingTest(
            "cisco_ios",
            "192.168.0.1",
            "cisco",
            "cisco",
            "0.0.0.0"
        )
        assert instance.evaluate_result(mocked_result) == expected

