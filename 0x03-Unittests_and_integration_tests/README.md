# 0x03. Unittests and Integration Tests
<p><strong>Unit testing</strong> is the process of testing that a particular function returns expexcted results for different set of inputs.</p><br>
<p>A unit test should only test the logic defined inside the tested function, that is teh standard inputs and corner cases.</p><br>
<p>Most calls to additional functions should be mocked, especially if they make network or database calls.</p><br>
<p><strong>Intergration testing</strong> aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.</p>
<p>Intergration test will test interaction between every part of a code.</p>

<h1>Tests execution</h1><br>
<code>
    python -m unittest path/to/test_file.py
</code><br>

# RESOURCES
<li><a href="https://intranet.alxswe.com/rltoken/a_AEObGK8jeqPtTPmm-gIA">unittest — Unit testing framework</a></li><br>
<li><a href="https://intranet.alxswe.com/rltoken/PKetnACd7FfRiU8_kpe5EA">unittest.mock — mock object library</a></li><br>
<li><a href="https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q">https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q</a></li><br>
<li><a href="https://intranet.alxswe.com/rltoken/mI7qc3Y42aZ7GTlLXDxgEg">parameterized</a></li><br>
<li><a href="https://intranet.alxswe.com/rltoken/x83Hdr54q4Vax5xQ2Z3HSA">memoization</a></li><br>