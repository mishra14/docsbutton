define([
    'base/js/namespace',
    'jquery',
    'base/js/utils',
    'base/js/dialog'
], function(Jupyter, $, utils, dialog) {

    function accept_liveshare() {
        console.log("Sending get req for liveshare")
        var pizzaUrl = utils.url_path_join(utils.get_body_data('baseUrl'), 'liveshare')
        console.log("liveshare request url: ", pizzaUrl)
        $.getJSON(pizzaUrl, function(data) {
            console.log("Data: ", data)
            dialog.modal(data)
        })
    }

    function place_button() {
	if (!Jupyter.toolbar) {
	    $([Jupyter.events]).on("app_initialized.NotebookApp", place_button);
	    return;
    }
    
	Jupyter.toolbar.add_buttons_group([{
	    label: 'LiveShare',
	    icon: 'fa-share',
	    callback: accept_liveshare
	}])
    }

    function load_ipython_extension() {
        console.log("LiveShare: Loading liveshare jupyter extension")
	    place_button();
    }

    return {
	load_ipython_extension: load_ipython_extension
    };

});
