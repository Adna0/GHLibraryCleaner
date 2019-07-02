import re
array = []
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    lines = [x.strip() for x in lines]
    for line in lines:
        if line and line[0] != "*":
            if "<b>" in line:
                array.append("\n"+re.sub(r'<.*?>', '', re.search(r'<b>[a-zA-Z0-9_.+-]+</b>', line).group(0))+"\nRequirements:")
            if line[:2] == "0x":
                array.append("\n"+line)
        else:
            if "active index user" in line:
                array.append("Active Index 0 User")
            if "active connection" in line:
                array.append("Active Connection")
            if "registered users" in line:
                array.append("Registered Users : "+re.search(r'\d', line).group(0))
            if "Using namespace" in line:
                array.append(re.sub(r'<.*?>', '',re.search(r'<b>[a-zA-Z_.]+</b>', line).group(0))+" "+re.sub(r'<.*?>', '', re.search(r'version <b>\d\.\d\.\d</b>', line).group(0)))
            if "port" in line:
                array.append("Active Ports : "+re.search(r'\d', line).group(0))

with open('output.txt', 'w') as output_file:
    output_file.write("\n".join(array))
print("All Done!")