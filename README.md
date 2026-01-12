# Option-Pricing-Analytics-Lab
**Quantitative Finance laboratory for Option Payoff modeling and Risk Analytics.**

## 1. Presentation
This project was developed during my second year at **Télécom SudParis** as an advanced extension of my derivative studies. Following the `Forward-Arbitrage-Lab`, which focused on linear instruments, this library builds a robust **Payoff & P&L Engine** for non-linear derivatives.

The objective is to provide a modular and vectorized framework to evaluate financial outcomes for both **European Vanilla** options and **Path-Dependent Exotic** structures.

## 2. Theoretical Framework
The library is engineered to handle the mathematical complexity of different exercise logics:

### A. Path-Independent (Vanilla Options)
The payoff depends strictly on the underlying asset price at maturity $S_T$:
*   **European Call**: $\max(0, S_T - K)$
*   **European Put**: $\max(0, K - S_T)$

### B. Path-Dependent (Exotic Options)
The gain is a function of the entire price path $\{S_t\}_{t \in [0,T]}$ observed during the life of the contract:
*   **Asian Options**: Mitigate spot volatility using arithmetic or geometric averages.
*   **Barrier Options**: Activation (**Knock-in**) or deactivation (**Knock-out**) logic based on price thresholds ($H$).
*   **Lookback Options**: "Zero-regret" structures using historical extrema ($S_{max}$ or $S_{min}$) as reference.
*   **Chooser Options**: Provides the holder the right to choose the option type (Call/Put) at an intermediate date.
*   **Binary (Digital) Options**: "All-or-nothing" payoffs based on a binary condition.
*   **Forward Start Options**: Exotic structures where the strike price is determined at a future fixing date.

### C. Risk Analytics: Net P&L Profile
The engine evaluates the **Net Profit & Loss** by subtracting the option's cost (Premium) from the final payoff:

$$
PNL = Payoff(S_t) - Premium
$$

## 3. Implementation Details
*   **Architecture**: Full Object-Oriented Programming (OOP) using **Abstract Base Classes (ABC)** to ensure a unified interface across all derivatives.
*   **Vectorization**: Intensive use of **NumPy** for high-performance path analysis (Max, Min, Mean), simulating professional quantitative development standards.
*   **Numerical Stability**: Implementation of the **Log-mean-exp trick** for Geometric Asian options to prevent arithmetic overflow on long time-series.
*   **Polymorphism**: The core engine treats all derivatives as generic `Option` objects, allowing for seamless portfolio benchmarking through a single execution hub.

## 4. Project Structure
```text
core/
├── base.py       # Abstract interface & Shared Analytics (P&L logic)
├── vanilla.py    # Standard European Call/Put implementations
└── exotic.py     # Advanced Path-Dependent derivatives (6 classes)
main.py           # Multi-product benchmarking and testing hub
```
## 5. Development Roadmap
* **Phase 1**: Implementation of the 6 major Exotic families and P&L modeling.
* **Phase 2**: Integration of a Monte Carlo Simulator (Geometric Brownian Motion) to compute the fair value (Price) of exotic contracts.
* **Phase 3**: Greeks calculation (Delta, Gamma, Vega) for exotic risk monitoring.

## Career Objective
Aspiring **Quantitative Researcher / Developer**. Currently seeking an internship in Quantitative Finance starting in **Fall 2026**. I am focused on bridging the gap between advanced mathematical models and high-performance software implementation.

---
**Contact**: Maéva Cavaleri - [cavalerimaeva@gmail.com](mailto:cavalerimaeva@gmail.com)
