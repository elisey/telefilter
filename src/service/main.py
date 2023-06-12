import logging

from client import Client
from core.config import settings
from filter_service import FilterServiceBasic, Rules


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def main() -> None:
    rules = Rules(include=settings.include_only)
    filter_service = FilterServiceBasic(rules)
    client = Client(
        settings.api_id,
        settings.api_hash,
        settings.session_key,
        filter_service,
        settings.send_to_channel,
        settings.monitor_channels,
    )
    client.run()


if __name__ == "__main__":
    main()
