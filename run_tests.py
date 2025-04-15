import os
import subprocess
import sys
from datetime import datetime

results = []

for subdir, dirs, files in os.walk("tests"):
    for library in dirs:
        newest = False
        versions = open("tests/%s/versions.txt"%library).readlines()
        if len(versions) == 0:
            newest = True
            versions.append('newest')
        subprocess.run(['pip', 'cache', 'purge'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['pip', 'uninstall', '-y', library], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for v in versions:
            v = v.strip()

            print("Testing %s version %s"%(library, v))

            install_result = "NO_INSTALL"
            test_result = ""
            uninstall_result = ""
            security_result = ""

            # First, attempt to install.
            if v == 'newest':
                xx = subprocess.run(['pip', 'index', 'versions', "%s"%(library)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                v = xx.stdout.decode("utf-8").splitlines()[0].split('(')[1].split(')')[0]
                x = subprocess.run(['pip', 'install', "%s"%(library)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                x = subprocess.run(['pip', 'install', "%s==%s"%(library,v)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if x.returncode != 0:
                install_result = "INSTALL_FAILED"
                print(x.stdout.decode("utf-8"))
            else:
                install_result = "INSTALL_PASSED"
            
                # Second, run tests
                y = subprocess.run(['python', '-m', 'pytest', 'tests/%s'%library])
                if y.returncode != 0:
                    test_result = "TESTS_FAILED"
                else:
                    test_result = "TESTS_PASSED"

                q = subprocess.run(['pip-audit'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                security_result = "NO_VULNERABILITIES"
                for line in q.stdout.decode("utf-8").splitlines():
                    if line.startswith(library):
                        security_result = "VULNERABILITIES_FOUND"




                # Finally, uninstall.
                z = subprocess.run(['pip', 'uninstall', '-y', library], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if z.returncode == 0:
                    print("uninstalled")
                    uninstall_result = ""
                else:
                    uninstall_result = "DEFAULT"


            results.append("%s;%s;%s;%s;%s;%s"%(library, v, install_result, test_result, uninstall_result, security_result))
    break

results.sort()


ofile = open('goodlist.md', 'w')
ofile.write("""| Package | Version | Installs | Validated[^1] | Vulnerability Scan[^2] |
| ------- | ------- | -------- | ------------- | ---------------------- |
"""            
            )
for r in results:
    l, v, i, t, u, s = r.split(';')
    default = False
    if u == "DEFAULT":
        default = True
        l = "**"+l+"**"
        v = "**"+v+"**"

    io = ""
    to = ""
    so = ""

    if i == "INSTALL_PASSED":
        io = "✅"
        if t == "TESTS_PASSED":
            to = "✅"
        else:
            to = "❌"
        if s == "VULNERABILITIES_FOUND":
            so = "❌"
        else:      
            so = "✅" 
    else:
        io = "❌"


    ofile.write("| %s | %s | %s | %s | %s |\n"%(l,v,io,to,so))

ofile.write("""

[^1]: A component is "validated" if all of the tests in its respective test case folder run without any errors or failed assertions. It is possible that there are use cases not covered by the test cases, so compatibility is suggested, not guaranteed. If you encounter incompatibility when using a library, please report it so we can update our test cases!

[^2]:  Vulnerability results pass if there are no high or critical CVEs for the component as of %s per the results of the scanning tool "pip-audit".
"""%datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
ofile.close()




