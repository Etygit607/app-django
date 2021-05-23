def amount(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total = total + (float(value["price"]) * value["lot"])
    return {"amount_total":total}