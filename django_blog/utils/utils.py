def get_categories_dict(categories, categories_distinct=None):
    categories_dict = {}
    categories_distinct = categories_distinct if categories_distinct else []
    for category in categories:
        if category not in categories_dict:
            if category not in categories_distinct:
                categories_distinct.append(category)
                if category_set := category.category_set.all():
                    categories_dict[category] = get_categories_dict(category_set, categories_distinct)
                else:
                    categories_dict[category] = {}
    return categories_dict
