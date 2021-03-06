import ctypes
from base import Output

class PCTalker(Output):
 lib32 = 'pctkusr.dll'
 lib64 = 'pctkusr64.dll'

 def speak(self, text, interrupt=False):
  if interrupt:
   self.silence()
  self.lib.PCTKPRead(text.encode('cp932', 'replace'))

 def silence(self):
  self.lib.PCTKVReset()

 def is_active(self):
  return self.lib.PCTKStatus() != 0

output_class = PCTalker
