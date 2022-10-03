from js import createObject, document, pythonDone
from pyodide.ffi import create_proxy
import asyncio

document.dispatchEvent(pythonDone)

value = 0
createObject(value, "pythonValue")

for i in range(10):
    value = i
    await asyncio.sleep(1)
