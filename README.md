# Kaprekar's Constant

Description
- A small Python script that performs Kaprekar's routine (for 4-digit numbers) until it reaches Kaprekar's constant 6174.

Example
- Start: 3524
  - D_desc = 5432
  - D_asc  = 2345
  - 5432 - 2345 = 3087
  - Repeat with 3087 → 8730 - 0378 = 8352 → 8532 - 2358 = 6174
  - 
Notes
- Input should be validated to ensure at least two different digits; numbers like 1111 will immediately produce 0 and not reach 6174.