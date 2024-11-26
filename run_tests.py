import os
import subprocess
import sys

results = []

for subdir, dirs, files in os.walk("tests"):
    for library in dirs:
        versions = open("tests/%s/versions.txt"%library).readlines()
        subprocess.run(['pip', 'uninstall', '-y', library], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for v in versions:
            v = v.strip()
            print("Testing %s version %s"%(library, v))

            install_result = "NO_INSTALL"
            test_result = ""
            uninstall_result = ""
            security_result = ""

            # First, attempt to install.
            x = subprocess.run(['pip', 'install', "%s==%s"%(library,v)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if x.returncode != 0:
                install_result = "INSTALL_FAILED"
            else:
                install_result = "" #"INSTALL_PASSED"
            
                # Second, run tests
                y = subprocess.run(['python', '-m', 'pytest', 'tests/%s'%library])
                if y.returncode != 0:
                    test_result = "TESTS_FAILED"
                else:
                    test_result = "TESTS_PASSED"

                q = subprocess.run(['pip-audit'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in q.stdout.decode("utf-8").splitlines():
                    if line.startswith(library):
                        security_result = "VULNERABILITIES_FOUND"




                # Finally, uninstall.
                z = subprocess.run(['pip', 'uninstall', '-y', library], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if z.returncode == 0:
                    pass #uninstall_result = "UNINSTALL_PASSED"
                else:
                    uninstall_result = "UNINSTALL_FAILED"


            results.append("%s %s %s %s %s %s"%(library, v, install_result, test_result, uninstall_result, security_result))
    break

print("")
print("FINAL RESULTS")
print("=============")
for r in results:
    print(r)