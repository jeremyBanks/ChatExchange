import asyncio
import collections


class Throttle:
    def __init__(self, interval):
        self.interval = interval
        self._queue = collections.deque()
        self._loop = asyncio.get_event_loop()
        self._queue_runner = self._loop.create_task(self._run_queue())
        self._next_awakening = self._loop.create_future()

    async def _run_queue(self):
        while True:
            if not self._queue:
                await self._next_awakening
                continue

            future = self._queue.popleft()
            future.set_result(None)
            await asyncio.sleep(self.interval, loop=self._loop)

    def _wake_queue_runner(self):
        self._next_awakening.set_result(None)
        self._next_awakening = self._loop.create_future()

    async def turn(self):
        future = self._loop.create_future()
        queue_was_empty = len(self._queue) == 0

        self._queue.append(future)

        if queue_was_empty:
            self._wake_queue_runner()

        return future
