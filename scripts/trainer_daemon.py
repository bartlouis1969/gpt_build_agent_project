from __future__ import annotations

import os
import time


def main() -> None:
    """Placeholder daemon voor CI (geen side effects)."""
    if os.getenv("TRAINER_DAEMON_DEBUG") == "1":
        # kort slaapje zodat het script niet meteen sluit als je het lokaal test
        time.sleep(0.01)


if __name__ == "__main__":
    main()
