from django.shortcuts import render

from practices.api import ApiError, get_json


DOG_API = "https://dog.ceo/api"


def dog_breeds():
    breeds = get_json(f"{DOG_API}/breeds/list/all")["message"]
    names = [f"{breed}/{subbreed}" for breed, subbreeds in breeds.items() for subbreed in subbreeds]
    return sorted([*breeds, *names])


def dog_photo(breed):
    return get_json(f"{DOG_API}/breed/{breed}/images/random")["message"]


def dog_gallery(request):
    query = request.GET.get("breeds", "")
    selected = dict.fromkeys(breed.strip().lower() for breed in query.split(",") if breed.strip())
    breeds = []
    photos = []
    errors = []
    try:
        breeds = dog_breeds()
    except ApiError as error:
        errors.append(str(error))
    else:
        for breed in selected:
            if breed not in breeds:
                errors.append(f"Неизвестная порода: {breed}.")
                continue
            try:
                photos.append((breed, dog_photo(breed)))
            except ApiError as error:
                errors.append(f"{breed}: {error}")

    return render(request, "catalog/dogs.html", {
        "breeds": breeds,
        "query": query,
        "photos": photos,
        "errors": errors,
    })
