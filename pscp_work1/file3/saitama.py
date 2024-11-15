"""saitama"""
import math
def main():
    """main"""
    push_ups = int(input())
    sit_ups = int(input())
    squats = int(input())
    run_km = int(input())
    push_ups_per_day = int(input())
    sit_ups_per_day = int(input())
    run_km_per_day = int(input())
    squats_per_day = int(input())
    days_for_push_ups = math.ceil(push_ups / push_ups_per_day)
    days_for_sit_ups = math.ceil(sit_ups / sit_ups_per_day)
    days_for_run = math.ceil(run_km / run_km_per_day)
    days_for_squats = math.ceil(squats / squats_per_day)
    mi_days = days_for_push_ups
    if days_for_sit_ups > mi_days:
        mi_days = days_for_sit_ups
    if days_for_run > mi_days:
        mi_days = days_for_run
    if days_for_squats > mi_days:
        mi_days = days_for_squats
    print(mi_days)
main()
