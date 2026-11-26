def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    aam, aad = [int(v) for v in arriveAlice.split("-")]
    alm, ald = [int(v) for v in leaveAlice.split("-")]
    bam, bad = [int(v) for v in arriveBob.split("-")]
    blm, bld = [int(v) for v in leaveBob.split("-")]

    aa = sum(days_of_month[:aam]) + aad
    al = sum(days_of_month[:alm]) + ald
    ba = sum(days_of_month[:bam]) + bad
    bl = sum(days_of_month[:blm]) + bld

    l = [aa,al,ba,bl]
    l.sort()
    if (l[0] == aa and l[1] == al) or (l[0] == ba and l[1] == bl):
        return 0 if al != ba and bl != aa else 1
    return l[2] - l[1] + 1