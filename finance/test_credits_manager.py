import os

from finance.credits_manager import CreditsManager


def test_credits_manager():
    log_file = "test_credits_log.csv"
    # Clean up any previous test log
    if os.path.exists(log_file):
        os.remove(log_file)
    cm = CreditsManager(log_file)
    cm.add_user("alice", 100)
    cm.earn_credits("alice", 50)
    cm.spend_credits("alice", 20)
    balance = cm.get_balance("alice")
    assert balance == 130, f"Expected 130, got {balance}"
    cm.add_user("bob", 0)
    cm.earn_credits("bob", 200)
    assert cm.get_balance("bob") == 200
    try:
        cm.spend_credits("bob", 300)
    except ValueError:
        pass  # Expected
    else:
        raise AssertionError("Should raise ValueError for insufficient credits")
    # Clean up
    if os.path.exists(log_file):
        os.remove(log_file)


if __name__ == "__main__":
    test_credits_manager()
    print("All tests passed.")
