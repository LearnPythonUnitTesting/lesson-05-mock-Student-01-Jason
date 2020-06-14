# Lesson-05-Mock
### 1. unittest.mock — mock object library
unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.

Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel for creating unique objects. See the quick guide for some examples of how to use Mock, MagicMock and patch().

Mock is very easy to use and is designed for use with unittest. Mock is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by many mocking frameworks.

There is a backport of unittest.mock for earlier versions of Python, available as mock on PyPI.

### 2. Basic Example
```
def get_result(a, b):
    pass
```
How could we test a unfinished method like 'add(a,b)'.
```
class TestMethod(unittest.TestCase):
    def test_get_result(self):
        cal.get_result = mock.Mock(return_value=15)
        print(cal.get_result(2, 5))
        print(cal.get_result(3, -5))
        print(cal.get_result(-5, -6))
        print(cal.get_result(5, 10))
        self.assertEqual(cal.get_result(5, 10), 15)
```
Use mock.Mock() to configure return_value of cal.get_result as 15. 

### 3. Exercise
Complete 'test_calculate' to test method 'get_int()'.