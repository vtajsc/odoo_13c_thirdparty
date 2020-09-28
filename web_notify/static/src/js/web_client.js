odoo.define('web_notify.WebClient', function (require) {
    "use strict";

    var WebClient = require('web.WebClient');
    var base_bus = require('bus.Longpolling');
    var session = require('web.session');
    require('bus.BusService');


    WebClient.include({
        show_application: function () {
            var res = this._super();
            this.start_polling();
            return res;
        },
        start_polling: function () {
            this.channel_success = 'notify_success_' + session.uid;
            this.channel_danger = 'notify_danger_' + session.uid;
            this.channel_warning = 'notify_warning_' + session.uid;
            this.channel_info = 'notify_info_' + session.uid;
            this.channel_default = 'notify_default_' + session.uid;
            this.all_channels = [
                this.channel_success,
                this.channel_danger,
                this.channel_warning,
                this.channel_info,
                this.channel_default,
            ];

            // startPolling to get this new tab registered,
            // in order to be able to call isMasterTab
            this.call('bus_service', 'startPolling');

            // - no need to add channels again if it was done already
            // - this is also a workaround for the infinite loop issue
            //   that occures when user logs in as a different user
            //   while still being logged in 2+ other tabs
            if(this.call('bus_service', 'isMasterTab')) {
                this.call('bus_service', 'addChannel', this.channel_success);
                this.call('bus_service', 'addChannel', this.channel_danger);
                this.call('bus_service', 'addChannel', this.channel_warning);
                this.call('bus_service', 'addChannel', this.channel_info);
                this.call('bus_service', 'addChannel', this.channel_default);
            }

            this.call(
                'bus_service', 'on', 'notification',
                this, this.bus_notification);
        },
        bus_notification: function (notifications) {
            var self = this;
            _.each(notifications, function (notification) {
                var channel = notification[0];
                var message = notification[1];
                if (
                    self.all_channels != null &&
                    self.all_channels.indexOf(channel) > -1
                ) {
                    self.on_message(message);
                }
            });
        },
        on_message: function (message) {
            _audio: null;
            if (!this._audio) {
                this._audio = new Audio();
                var ext = this._audio.canPlayType("audio/ogg; codecs=vorbis") ? ".ogg" : ".mp3";
                var session = this.getSession();
                this._audio.src = session.url("/web_notify/static/src/audio/notify" + ext);
            }
            this._audio.play();
            return this.call(
                'notification', 'notify', {
                    type: message.type,
                    title: message.title,
                    message: message.message,
                    sticky: message.sticky,
                    className: message.className,
                }
            );
        },
    });

});
