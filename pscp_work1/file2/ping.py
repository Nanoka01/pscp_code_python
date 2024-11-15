"""Pign"""
import math
def main():
    """main"""
    Lost = 0
    Received = 0
    l1 = input()
    l2 = input()
    l3 = input()
    l4 = input()
    l5 = input()
    l6 = input()
    l7 = input()
    Reply_count = (l4+l5+l6+l7).count("Reply from")
    Lost = 4-Reply_count
    persent = Lost*25
    Received = Reply_count
    if l3.find("[")>0:
        start_idx = l3.find('[') + 1
        end_idx = l3.find(']')
        ip_address = l3[start_idx:end_idx]
    else:
        start_idx = l3.find('Pinging ') + len('Pinging ')
        end_idx = l3.find(' with')
        ip_address = l3[start_idx:end_idx]

    print(f"Ping statistics for {ip_address}:")
    print(f"    Packets: Sent = 4, Received = {Received}, Lost = {Lost} ({persent}% loss),")
    if persent !=100:
        if l4.count("time=")==1:
            font_l4 = l4.find("time=")+5
            back_l4 = l4.find("ms")
            numl4 = int(l4[font_l4:back_l4])
        else:
            numl4=0
        if l5.count("time=")==1:
            font_l5 = l5.find("time=")+5
            back_l5 = l5.find("ms")
            numl5 = int(l5[font_l5:back_l5])
        else:
            numl5=0
        if l6.count("time=")==1:
            font_l6 = l6.find("time=")+5
            back_l6 = l6.find("ms")
            numl6 = int(l6[font_l6:back_l6])
        else:
            numl6=0
        if l7.count("time=")==1:
            font_l7 = l7.find("time=")+5
            back_l7 = l7.find("ms")
            numl7 = int(l7[font_l7:back_l7])
        else:
            numl7=0
        max_l = max(numl7,numl6,numl5,numl4)
        avg_l =(numl7+numl6+numl5+numl4)/Reply_count
        avg_l = math.floor(avg_l)
        non_zero_times = [n for n in (numl7, numl6, numl5, numl4) if n != 0]
        if non_zero_times:
            min_l = min(non_zero_times)
        else:
            min_l = 0
        print(f"Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {min_l}ms, Maximum = {max_l}ms, Average = {avg_l}ms")
main()
