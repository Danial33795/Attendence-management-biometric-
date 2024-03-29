import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

class MyFingerprint(PyFingerprint):
    def searchTemplate(self):
        # Your custom search code here
        return super().searchTemplate()

# Initialize the fingerprint sensor
f = MyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

# Check if the fingerprint sensor is ready
if not f.verifyPassword():
    raise ValueError('The given fingerprint sensor password is wrong!')

# Search for a fingerprint template
try:
    print('Waiting for finger...')
    while not f.readImage():
        pass
    f.convertImage(0x01)
    result = f.searchTemplate()
    position = result[0]
    print('Found template at position #' + str(position))

# If no fingerprint template is found, exit
except Exception as e:
    print('No matching template found')
    exit(1)

# Hash the fingerprint template
template = f.loadTemplate(position)
print('Fingerprint template loaded')
print('The hash of the template is:')
print(hashlib.sha256(template).hexdigest())
