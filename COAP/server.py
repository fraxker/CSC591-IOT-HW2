import logging
from pathlib import Path

import asyncio

import aiocoap.resource as resource
import aiocoap

DATAFILES = Path("/DataFiles")

HundredB = DATAFILES.joinpath("100B")
TenKB = DATAFILES.joinpath("10KB")
OneMB = DATAFILES.joinpath("1MB")
TenMB = DATAFILES.joinpath("10MB")

class HWClass(resource.Resource):
    async def render_get(self, r):
        flag = r.payload.decode("utf-8")
        match flag:
            case HundredB.name:
                file = HundredB
            case TenKB.name:
                file = TenKB
            case OneMB.name:
                file = OneMB
            case TenMB.name:
                file = TenMB
            case _:
                raise Exception(f"Unknown name: {flag}")
        with file.open("rb") as f:
            return aiocoap.Message(payload=f.read())

logging.basicConfig(level=logging.INFO)

async def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['hw'], HWClass())

    await aiocoap.Context.create_server_context(root)

    # Run forever
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())