Week 3 Lab: Order Approval Policy

This program (lab03_order_approval.py) verifies order eligibility based on requested quantity and stock levels, and applies a 10% discount for members on orders of 500 TRY or more.

Boundary Test Table (Stretch Task)

| Test Case | Order Amount | Available Stock | Requested Quantity | Is Member? | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Boundary 1 (< 500 TRY) | 499.99 TRY | 10 | 2 | Yes | Approved, No discount, Final: 499.99 TRY | Approved, Final: 499.99 TRY |
| Boundary 2 (= 500 TRY) | 500.00 TRY | 10 | 2 | Yes | Approved, 10% discount, Final: 450.00 TRY | Approved, Final: 450.00 TRY |
| Boundary 3 (> 500 TRY) | 500.01 TRY | 10 | 2 | Yes | Approved, 10% discount, Final: 450.01 TRY | Approved, Final: 450.01 TRY |
| Error (Insufficient Stock) | 600.00 TRY | 3 | 5 | Yes | Rejected (Insufficient stock), No final price | Rejected, No final price |
| Error (Invalid Quantity) | 600.00 TRY | 10 | 0 | No | Rejected (Quantity <= 0), No final price | Rejected, No final price |
