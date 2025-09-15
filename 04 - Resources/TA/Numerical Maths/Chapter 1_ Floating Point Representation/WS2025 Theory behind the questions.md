---
tags:
  - numerical
date: 2025-09-15T09:27:00
---
## Question 1

![[Pasted image 20250915092814.png]]
### 1. Why DC bus current matters
In power electronics (think inverters, converters, motor drives, UPS systems), the **DC bus** is the main energy highway inside the system. You usually start with rectified AC or a battery, and this creates a DC link (the “bus”).
- The **DC bus current** tells you how much power is flowing through the system.
- It’s critical for:
    - **Monitoring** (is the system overloaded?)
    - **Control** (regulating motor speed, torque, etc.)
    - **Protection** (shut things down before smoke comes out).
Because current can flow in either direction (charging vs. discharging, motoring vs. braking), you need a number that can represent **positive and negative values**. And because real-world measurements aren’t usually nice whole numbers, you also need **fractions**. That’s where floating-point comes in.
---
### 2. Decimal vs. binary
- Humans think in **decimal (base-10)**, because we’ve got 10 fingers.
- Computers think in **binary (base-2)**, because hardware is built from switches that are either **on (1)** or **off (0)**.

Storing integers in binary is straightforward. The problem is with **real numbers** (with fractions). You can’t just slap a decimal into binary memory and hope it works. You need a standard representation.

---
### 3. Enter IEEE-754
The IEEE-754 standard is the worldwide agreement on how to represent floating-point numbers in binary. Without it, a float saved on one computer might mean something completely different on another.

For **single precision (32-bit, float32):**
- **1 bit** = sign (0 for +, 1 for –)
- **8 bits** = exponent (with a bias of 127)
- **23 bits** = fraction (mantissa/significand)

The actual value is:
```ini 
Value = (–1)^sign × (1 + mantissa) × 2^(exponent – 127)
```

So, with 32 bits, you can store a wide range of positive and negative numbers, with fractions, at a reasonable precision. Perfect for measured currents.

---
### 4. Why not just use integers?
Imagine measuring DC bus current:
- Sometimes it’s **tiny** (milliamps of standby power).
- Sometimes it’s **huge** (hundreds of amps in a motor drive).

Using fixed integers (say, a signed 16-bit int) would either:
- Run out of range (too small or too large).
- Lose fractional resolution (round everything badly).

Floating-point gives you the **dynamic range** (very small to very large) and **fractional precision** needed in real systems.

---

### 5. The specific task (–25.125 A)
That’s just the worked example where you actually encode the number into the IEEE-754 binary32 format. The question you pasted is basically saying: _“Here’s why floating-point exists, now prove you understand by encoding this real-world measurement.”_

---

So in summary:
- DC bus current is vital for control and protection.
- Decimal is how humans think, binary is how machines think.
- IEEE-754 is the universal way to represent fractional real numbers in binary.
- Floating-point is chosen over integers because of its huge range and precision.
- –25.125 A is just the practical example.
---
## Question 2

![[Pasted image 20250915100743.png]]

---
### 1. Why floating-point in data acquisition?
Industrial systems live in the real world, where sensor outputs aren’t neat integers. Voltage can be **tiny** (millivolts) or **large** (hundreds of volts), and it usually has **fractional parts**. Storing those values as fixed-point integers would either:
- Clip the large numbers, or
- Lose all precision in the small ones.

Floating-point (IEEE-754) solves that by giving a **huge dynamic range** and **fractional accuracy**, all in a fixed 32-bit format. That way, any device (microcontroller, logger, PC) can read the same binary pattern and decode the same real number without arguments.

---
### 2. Structure of IEEE-754 binary32 (single precision)
The 32 bits are split up:
- **1 bit**: sign (0 for +, 1 for –)
- **8 bits**: exponent (stored with a bias of 127)
- **23 bits**: fraction (mantissa)

Value is interpreted as:
``` ini
(–1)^sign × (1 + mantissa) × 2^(exponent – 127)
```
This format ensures you always have a **normalized form** (leading 1 before the binary point) for nonzero numbers, which maximizes precision.

---
### 3. Why the bias again?
Because exponents can be positive or negative, but hardware doesn’t want to deal with signed fields. By adding a bias (127 for single precision), all exponents are stored as unsigned integers. For example:
- Exponent –1 → stored as 126
- Exponent 0 → stored as 127
- Exponent +3 → stored as 130

This makes sorting, comparisons, and hardware decoding far easier.
