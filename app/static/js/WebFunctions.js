$(document).ready(function() {

  var tableStore = $('#RetailerStore').DataTable({
    "retrieve": true,
    "stateSave": true,  // to save pagination on refresh
    "scrollY": "50vh",
    "scrollCollapse": true,
    "ordering": true,
    dom: "frt",
    //"autoWidth": true,
    'order': [[0, 'asc']],
    "columnDefs": [
    {"className": "dt-center", "targets": "_all"}
  ]

  });


  var tableSavings = $('#SavingsConsumer').DataTable({
    "retrieve": true,
    "stateSave": true,  // to save pagination on refresh
    "scrollY": "50vh",
    "scrollCollapse": true,
    "ordering": true,
    dom: "frt",
    //"autoWidth": true,
    'order': [[0, 'asc']],
    "columnDefs": [
    {"className": "dt-center", "targets": "_all"}
  ]

  



  });

});
