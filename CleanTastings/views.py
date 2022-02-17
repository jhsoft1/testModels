from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import EveningWhisky, Tasting


def valued(request, eveningwhisky_id):
    eveningwhisky = get_object_or_404(EveningWhisky, pk=eveningwhisky_id)
    try:
        nose = request.POST['nose']
        taste = request.POST['taste']
        # if exists(eveningwhisky.tasting_set.get(user=request.user)):update
        new_tasting = eveningwhisky.tasting_set.create(nose=nose, taste=taste, user=request.user)
    except Exception:
        print('Exception', nose, taste, request.user)  # , new_tasting)
    else:
        return HttpResponseRedirect(reverse('CleanTastings:results', args=(eveningwhisky.id,)))


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/Question_detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    # template_name = 'CleanTastings/EveningWhisky_list.html'
    context_object_name = 'todays_whiskies_list'

    def get_queryset(self):
        """Return todays whiskies."""
        return EveningWhisky.objects.filter(evening__date__exact=date.today())


class DetailView(generic.DetailView):
    model = EveningWhisky
    # template_name = 'CleanTastings/EveningWhisky_detail.html'


class ResultsView(generic.ListView):
    template_name = 'CleanTastings/Tasting_list.html'
    context_object_name = 'my_todays_tastings_list'

    def get_queryset(self):
        """Return my todays tastings."""
        return Tasting.objects.filter(evening_whisky__evening__date__exact=date.today())  # User fehlt
