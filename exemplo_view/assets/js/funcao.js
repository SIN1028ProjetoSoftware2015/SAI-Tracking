(function($) {

  RemoveTableRow = function(handler) {
    var tr = $(handler).closest('tr');

    tr.fadeOut(400, function(){ 
      tr.remove(); 
    }); 

    return false;
  };
  
  AddTableRow = function() {
      
      var newRow = $("<tr>");
      var cols = "";
      
      cols += '<td><input type="text" name="Sem_ano"></td>';

      cols += '<td><input type="text" name="cod_disc"></td>'; 
      
      cols += '<td><input type="text" name="Cred_carg"></td>'; 

      cols += '<td><input type="text" name="Cod_disc_2"></td>'; 

      cols += '<td><input type="text" name="Cred_carg_2"></td>'; 
      
      cols += '<td class="actions">';
      cols += '<button class="btn btn-large btn-danger" onclick="RemoveTableRow(this)" type="button">Remover</button>';
      cols += '</td>';
      
      newRow.append(cols);
      
      $("#products-table").append(newRow);
    
      return false;
  };
  AddRow = function() {
      
      var novo = $("<tr>");
      var cols = "";
      
      cols += '<td><input type="text" name="cod"></td>';

      cols += '<td><input type="text" name="nome"></td>'; 
      
      cols += '<td><input type="text" name="ant"></td>'; 

      cols += '<td><input type="text" name="prof"></td>'; 

      
      cols += '<td class="actions">';
      cols += '<button class="btn btn-large btn-danger" onclick="RemoveTableRow(this)" type="button">Remover</button>';
      cols += '</td>';
      
      novo.append(cols);
      
      $("#produto-tabela").append(novo);
    
      return false;
  };
  

})(jQuery);