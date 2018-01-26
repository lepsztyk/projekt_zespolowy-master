# Skopiować do widoków










def edit_issuer(request, issuer_id):
    try:
        this_item = Wystawca.objects.get(id=issuer_id)
        context = {'this_item': this_item}
    except Wystawca.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Taki wystawca nie istnieje!')
        return redirect('index')
    if (request.user.groups.filter(name='Pracownik').exists()):
        if request.method == 'POST':
            form = WystawcaForm(request.POST, instance=this_item)
            if form.is_valid():
                post = form.save(commit=False)
                post.nazwa = request.POST.get('nazwa')
                post.kod_pocztowy = request.POST.get('kod_pocztowy')
                post.miasto = request.POST.get('miasto')
                post.ulica = request.POST.get('ulica')
                post.telefon = request.POST.get('telefon')
                post.email = request.POST.get('email')
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano wystawce!')
                return redirect('issuers', issuer_id=post.id)
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_issuer.html', context)


def edit_owner(request, owner_id):
    try:
        this_item = Wlasciciel.objects.get(id=owner_id)
        context = {'this_item': this_item}
    except Wlasciciel.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Taki właściciel nie istnieje!')
        return redirect('index')
    flat_list = Mieszkanie.objects.all()
    context = {'flat_list': flat_list}
    if (request.user.groups.filter(name='Pracownik').exists()):
        if request.method == 'POST':
            form = WlascicielForm(request.POST, instance=this_item)
            if form.is_valid():
                post = form.save(commit=False)
                post.imie = request.POST.get('imie')
                post.nazwisko = request.POST.get('nazwisko')
                post.telefon = request.POST.get('telefon')
                post.email = request.POST.get('email')
                post.mieszkanie.id = int(request.POST.get('mieszkanie'))
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano właściciela!')
                return redirect('owners', owner_id=post.id)
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_owner.html', context)


def edit_counter(request, counter_id):
    try:
        this_item = Licznik.objects.get(id=counter_id)
        context = {'this_item': this_item}
    except Licznik.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Taki licznik nie istnieje!')
        return redirect('index')
    if (request.user.groups.filter(name='Pracownik').exists()):
        if request.method == 'POST':
            form = LicznikForm(request.POST, instance=this_item)
            if form.is_valid():
                post = form.save(commit=False)
                post.typ = request.POST.get('typ')
                post.cena_netto = float(request.POST.get('cena_netto'))
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano licznik!')
                return redirect('counter', counter_id=post.id)
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_counter.html', context)


def edit_counter_state(request, counter_state_id):
    try:
        this_item = StanLicznik.objects.get(id=counter_state_id)
        context = {'this_item': this_item}
    except StanLicznik.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Taki stan licznika nie istnieje!')
        return redirect('index')
    if (request.user.groups.filter(name='Pracownik').exists()):
        counters_list = Licznik.objects.all()
        flat_list = Mieszkanie.objects.all()
        context = {'counters_list': counters_list, 'flat_list': flat_list}
        if request.method == 'POST':
            form = StanLicznikForm(request.POST, instance=this_item)
            if form.is_valid():
                post = form.save(commit=False)
                post.typ.id = int(request.POST.get('typ'))
                post.mieszkanie.id = int(request.POST.get('mieszkanie'))
                post.stan = float(request.POST.get('stan'))
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano stan licznika!')
                return redirect('counter_state', counter_state_id=post.id)
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_counter_state.html', context)


def edit_worker(request, worker_id):
    try:
        this_item = Pracownik.objects.get(id=worker_id)
        context = {'this_item': this_item}
    except Pracownik.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Takie pracownik nie istnieje!')
        return redirect('index')
    table = {
        ord('ą'): 'a',
        ord('ć'): 'c',
        ord('ę'): 'e',
        ord('ł'): 'l',
        ord('ń'): 'n',
        ord('ó'): 'o',
        ord('ś'): 's',
        ord('ź'): 'z',
        ord('ż'): 'z',
        ord('Ą'): 'A',
        ord('Ć'): 'C',
        ord('Ę'): 'E',
        ord('Ł'): 'L',
        ord('Ń'): 'N',
        ord('Ó'): 'O',
        ord('Ś'): 'S',
        ord('Ź'): 'Z',
        ord('Ż'): 'Z',
    }
    position_list = Stanowisko.objects.all()
    address_list = Adres.objects.all()
    groups = Group.objects.all()
    context = {'position_list': position_list, 'address_list': address_list, 'groups': groups}
    if (request.user.groups.filter(name='Pracownik').exists()):
        if request.method == 'POST':
            form = PracownikForm(request.POST, instance=this_item)
            if form.is_valid():
                username = request.POST.get('imie')[:1] + request.POST.get('nazwisko')
                username.translate(table)
                user, created = User.objects.get_or_create(username=username.lower())
                while not created:
                    i = 1
                    user, created = User.objects.get_or_create(username=username.lower() + str(i))
                    i += 1
                user.set_password(username.lower() + '!1')
                user.email = request.POST.get('email')
                user.groups.add(int(request.POST.get('stanowisko')))
                user.save()
                post = form.save(commit=False)
                post.imie = request.POST.get('imie')
                post.nazwisko = request.POST.get('nazwisko')
                post.telefon = request.POST.get('telefon')
                post.email = request.POST.get('email')
                post.stanowisko.id = int(request.POST.get('stanowisko'))
                post.adres.id = int(request.POST.get('adres'))
                post.user = user
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano pracownika!')
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_worker.html', context)


def edit_position(request, position_id):
    try:
        this_item = Stanowisko.objects.get(id=position_id)
        context = {'this_item': this_item}
    except Stanowisko.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Takie stanowisko nie istnieje!')
        return redirect('index')
    if (request.user.groups.filter(name='Pracownik').exists()):
        if request.method == 'POST':
            form = StanowiskoForm(request.POST, instance=this_item)
            if form.is_valid():
                group, created = Group.objects.get_or_create(name=request.POST.get('nazwa'))
                if not created:
                    messages.add_message(request, messages.ERROR, 'Podane stanowisko już istnieje!')
                    return redirect('index')
                group.save()
                post = form.save(commit=False)
                post.nazwa = request.POST.get('nazwa')
                post.pensja = request.POST.get('pensja')
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano stanowisko!')
                return redirect('positions', position_id=post.id)
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_position.html', context)


def edit_overtime(request, overtime_id):
    try:
        this_item = Nadgodziny.objects.get(id=overtime_id)
        context = {'this_item': this_item}
    except Nadgodziny.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Takie nadgodziny nie istnieją!')
        return redirect('index')
    if (request.user.groups.filter(name='Pracownik').exists()):
        worker_list = Pracownik.objects.all()
        context = {'worker_list': worker_list}
        if request.method == 'POST':
            form = NadgodzinyForm(request.POST, instance=this_item)
            if form.is_valid():
                post = form.save(commit=False)
                post.ilosc = float(request.POST.get('ilosc'))
                post.pracownik.id = int(request.POST.get('pracownik'))
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Pomyślnie edytowano nadgodziny pracownikowi!')
                return redirect('overtime', overtime=post.id)
            else:
                messages.add_message(request, messages.ERROR, 'Coś poszło nie tak!')
                return redirect('index')
    else:
        messages.add_message(request, messages.ERROR, 'Nie możesz tego zrobić!')
        return redirect('index')
    return render(request, 'add_overtime.html', context)
