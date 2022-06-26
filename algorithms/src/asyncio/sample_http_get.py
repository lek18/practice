import aiohttp
import asyncio
from ml_tools.timer import Timer

## throttling
API_CONCURRENCY_LIMIT = 5

# semaphore for limiting async concurrency
sem = asyncio.Semaphore(API_CONCURRENCY_LIMIT)


async def retry_w_backoff(fn, max_retries=10):
    retries = 0
    while True:
        try:
            return await fn()
        except TimeoutError as e:
            retries += 1
            if retries >= max_retries:
                raise e
            await sleep(retries * 1)
            print(f"retrying: {retries}th time")

## your get request
async def v2_request(var, timeout, api_key, url):
    async with sem, aiohttp.ClientSession(raise_for_status=False) as session:
        with Timer('v2_req', print):
            url = url
            headers = {"X-Api-Key": api_key, "Content-Type": "application/json"}
            # could be get input
            data = {
                "input1": var
            }
            async with session.get(
                url, data=data, timeout=timeout, headers=headers
            ) as response:
                if response.status == 404:
                    return None
                res = await response.json()
                return res

async def wrapper_func1(input1, api_key, url):
    try:
        if input1 is None:
            return None
        timeout = aiohttp.ClientTimeout(5)
        fn = lambda: v2_request(input1, timeout, api_key, url)
        return await retry_w_backoff(fn)
    except Exception as e:
        print(f"Error with {input1}")
        print(e)
        return None


# batch async calls to  endpoint
# Only unique set of inputt are queried
# Return value is respone from endpoint
async def batch_4_wrapper_func1(input1, api_key, url):
    with Timer("span_match_companies", print):
        unique_inputs = list(set(input1))
        reqs = [
            asyncio.create_task(wrapper_func1(inputs, api_key, url))
            for inputs in unique_inputs
        ]
        results = await asyncio.gather(*reqs)
        output_lookup = dict(zip(unique_inputs, results))
        return output_lookup

API_KEY = "your key if needed"
api_url = "YOUR URL GET/POST"

## using the batch
output = await batch_4_wrapper_func1(input_names=[],
                                     api_key=API_KEY,
                                     url=api_url
                                     )