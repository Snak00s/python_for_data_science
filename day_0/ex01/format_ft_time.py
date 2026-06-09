import time
import datetime

int_ns = time.time()
print("Seconds since January 1, 1970:", f"{int_ns:,.4f}", "or", f"{int_ns:.2e}", "in scientific notation")

timestruct = time.localtime()
print(time.asctime().split()[1], timestruct.tm_mday, timestruct.tm_year)