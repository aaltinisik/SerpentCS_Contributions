/*global Highcharts*/
odoo.define("web_lead_funnel_chart.web_lead_funnel_chart", function(require) {
    "use strict";

    var core = require("web.core");
<<<<<<< HEAD
    var dataset = require("web.data");
    var Widget = require("web.Widget");
    var WebClient = require('web.web_client');
    var Session = require('web.session');
=======
    var AbstractAction = require("web.AbstractAction");
    var ajax = require('web.ajax');
    var Session = require('web.session');

>>>>>>> upstream/12.0
    var _t = core._t;

    var web_lead_funnel_chart = AbstractAction.extend({
        template: "FunnelChart",
        xmlDependencies: ['web_lead_funnel_chart/static/src/xml/web_funnel_chart.xml'],
        start: function() {
            var self = this;
<<<<<<< HEAD
            self.crm_lead_dataset = new dataset.DataSetSearch(self, "crm.lead", {}, []);
            self.crm_lead_dataset.call("get_lead_stage_data", [
                []
            ]).done(function(callbacks) {
=======
            var emp_child = [];
            ajax.jsonRpc('/web/dataset/call_kw', 'call', {
                model:  'crm.lead',
                method: 'get_lead_stage_data',
                args: [[]],
                kwargs: {
                },
            }).then(function (callbacks) {
>>>>>>> upstream/12.0
                self.CrmFunnelChart = Highcharts.chart("container",{
                    chart: {
                        type: "funnel",
                        marginRight: 100
                    },
                    title: {
                        text: _t("Lead/Opportunity Funnel Chart"),
                        x: -50
                    },
                    plotOptions: {
                        series: {
                            dataLabels: {
                                enabled: true,
                                format: "<b>{point.name}</b>({point.y:,.0f})",
                                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || "black",
                                softConnector: true
                            },
                            neckWidth: "30%",
                            neckHeight: "25%"

                            //-- Other available options
                            // height: pixels or percent
                            // width: pixels or percent
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    series: [{
                        name: _t("Number Of Leads"),
                        data: callbacks
                    }]
                });
<<<<<<< HEAD
                    var funnel_container = self.CrmFunnelChart.container;
                    return self.rpc("/web/action/load", {action_id: "crm.crm_lead_opportunities_tree_view"}).done(function(result) {
                        funnel_container.onclick = function (event) {
                            if(event.path[0].point !== undefined) {
                                var crm_stage = event.path[0].point.name;
                                result.display_name = _t(crm_stage);
                                result.view_type = "list";
                                result.view_mode = "list";
                                result.menu_id = 126;
                                result.flags = {
                                        search_view: true,
                                        display_title: true,
                                        pager: true,
                                        list: {selectable: true}
                                }
                                result.views = [[false, "list"], [false, "form"],[false,"kanban"],[false,"calendar"],[false,"pivot"],[false,"graph"]];
                                result.domain = [['stage_id.name', '=', _t(crm_stage)]];
                                result.filter = true;
                                result.target = 'current';
                                result.context = {'default_user_id': Session.uid};
                                return WebClient.action_manager.do_action(result);
                            }
                        }
                   });
=======
                var funnel_container = self.CrmFunnelChart.container;
                return self._rpc({route: '/web/action/load',params: {
                    action_id: "crm.crm_lead_opportunities_tree_view",
                }}).done(function(result){
                    funnel_container.onclick = function (event) {
                        if(event.composedPath()[0].point !== undefined) {
                            var crm_stage = event.composedPath()[0].point.name;
                            result.display_name = _t(crm_stage);
                            result.view_type = "list";
                            result.view_mode = "list";
                            result.menu_id = 126;
                            result.flags = {
                                    search_view: true,
                                    display_title: true,
                                    pager: true,
                                    list: {selectable: true}
                            }
                            result.views = [[false, "list"], [false, "form"],[false,"kanban"],[false,"calendar"],[false,"pivot"],[false,"graph"]];
                            result.domain = [['stage_id.name', '=', _t(crm_stage)]];
                            result.filter = true;
                            result.target = 'current';
                            result.context = {'default_user_id': Session.uid};
                            return self.do_action(result,{
                                on_reverse_breadcrumb: function(){
                                    self.start();
                                }
                            });
                        }
                    }
                });
>>>>>>> upstream/12.0
            });
        },
    });
    
    core.action_registry.add("web_lead_funnel_chart.funnel", web_lead_funnel_chart);

});
