# Mental Unload
Keep your mental load low!

# Application architecture
Following the principles of clean architecture / hexagonal architecture:
- separate user side, business logic and server side
- dependencies go to business logic (business logic does not depend on user side and server side)
- layers are isolated by ports and adapters

## Use cases / business logic
Use cases are interactors. There is one use case for each individual action of an actor (person or system interacting with our application) -> one execute function.
They are to be used in APIs, cli commands, tasks, etc.

## Input DTOs
Input DTOs are immutable data structure used as arguments in the use cases' function. DTOs should be validated before being passed to use cases.

## Interfaces / ports (abstract classes)
Interfaces are wrappers used to call a third party API or another component. This prevents the use cases / business logic to be polluted with irrelevant details and names.

## Interface adapters
An adapter is just an implementation of an interface.