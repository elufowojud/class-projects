def beasley_reduction(universal_set, subsets):

    # Mandatory subsets list
    mandatory_subsets = []

    # Step 1: Apply the second reduction rule
    # Check for elements in the universal set that are covered by exactly one subset
    element_to_subset = {u: [] for u in universal_set}  # Map each element to subsets containing it
    for i, subset in enumerate(subsets):
        for element in subset:
            element_to_subset[element].append(i)

    for element, subset_indices in element_to_subset.items():
        if len(subset_indices) == 1:  # Element covered by exactly one subset
            mandatory_index = subset_indices[0]
            mandatory_subset = subsets[mandatory_index]
            if mandatory_subset not in mandatory_subsets:
                mandatory_subsets.append(mandatory_subset)

    # Remove elements in mandatory subsets from the universal set
    covered_elements = set()
    for subset in mandatory_subsets:
        covered_elements.update(subset)

    updated_universal_set = [u for u in universal_set if u not in covered_elements]

    # Remove mandatory subsets from the list of subsets
    updated_subsets = [s for s in subsets if s not in mandatory_subsets]

    # Step 2: Apply the first reduction rule
    # Remove subsets that are supersets of other subsets
    non_superset_subsets = []
    for i, subset in enumerate(updated_subsets):
        is_subset = False
        for j, other_subset in enumerate(updated_subsets):
            if i != j and set(subset).issubset(set(other_subset)):
                is_subset = True
                break
        if not is_subset:
            non_superset_subsets.append(subset)

    # Return the updated universal set, updated subsets, and mandatory subsets
    return updated_universal_set, non_superset_subsets, mandatory_subsets


# Example usage
universal_set = [1, 2, 3, 4, 5, 6]
subsets = [
    [1, 2],
    [2, 3, 4],
    [4, 5],
    [1],
    [6],
    [3, 5, 6]
]

updated_u, updated_e, mandatory = beasley_reduction(universal_set, subsets)
print("Updated Universal Set:", updated_u)
print("Updated Subsets:", updated_e)
print("Mandatory Subsets:", mandatory)