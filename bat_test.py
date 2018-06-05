from subprocess import Popen
process = Popen("test.cmd", cwd=r"C:\Integrity_Test\TestGenius\Integrity")
stdout, stderr = process.communicate()
