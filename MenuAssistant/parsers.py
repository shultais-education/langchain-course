from MenuAssistant.schemas import GeneratedMenu


def sort_dishes(menu: GeneratedMenu):
    return sorted(menu.dishes)
