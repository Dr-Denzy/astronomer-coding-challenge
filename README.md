### Design / Implementation Decision and Limitations
- In a non-test condition I would have preferred to use a production-ready Python framework such as Flask or FastAPI to implement my solution.
- I would have also preferred a persistent data storage for my objects. Or use an ORM for my models.
- In the unittest, for the sake of time pressures, I had to do  float comparison which I know can be a source of bugs somewhere down the road. In a non-test condition I would use a more robust solution for that.

### Testing
- unittests were written using Pytest framework.
- In a non-test condition I would have gone the TDD route where I would be compelled to write a more extensive unittest coverage for my implementation.

### Time and Space Complexity
- Python builtin dictionary and lists used for the cart class implementation.
- Appending an item to a dictionary has O(1).
- fetching an item by key from a dictionary is also O(1).


### Setup / Run this program
1. Mac/Linux OS: launch the terminal program and `cd` into the astronomer directory.

2. run `pip3 install -r requirements.txt` or `pip3 install -e .` 

3. run the python script like so:  `python3 cart.py` or `python3 -m cart`.

