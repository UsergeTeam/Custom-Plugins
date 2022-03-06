

# here you can do the main thing like registering handlers, ...

from userge import userge, Message
from .. import _plugin_name as test


@userge.on_cmd("test", about="my first command")
async def first_command(message: Message) -> None:
    """ this thing will be used as command doc string """

    test.Dynamic.TIMEOUT = 90

    await call_api()

    await message.edit("first cmd executed")


async def call_api() -> None:
    print(test.API_KEY)
