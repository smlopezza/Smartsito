$(document).ready(function() {
// https://www.codeply.com/go/7XYosZ7VH5
  // Hide submenus
$('#body-row .collapse').collapse('hide');

// Collapse/Expand icon
$('#collapse-icon').addClass('fa-angle-double-left');

// Collapse click
$('[data-toggle=sidebar-colapse]').click(function() {
    SidebarCollapse();
});

function SidebarCollapse () {
    $('.menu-collapsed').toggleClass('d-none');
    $('.sidebar-submenu').toggleClass('d-none');
    $('.submenu-icon').toggleClass('d-none');
    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');

    // Treating d-flex/d-none on separators with title
    var SeparatorTitle = $('.sidebar-separator-title');
    if ( SeparatorTitle.hasClass('d-flex') ) {
        SeparatorTitle.removeClass('d-flex');
    } else {
        SeparatorTitle.addClass('d-flex');
    }

    // Collapse/Expand icon
    $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
}

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
