# Library Management System (Data Structures Project)

This project is a console-based Library Management System written in Python. It was developed as a practical assignment for my Data Structures course to implement and utilize core data structures from scratch.

## Core Technical Features

The system is built around custom data structures to ensure efficiency:

1.  **Book Catalog (Binary Search Tree - BST)**
    * **Why:** A BST is used to store the book catalog, using the **ISBN** as the key.
    * **Advantage:** This allows for highly efficient book lookups, insertions, and deletions (Average case: **O(log n)**). It also provides a trivial way to list all books in sorted order (by ISBN) using an **in-order traversal**.
    * *Implementation:* `BookBST` and `BookNode` classes.

2.  **Reservation Queue (Linked List)**
    * **Why:** Each book object (`BookNode`) contains its own reservation queue to manage waiting lists fairly.
    * **Advantage:** A custom-built **Linked List** is used to implement a **FIFO (First-In, First-Out) Queue**. By tracking both the `head` and `tail` of the list, both adding a new reservation (`append`) and serving the next member in line (`pop_left`) are **O(1)** operations. This ensures the system remains fast, even with long waiting lists.
    * *Implementation:* `ReservationList` and `ReservationNode` classes.

3.  **Member Registry (Python Set)**
    * **Why:** A Python `set` is used to manage member registrations.
    * **Advantage:** This inherently enforces **uniqueness** (a member cannot be registered twice) and provides **O(1)** average time complexity for checking if a member exists in the system.
4. Action History (Stack)
   * To track the system's operation logs, a Stack data structure is implemented manually (using a linked-list approach).

   * Purpose: The system records every critical action (e.g., adding a book, registering a member, lending/returning a book).

   * Why Stack?: The LIFO (Last-In, First-Out) principle is ideal for log management. When a user requests to see the history, they are primarily interested in the most recent activities. The Stack ensures the latest transaction is always accessed first at the top.

   * Implementation:

   * LogNode Class: Represents a single log entry containing a message string and a pointer to the next node.

   * ActionStack Class: Manages the nodes.

   * Complexity: The push operation is O(1) (constant time), ensuring that logging does not slow down the main operations.

## Functional Features

* **Add Book:** Add a new book to the catalog (via BST insertion).
* **Register Member:** Add a new, unique member to the system (via Set insertion).
* **Lend Book:**
    * If available, mark the book as "Checked Out".
    * If unavailable, add the member to that book's reservation queue (via Linked List `append`).
* **Return Book:**
    * If no reservations, mark the book as "Available".
    * If reservations exist, automatically assign the book to the next member in the queue (via Linked List `pop_left`).
* **List All Books:** Prints a full list of books, sorted by ISBN (via BST `in-order` traversal).
* **List All Members:** Prints an alphabetized list of all registered members.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Clone this repository.
3.  Navigate to the project directory and run:
    ```bash
    python library_system.py
    ```

## Development & Learning

This project was a valuable exercise in applying data structure theory to a practical problem. The design choices (BST vs. List, Linked List vs. Array) were made to prioritize performance for common operations like searching and queue management.

AI (Chatgpt 5) was used as a collaborative tool and learning aid during development, particularly for validating these design choices and refining the implementation of the custom data structures.
