def pressureGauges(morning, evening):
    return [[ min(a[0], a[1]) for a in zip(morning, evening) ], [max(b[0], b[1]) for b in zip(morning, evening)]]
