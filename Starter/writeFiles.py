contents = ["Core Java, Java 8+ and Spring Boot", "Python fundamentals, Python for Machine Learning & AI",
            "Docker, Kubernetes for Cloud Computing"]

fileNames = ["java.txt", "python.txt", "devOps.txt"]

for content, fileName in zip(contents, fileNames):
    file = open(f"files/{fileName}", "w")
    file.write(content)
    file.close()

file = open("files/test.txt", "w")
file.write("Test Data")
file.close()

for fileName in fileNames:
    file = open(f"files/{fileName}", "r")
    content = file.read()
    print(content)
