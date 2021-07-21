
var remove = $(".repetir-campo_remover").click(removeResposta);
var mostrarescondertag = $(".esconder-tag").click(esconderMostrar);
var mostrar = $('#sidebarCollapse').click(mostrarEsconder);




$("input[name='pegarComponente']").on('input', function(){
    var selected = $(this).val();
    console.log("teste");
});
function esconderMostrar (){
  $(".select-span").toggle();
}

function removeResposta(){
  $(this).parent().remove();
}

function mostrarEsconder(){
  $('#sidebar').toggleClass('active');
}
