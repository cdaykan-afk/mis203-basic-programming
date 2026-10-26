# Lab 05 - Shipping Quote

## Testing & Fixes
- **Test run:** Tested `calculate_shipping_fee(100.00, "standard")` to see if exactly $100 earns free shipping.
- **Change made:** I originally wrote `if discounted_subtotal > 100.00:`, which charged a $7.50 fee on an exact $100 order. I changed it to `>= 100.00` so customers hitting the threshold get free shipping.
