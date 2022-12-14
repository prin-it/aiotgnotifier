"""Main module."""

import httpx


class Notifier:
    """Notifier class for telegram messenger."""

    _message_url = "https://api.telegram.org/bot{token}/sendMessage"

    def __init__(self, token: str, ids: list[int]) -> None:
        """Init class.

        :param token: telegram bot token
        :param ids: list of user ids for notification
        """
        self._token = token
        self._ids = ids

    async def notify(self, message: str) -> bool:
        """Send notification message.

        :param message: message text
        :return: status of sending
        """
        success = True
        url = self._message_url.format(token=self._token)
        async with httpx.AsyncClient() as client:
            for chat_id in self._ids:
                try:
                    await client.post(
                        url,
                        json={
                            "chat_id": chat_id,
                            "text": message,
                            "parse_mode": "MarkdownV2",
                        },
                    )
                except Exception:
                    success = False
        return success
