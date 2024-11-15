"""Ping"""
def gettime(line):
    """Get MS"""
    if line.count("time="):
        start = line.find("time=")
        end = line.find("ms")
        return int(line[start + 5:end])
    return "Nofound"
def main():
    """Ping"""
    ping = input()
    input()
    line1 = input()
    line2 = input().replace("<1", "=0")
    line3 = input().replace("<1", "=0")
    line4 = input().replace("<1", "=0")
    line5 = input().replace("<1", "=0")
    var_ip = ""
    if not ping[ping.find("ping ") + 5:][0].isdigit():
        f_ip = line1.find("[")
        b_ip = line1.find("]")
        var_ip = line1[f_ip + 1:b_ip]
    else:
        var_ip = ping[ping.find("ping ") + 5:]
    sus = (line2 + line3 + line4 + line5).count(var_ip)
    percentloss = (4 - sus) * 25
    print(f"Ping statistics for {var_ip}:")
    print(f"    Packets: Sent = 4, Received = {sus}, Lost = {4 - sus} ({percentloss}% loss),")
    timeee = [gettime(line2), gettime(line3), gettime(line4), gettime(line5)]
    for _ in range(timeee.count("Nofound")):
        timeee.remove("Nofound")
    if len(timeee) > 0:
        print("Approximate round trip times in milli-seconds:")
        mac = max(timeee)
        meen = min(timeee)
        avg = int(sum(timeee) / len(timeee))
        print(f"    Minimum = {meen}ms, Maximum = {mac}ms, Average = {avg}ms")
main()
