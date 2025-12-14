USE alx_book_store;

-- Create Authors table first
CREATE TABLE Authors (
	author_id INT PRIMARY KEY,
	author_name VARCHAR(225)
);

-- Create Books tables (Depends on Authors)
CREATE TABLE Books (
	book_id INT PRIMARY KEY,
	title VARCHAR(130),
	author_id INT,
	price DOUBLE,
	publicaation_date DATE,
	FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Create Customers table (No dependencies)
CREATE TABLE Customers (
	customer_id INT PRIMARY KEY,
	customer_name VARCHAR(215),
	email VARCHAR(215),
	address TEXT
);

-- Create Orders table (depends on Customers table)
CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
	customer_id INT,
	order_date DATE,
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Order Details table (This will depends on the Order and Books table)
CREATE TABLE Order_Details (
        order_detailid INT PRIMARY KEY,
	order_id INT,
	book_id INT,
	quantity DOUBLE,
	FOREIGN KEY (order_id) REFERENCES Orders(order_id),
	FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

