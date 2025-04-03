import math
import scipy.stats as st

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the European call option price using the Black-Scholes formula.
    
    Parameters:
      S (float): Current stock price
      K (float): Strike price
      T (float): Time to expiration (in years)
      r (float): Risk-free interest rate (annualized)
      sigma (float): Volatility of the underlying stock (annualized)
      
    Returns:
      float: Call option price
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    call_price = S * st.norm.cdf(d1) - K * math.exp(-r * T) * st.norm.cdf(d2)
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """
    Calculate the European put option price using the Black-Scholes formula.
    
    Parameters:
      S (float): Current stock price
      K (float): Strike price
      T (float): Time to expiration (in years)
      r (float): Risk-free interest rate (annualized)
      sigma (float): Volatility of the underlying stock (annualized)
      
    Returns:
      float: Put option price
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    put_price = K * math.exp(-r * T) * st.norm.cdf(-d2) - S * st.norm.cdf(-d1)
    return put_price

# Example usage:
S = 100      # Current stock price
K = 100      # Strike price
T = 1        # Time to expiration in years
r = 0.05     # Risk-free rate (5%)
sigma = 0.2  # Volatility (20%)

call = black_scholes_call(S, K, T, r, sigma)
put = black_scholes_put(S, K, T, r, sigma)

print(f"European Call Option Price: {call:.2f}")
print(f"European Put Option Price: {put:.2f}")
