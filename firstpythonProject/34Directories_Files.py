from pathlib import Path

p = Path()
# p.mkdir()
# p.rmdir()
for f in p.glob('*'):
    print(f)