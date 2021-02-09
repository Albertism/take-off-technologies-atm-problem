# take-off-technologies-atm-problem
ATM design problem from take off technologies take home assignment.

## Usage
For the main program you can run this in the root directory:
```
main.py
```

For the tests:
```
python -m unittest
```

## Potential improvements
In hindsight, these are some of the improvements I would make for better performance / readability

- **Using an ORM**: I used helper methods to directly map queries to objects. I should use proper ORMs to improve performance and data integrity
- **Better encapsulations**: I used global variables in multiple locations which are not safe. I would use better thought out encapsulations to avoid running into potential issues.
- **Better structured modules**: I feel that I should further split main.py into modules that makes more sense, for example a timer should be in its own module. I believe this could improve readability a lot more
- **Handling fail cases for db**: I did not implement handlers to handle cases when query execution failed. This will ensure application to be more stable.
- **Better written test cases**: I should use mocks to thoroughly test apis and main functionalities. In this case, I was not quite sure the best ways to write good test cases for them.

I would really appreciate any feedbacks on this project!
