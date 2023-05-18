from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {'lista_filmes_recentes': lista_filmes, 'filme_destaque': filme_destaque}


def lista_filmes_popular(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {'lista_filmes_popular': lista_filmes}
