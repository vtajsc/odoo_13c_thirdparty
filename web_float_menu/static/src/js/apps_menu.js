odoo.define('web_float_menu', function(require) {
"use strict";

var AppsMenu = require('web.AppsMenu');

AppsMenu.include({
    init: function(parent, menuData) {
        this._super.apply(this, arguments);
        this._apps.forEach((app, index) => {
            app.is_float = menuData.children[index].is_float;
        });
    }
});

});
