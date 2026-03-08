def fibonacci(n: int) -> int:
	"""Return the nth Fibonacci number using recursion."""
	if not isinstance(n, int):
		raise TypeError("n must be an integer")
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)
