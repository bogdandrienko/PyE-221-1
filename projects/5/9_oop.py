# class Meter():
#     def __init__(self, dev):
#         self.dev = dev
#     def __enter__(self):
#         #ttysetattr etc goes here before opening and returning the file object
#         self.fd = open(self.dev, MODE)
#         return self
#     def __exit__(self, type, value, traceback):
#         #Exception handling here
#         close(self.fd)
#
# meter = Meter('dev/tty0')
# with meter as m:
#     #here you work with the file object.
#     m.fd.read()

