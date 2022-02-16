import asyncio
from pathlib import Path
import time
import sys
from statistics import mean, stdev

from aiocoap import *

DATAFILES = Path("/DataFiles")

HundredB = DATAFILES.joinpath("100B")
TenKB = DATAFILES.joinpath("10KB")
OneMB = DATAFILES.joinpath("1MB")
TenMB = DATAFILES.joinpath("10MB")

async def downlink(protocol, file: Path, repeat: int, size: int):
    times = []
    sizes = []
    for _ in range(repeat):
        request = Message(code=GET, uri='coap://server/hw', payload=str.encode(file.name))
        start_time = time.time()
        try:
            r = await protocol.request(request).response
            times.append(time.time() - start_time)
            sizes.append(sys.getsizeof(r))
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
    print(file.name, "Throughput Mean in kilobits:", size * 0.008 / mean(times))
    print(file.name, "Throughput STD in kilobits:", size * 0.008 / stdev(times))
    print(file.name, "Packet Size Mean in kilobits:", mean(sizes) * 0.008, flush=True)

async def main():
    protocol = await Context.create_client_context()
    # Downlink 100 B file
    print("Downlinking 100B file")
    await downlink(protocol, HundredB, 10000, 100)

    # Downlink 10kB file
    print("Downlinking 10KB file")
    await downlink(protocol, TenKB, 1000, 10000)

    # Downlink 1MB file
    print("Downlinking 1MB file")
    await downlink(protocol, OneMB, 100, 1000000)

    # # Downlink 10MB file
    print("Downlinking 10MB file")
    await downlink(protocol, TenMB, 5, 10000000)

if __name__ == "__main__":
    asyncio.run(main())