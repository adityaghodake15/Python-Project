import sqlite3
import pandas as pd
from pathlib import Path

# Database location
DB_PATH = Path(__file__).resolve().parents[1] / "data" / "Chinook.db"

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)

# Load a few tables into Pandas
customers = pd.read_sql("SELECT * FROM Customer", conn)
invoices = pd.read_sql("SELECT * FROM Invoice", conn)
invoice_lines = pd.read_sql("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT * FROM Track", conn)

# Display data
print("Customers:")
#print(customers.head())

print("\nInvoices:")
#print(invoices.head())

print("\nInvoice Lines:")
#print(invoice_lines.head())

# Check table dimensions
#print("\nTable dimensions:")
#print("Customers:", customers.shape)
#print("Invoices:", invoices.shape)
#print("Invoice Lines:", invoice_lines.shape)
#print("Tracks:", tracks.shape)

# Merge Customers and Invoices
customer_sales = customers.merge(
    invoices,
    on="CustomerId",
    how="inner"
)

# Calculate customer-wise spending
pandas_result = (
    customer_sales
    .groupby(
        ["CustomerId", "FirstName", "LastName"],
        as_index=False
    )
    .agg(
        TotalSpent=("Total", "sum"),
        InvoiceCount=("InvoiceId", "count")
    )
    .sort_values(
        by=["TotalSpent", "CustomerId"],
        ascending=[False, True]
    )
    .head(10)
)

# Round revenue to 2 decimal places
pandas_result["TotalSpent"] = pandas_result["TotalSpent"].round(2)

print("\nTop 10 Customers - Pandas:")
print(pandas_result.to_string(index=False))


# Execute SQL query
sql_query = """
SELECT
    c.CustomerId,
    c.FirstName,
    c.LastName,
    ROUND(SUM(i.Total), 2) AS TotalSpent,
    COUNT(i.InvoiceId) AS InvoiceCount
FROM Customer c
INNER JOIN Invoice i
    ON c.CustomerId = i.CustomerId
GROUP BY
    c.CustomerId,
    c.FirstName,
    c.LastName
ORDER BY
    TotalSpent DESC,
    c.CustomerId ASC
LIMIT 10;
"""

sql_result = pd.read_sql_query(sql_query, conn)
print(sql_result.to_string(index=False))

# Reset indexes for comparison
sql_result = sql_result.reset_index(drop=True)
pandas_result = pandas_result.reset_index(drop=True)

# Validate results
from pandas.testing import assert_frame_equal

assert_frame_equal(
    sql_result,
    pandas_result,
    check_dtype=False
)

print("\nSQL vs Pandas Comparison: PASSED")
print("Both methods returned identical results.")


# 2nd Business Question :- 




conn.close()