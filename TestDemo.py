# Test cases to verify the logic
from SjkhZhouSui import FakerDemo

test_data = [
    {"csrq": "19731028", "zjqsrq": "20200307", "expected_zjjzrq": "30001231"},
    {"csrq": "20030726", "zjqsrq": "20200307", "expected_zjjzrq": "20300307"},
    {"csrq": "19931115", "zjqsrq": "20200307", "expected_zjjzrq": "20400307"},
]

f = FakerDemo()

for data in test_data:
    fznl = f.calculate_fznl(data["csrq"], data["zjqsrq"])
    zjjzrq = f.calculate_zjjzrq(fznl)
    print(f"csrq: {data['csrq']}, zjqsrq: {data['zjqsrq']}, fznl: {fznl}, zjjzrq: {zjjzrq}, expected_zjjzrq: {data['expected_zjjzrq']}")
    assert zjjzrq == data["expected_zjjzrq"], f"Test failed for csrq: {data['csrq']}"

print("All tests passed.")