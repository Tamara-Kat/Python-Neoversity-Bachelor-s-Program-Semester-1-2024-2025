n = 7000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

print(f"hours: {hours}, minute: {minutes}, seconds: {seconds}")
