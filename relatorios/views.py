from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from equipamentos.models import Maquina
from impressoras.models import Impressora
from nobreaks.models import Nobreak


@login_required
def rel_equipamentos(request):
    '''EQUIPAMENTOS'''

    count_hp402 = Maquina.objects.filter(modelo='1').count()
    count_pro_one = Maquina.objects.filter(modelo='2').count()
    count_itautec = Maquina.objects.filter(modelo='3').count()
    
    '''IMPRESSORAS'''
    count_l455 = Impressora.objects.filter(modelo='Epson L455').count()
    count_hp2055dn = Impressora.objects.filter(modelo='HP 2055dn').count()
    count_hp2015 = Impressora.objects.filter(modelo='HP 2015').count()
    count_hp1200 = Impressora.objects.filter(modelo='HP 1200').count()
    count_hpj2010 = Impressora.objects.filter(modelo='HP j2010').count()
    count_hpm201 = Impressora.objects.filter(modelo='HP M201').count()
    count_hpdesk2546 = Impressora.objects.filter(modelo='HP DESKJET 2546').count()
    count_hpcm1410 = Impressora.objects.filter(modelo='HP CM1410').count()
    count_hpdesk895 = Impressora.objects.filter(modelo='HP DESKJET 895').count()
    count_hppro400 = Impressora.objects.filter(modelo='HP PRO400').count()   
    '''NOBREAKS'''
    count_rag = Nobreak.objects.filter(modelo_nobreak='1').count()
    count_apc = Nobreak.objects.filter(modelo_nobreak='2').count()
    '''SISTEMA OPERACIONAL'''
    count_so_xp = Maquina.objects.filter(sistema='1').count()
    count_so7 = Maquina.objects.filter(sistema='2').count()
    count_so8 = Maquina.objects.filter(sistema='3').count()
    count_so10 = Maquina.objects.filter(sistema='4').count()
    
    return render(request,'relatorios.html', {
                                              'count_hp402': count_hp402,
                                              'count_pro_one': count_pro_one,
                                              'count_itautec': count_itautec,

                                              'count_hp2055dn': count_hp2055dn,
                                              'count_l455': count_l455,
                                              'count_hp2015': count_hp2015,
                                              'count_hp1200': count_hp1200,
                                              'count_hpj2010': count_hpj2010,
                                              'count_hpm201': count_hpm201,
                                              'count_hpdesk2546': count_hpdesk2546,
                                              'count_hpcm1410': count_hpcm1410,
                                              'count_hpdesk895': count_hpdesk895,
                                              'count_hppro400': count_hppro400,

                                              'count_rag': count_rag,
                                              'count_apc': count_apc,

                                              'count_so_xp': count_so_xp,
                                              'count_so7': count_so7,
                                              'count_so8': count_so8,
                                              'count_so10': count_so10,
                                                                                            
                                              })
