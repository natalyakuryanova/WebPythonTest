from BaseCMD import co
import yaml

with open("cmddata.yaml") as f:
    cmddata = yaml.safe_load(f)

address = cmddata.get('address')
tuning = cmddata.get('tuning')

class TestPositive:
    def test_nikto(self):
        res = co(f"nikto -h {address} -ssl -Tuning {tuning}", "0 error(s)")
        assert res, "test nikto FAIL"