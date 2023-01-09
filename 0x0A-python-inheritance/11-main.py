root@78503a328c25:/alx-higher_level_programming/0x0A-python-inheritance# cat > 11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
