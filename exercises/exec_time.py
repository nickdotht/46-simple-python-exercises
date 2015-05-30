def exec_time(func):
	import timeit
	def wrapper(*args, **kwargs):
		start_time = timeit.default_timer()
		res = func(*args, **kwargs)
		elapsed = timeit.default_timer() - start_time
		print 'Elapsed time: %f' % elapsed
		return res
	return wrapper