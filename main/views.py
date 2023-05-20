from django.shortcuts import render


def calc_func(form_input, request):
    res = None
    if form_input != '':
        is_round = request.POST.get('round')
        try:
            if is_round == 'yes':
                res = round(eval(form_input))
            else:
                res = eval(form_input)
        except ZeroDivisionError:
            res = ZeroDivisionError.__doc__
        except Exception:
            res = 'Incorrect input'
    return res


def index(request):
    equation_res = ''
    if request.method == 'POST':
        equation = request.POST.get('equation')
        equation_res = calc_func(equation, request)
    context = {'equation_res': equation_res}
    return render(request, 'main/index.html', context)
