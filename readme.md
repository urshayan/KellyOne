#  KellyOne

**KellyOne** is a Python-based desktop app built with Tkinter that helps traders and investors find the *optimal position size* for their trades using the **Kelly Criterion** — a mathematical formula designed to maximize long-term capital growth while managing risk.

---

##  Features

✅ Simple and elegant Tkinter interface  
✅ Calculates the optimal fraction (`f*`) to invest based on win probability and reward-to-risk ratio  
✅ Provides a recommended investment amount based on total capital  
✅ Warnings for over-risked trades    

---

## Source
  <https://en.wikipedia.org/wiki/Kelly_criterion>

##  The Kelly Formula

\[
f^* = \frac{bp - q}{b}
\]

Where:
- **b** = reward-to-risk ratio  
- **p** = probability of winning  
- **q** = 1 - p = probability of losing  

KellyOne calculates the fraction of your capital you should invest (`f*`) and converts it into a recommended dollar amount.

---

##  Example

| Input | Value |
|--------|--------|
| Probability of Winning (p) | 0.6 |
| Reward-to-Risk Ratio (b) | 1.5 |
| Total Capital ($) | 10,000 |

**Output:**
>  Optimal Fraction: 33.33%  
>  Recommended Investment: \$3,333.33  

---

##  Installation

```bash
# Clone the repository
git clone https://github.com/urshayan/KellyOne
cd KellyOne

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

