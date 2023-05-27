odoo.define('Dentistry.odontogram_widget', function (require) {
    'use strict';

    var core = require('web.core');
    var AbstractField = require('web.AbstractField');

    var QWeb = core.qweb;
    var _t = core._t;

    var OdontogramWidget = AbstractField.extend({
        supportedFieldTypes: ['char'],

        // The template for the widget
        template: 'your_module_name.odontogram_widget',

        // Render the widget
        _render: function () {
            this.$el.html(QWeb.render(this.template, {widget: this}));
        },
    });

    core.form_widget_registry.add('odontogram', OdontogramWidget);

    return OdontogramWidget;
});
