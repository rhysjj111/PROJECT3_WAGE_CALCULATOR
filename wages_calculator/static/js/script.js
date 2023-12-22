document.addEventListener('DOMContentLoaded', function() {
    // collapsible initialization
    const collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

    // modal initialization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"},
        disableDayFn: function(date){
            if(document.querySelector('#wages_date') != null){
                if(date.getDay() == 1){
                return false;
                } else {
                return true;
                };
            }   
        }
    })

    // select initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    function removeTabs() {
        const subTabs = document.querySelector('#sub-menu-tabs')
        if (subTabs) {
            const tabs = M.Tabs.init(subTabs, swipeable=true);
            if(window.innerWidth > 992){
                tabs.destroy();
            } else {
                tabs;
            }
        }
    }
    window.onresize = removeTabs;
    removeTabs();
    
});
