from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
