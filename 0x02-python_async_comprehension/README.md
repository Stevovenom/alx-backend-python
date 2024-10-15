# 0x02-python_async_comprehension

<h1> Writing an Asynchronous Generator </h1><br>
<p>An asynchronous generator allows you to yield values whilel performing asynchronous operations. This is useful when yo need to perform non-blocking operations like I/O tasks while generating values.</p><br>
<p> To define an asynchronous generator, use the <code>async def </code> keyword, ad to yield values, use <code>yield</code> keyword with the <code>await</code> keyword for asynchronous calls.</p><br>
<code>
async def async_gen():
    for i in range(5):
        await asyncio.sleep(1) // the asynchronous operation
        yield i

</code><br><br>
<h2> Explanation</h2><br>
<p>Here, the generator <strong>async_gen()</strong> yields numbers from 0 to 4 but awaits for 1 second between each yield. The key points are:</p><br>
1. <strong> async def </strong> is used to declare the generator.<br>
2. <strong> await </strong> allows the generator to pause while waiting for some asynchronous operation like <code> asyncio.sleep </code><br><br>
<p> To iterate over an asynchronous generator, you use <strong><code>async for</code><strong>:<br>
<code>
import asyncio

asyncio def async_gen():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_gen():
    print(value)

// run the asynchronous code
asyncio.run(main())
</code><br>

<h1> Using Async comprehensions </h1><br>
<p>Async comprehensions are used to iterate over asynchronous iterators like asynchronous generators in a concise and readable way.</p><br>

<code>
async def async_comprehension():
    result = [i async for i in async_gen()]
    return result
</code><br>
<h2> Explanation </h2><br>
1. The <strong>async for</strong> loop is used within a list comprehension.<br>
2. It gathers all values from the asynchronous generator into a list.<br>

<p>To run the async comprehension:</p><br>
<code>
import asyncio

async def async_gen():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def async_comprehension():
    return [i async for i in async_gen()]

async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())
</code><br><br>

<h1> Type-Annotating Generators </h1><br>
<p> To add type annotations for generators, you use <strong><code>Generator</code></strong> from <strong><code>typing</code><strong> for regular generators and <strong><code>AsyncGenerator</code></strong> for asynchronous generators.</p><br>

<p>A <strong>regular generator</strong> that yields integers can be annoted as follows:</p><br>
<code>
from typing import Generator

def gen_numbers() -> Generator[int, None, None];
    for i in range(5):
        yield i
</code><br>

<h2> Explanation </h2><br>
<p>The annotation <strong><code>Generator[int, None, None] </code></strong> means:<br>
1. The generator yields integers (int).<br>
2. It doesn't accept any input when resuming None.<br>
3. It returns None when done.<br>

<p>For an <strong> asynchronous generator</strong>, we use <strong><code>AsyncGenerator</code></strong>:<br>
<code>
from typing import AsyncGenerator
import asyncio

async def async_gen() -> AsynGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i
</code><br>

<h2> Explanation </h2>
1. The generator yields integers int.<br>
2. It doesnt accept any inputs or send any values when resumed None.<br>

<h2>Exampe of usage is: </h2><br>
<code>
from typing import AsynGenerator
import asyncio

async def async_gen() -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_gen():
        print(value)

asyncio.run(main())
</code><br>
<p> In the code above, the <strong><code>async_gen()</code><strong> is an asynchronous generator that yields integers, and its type annotation clearly reflects this asn it does not return any final value when its finished None.<p><br>

# RESOURCES
<a href="https://intranet.alxswe.com/rltoken/hlwtED-iLsdORSgly8DsyQ">PEP 530 – Asynchronous Comprehensions</a><br>
<a href="https://intranet.alxswe.com/rltoken/0OkbObYzCKtO7ZUAxfKvkw">What’s New in Python: Asynchronous Comprehensions / Generators</a><br>
<a href="https://intranet.alxswe.com/rltoken/l4Fnno568VbVIn9GvrFVtQ">Type-hints for generators</a><br>
