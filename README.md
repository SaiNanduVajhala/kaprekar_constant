# Kaprekar Program

Description
- A small Python script that performs Kaprekar's routine (for 4-digit numbers) until it reaches Kaprekar's constant 6174.

Formula
- For a given 4-digit number with at least two distinct digits:
  1. Let D_desc be the digits sorted in descending order.
  2. Let D_asc be the digits sorted in ascending order.
  3. Compute: result = D_desc - D_asc
  4. Repeat the process with result until it reaches 6174 (Kaprekar's constant) or enters a fixed point.

Steps
1. Choose a 4-digit number (leading zeros allowed) with at least two different digits.
2. Form the largest number by sorting digits descending (`D_desc`).
3. Form the smallest number by sorting digits ascending (`D_asc`).
4. Subtract: `result = D_desc - D_asc`.
5. If `result == 6174` stop; otherwise go to step 2 using `result` (pad with leading zeros to 4 digits).

Example
- Start: 3524
  - D_desc = 5432
  - D_asc  = 2345
  - 5432 - 2345 = 3087
  - Repeat with 3087 → 8730 - 0378 = 8352 → 8532 - 2358 = 6174

Usage
- Run the program from the workspace root:

```powershell
python Kaprekar.py
```

Notes
- Input should be validated to ensure at least two different digits; numbers like 1111 will immediately produce 0 and not reach 6174.
