import tests.test_is_type
import tests.test_validate
import doctest

total = 0
failed = 0

results = doctest.testmod(tests.test_is_type)
total += results.attempted
failed += results.failed

results = doctest.testmod(tests.test_validate)
total += results.attempted
failed += results.failed

print(f"Passed {total - failed}/{total} tests")

# Hopefully this will cause the github action to fail if any tests fail
if failed > 0:
	exit(1)