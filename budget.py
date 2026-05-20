def allocate_budget(total_budget):

    return {
        "Hotel": total_budget * 0.40,
        "Food": total_budget * 0.20,
        "Transport": total_budget * 0.20,
        "Sightseeing": total_budget * 0.15,
        "Emergency": total_budget * 0.05
    }