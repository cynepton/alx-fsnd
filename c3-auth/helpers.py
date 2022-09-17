from functools import wraps


def decorator(destination: str):
    """Main decorator

    The actual decorator being called.
    The only purpose of this really is to allow you pass arguments when \
    calling the decorator.

    For example:

    ```
    @decorator(destination="Paris")
    def some_function():
    ```
    
    The paarameters passed are then available within the function context for \
    other functions being defined inside of this one to use.

    This returns the `inner_decorator` that expects the function that 

    Args:
        destination (str): The destination
    """
    def inner_decorator(function: function):
        """Actual decorator

        This is the function returned by the main decorator function.

        python will call it and pass it the function that is wrapped with the decorator.

        For example, for a function fly:

        ```
        @decorator(destination="Paris")
        def fly():
        ```

        This would be the quivalent of doing:

        ```
        def fly():
            ...
        
        fly = inner_decorator(fly)
        ```


        Args:
            function (_type_): The actual function being wrapped with the decorator

        Returns:
            function : The function being wrapped 
        """

        # @wraps takes the properties of the wrapped function such as `__doc__`
        # and gives them to the wrapper function
        @wraps(function)
        def wrapper():
            """The wrapper function

            This is the function that actually gets run in the end in the \
            place of the wrapped function.
            """
            print("Before transporting to {}".format(destination))
            if destination.lower() == "paris":
                function()
                print("Transported")
            else:
                print("Could not transport")
        return wrapper
    return inner_decorator

@decorator(destination="Paris")
def fly():
    """Flying action
    """
    print("In transit")

@decorator(destination="Lagos")
def drive():
    print("Driving")

print(fly.__doc__)
fly()
drive()


