def urgency(deadline, now, duration_min, horizon_h):
    if deadline is None:
        return 0.0
    slack_h = (deadline - now).total_seconds() / 3600 - duration_min / 60
    return min(1.0, max(0.0, 1 - slack_h / horizon_h))