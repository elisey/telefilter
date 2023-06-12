from __future__ import annotations

import logging
from typing import Collection

from telethon import TelegramClient, events
from telethon.events.newmessage import NewMessage
from telethon.sessions import StringSession
from telethon.tl.types import Message

from filter_service import FilterServiceInterface


logger = logging.getLogger(__name__)


class Client(TelegramClient):  # type: ignore[misc]
    def __init__(
        self,
        api_id: int,
        api_hash: str,
        session_key: str,
        filter_service: FilterServiceInterface,
        send_to_channel: str,
        monitor_channels: Collection[str],
    ):
        super().__init__(StringSession(session_key), api_id=api_id, api_hash=api_hash)
        self.filter_service = filter_service
        self.send_to_channel = send_to_channel

        event_message_filter = events.NewMessage(chats=set(monitor_channels))
        self.add_event_handler(self.messages_event_handler, event_message_filter)

    async def _handle_message(self, message: Message) -> Message | None:
        filtered_data = self.filter_service.handle(message.message)

        if filtered_data is None:
            logger.info("Message filtered out. Skip")
            return None

        message.message = filtered_data

        return message

    async def messages_event_handler(self, event: NewMessage.Event) -> None:
        logger.info(f"Received event: {event}")

        message = await self._handle_message(event.message)
        if message is None:
            return
        channel = await self.get_entity(self.send_to_channel)
        await self.send_message(channel, message)

    def run(self) -> None:
        self.start()
        self.run_until_disconnected()
