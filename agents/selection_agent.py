def get_selection_result(
    score
):

    if score >= 8:

        return "SELECTED"

    elif score >= 6:

        return "BORDERLINE"

    else:

        return "NOT SELECTED"