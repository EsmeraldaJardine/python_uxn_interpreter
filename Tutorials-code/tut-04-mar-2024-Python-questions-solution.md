# Python features used in the course

These are some less common features of Python that we will use in the course:

* Tuples
* Enums
* Objects
* Lambdas
* Maps
* Using functions as values

Also, but to be discussed later:

* Bit masking and bit shifting


## Exercise 

* Create a class with a number, a string and a boolean

    The number is the length of the string; the boolean indicates if the string has been manipulated

    ```python
    """
    I use the class purely as a container ("record" or "struct") 
    to group some values.
    So there is no need for an explicit constructor 
    nor for getters, setters or any other methods. 
    It is of course not wrong to use these.
    """
    
    class StrContainer:
        string = ""
        length = 0
        touched = False
    ```
* Populate a list with instances of this class


    ```python
    """
    I create a list of strings by splitting a string 
    """

    strings = """
        haru no nioi mo
        mefuku hana mo 
        tachisukumu atashi ni 
        kimi wo tsurete wa konai
        """.split()

    """
    I pad the strings with a single space at the end
    """
    paddedStrings = map(lambda s : s+' ',strings)

    """
    Using `map` of a function `populate()` over `paddedStrings`, 
    I populate a list with StringContainer instances

    `populate()` 
    creates an instance, 
    sets the `string` and `length` attributes via assignment 
    and returns it.
    """
    def populate(st):
        strCont = StrContainer()
        strCont.str = st
        strCont.length = len(st)
        return strCont

    strContainers = map(populate, paddedStrings)
    ```
* Using a map and a lambda, convert this list to a list of tuples

    ```python
    """
    Converting the objects to tuples is easy:
    every attribute becomes a tuple element
    """
    strTups = map( lambda s : (s.str,s.len,s.touched), strContainers)
    ```

* In the same way, remove the last character from every string and decrement the length field. 

    ```python
    """
        We take the tuple and modify each element:
        the last characator of `string` is removed a slice `[0:t[1]-1]`;
        the `length` is decremented;
        the `touched` field is set to `True`
    """
    updatedStrTups = map( lambda t : (t[0][0:t[1]-1],t[1]-1,True), strTups)

    """
    That's it. Print it our to check.
    The `list()` is needed because map returns an iterator, not a list
    """
    print(list(map(lambda t: t[0],updatedStrTups)))
    ```



