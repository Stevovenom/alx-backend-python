# 0x00-python_variable_annotations


<img src="https://i.redd.it/y9y25tefi5401.png" alt="variable annotations"><br>
    <h1>Type Annotations in Python 3</h1>
    
<h2> 1. ⚔️How to Use Type Annotations</h2>
    <p>Type annotations in Python allow you to explicitly declare the data types of variables, function arguments, and return types. This helps in making your code more readable and allows static type checkers like <code>mypy</code> to catch potential issues before runtime.</p>

<h3>Function Signatures with Type Annotations</h3>
    <pre><code>def greet(name: str) -> str:
    return f"Hello, {name}!"</code></pre>
    <p>In this example, the function <code>greet</code> accepts a parameter <code>name</code> of type <code>str</code> and returns a <code>str</code>. Type annotations make it clear what type of data is expected and returned.</p>

 <h3>Variable Type Annotations</h3>
    <pre><code>x: int = 10
y: float = 5.5
is_valid: bool = True</code></pre>
    <p>Here, variables <code>x</code>, <code>y</code>, and <code>is_valid</code> are explicitly typed. Python does not enforce these types at runtime, but tools like <code>mypy</code> can check for consistency.</p>

 <h2>2. Duck Typing</h2>
    <p>Python is dynamically typed, and the idea of <strong>Duck Typing</strong> means that the type or class of an object is less important than the methods it defines. If an object behaves like a certain type, it can be used as that type. This is summarized by the phrase "If it looks like a duck and quacks like a duck, it’s probably a duck."</p>
    
<p>For example:</p>
    <pre><code>class Duck:
    def quack(self):
        print("Quack!")
        
class Dog:
    def quack(self):
        print("Woof-quack!")</code></pre>
    <p>Even though <code>Duck</code> and <code>Dog</code> are different classes, as long as the <code>quack</code> method is present, Python treats them as similar types in certain contexts.</p>

<h2>3. Validating Code with mypy</h2>
    <p><code>mypy</code> is a static type checker for Python. It analyzes type annotations in your code and reports mismatches between expected and actual types.</p>

 <h3>Installing mypy</h3>
    <pre><code>pip install mypy</code></pre>

 <h3>Running mypy</h3>
    <p>You can run <code>mypy</code> on your Python files to check for type consistency:</p>
    <pre><code>mypy my_script.py</code></pre>
    <p>If there are any type mismatches, <code>mypy</code> will report them.</p>

 <h2>Useful Links</h2>
    <ul>
        <li><a href="https://docs.python.org/3/library/typing.html" target="_blank">Python Typing Documentation</a></li>
        <li><a href="https://mypy.readthedocs.io/en/stable/" target="_blank">mypy Documentation</a></li>
        <li><a href="https://realpython.com/python-type-checking/" target="_blank">Real Python - Type Checking in Python</a></li>
    </ul>

# RESOURCES
<a href="https://intranet.alxswe.com/concepts/554">Advanced python</a><br>
