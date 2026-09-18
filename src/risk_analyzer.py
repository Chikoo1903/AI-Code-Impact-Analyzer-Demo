def calculate_risk(score, blockers=0, overdue_tasks=0, critical_bugs=0):

    if critical_bugs > 0:
        return "Critical"

    if blockers >= 3:
        return "Critical"

    if overdue_tasks >= 5:
        return "Critical"

    if score >= 9:
        return "Critical"

    if score >= 7:
        return "High"

    if score >= 4:
        return "Medium"

    return "Low"