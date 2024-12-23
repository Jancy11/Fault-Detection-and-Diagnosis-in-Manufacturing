def take_action(root_cause):
    if "pressure" in root_cause:
        return "Adjust pressure settings in the system."
    elif "temperature" in root_cause:
        return "Reduce temperature in the furnace."
    else:
        return "No corrective action needed."
