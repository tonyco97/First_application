<template>
  <div>
    <h2>{{$t('dashboard.title')}}</h2>
    <button class="btn btn-default" data-toggle="modal" data-target="#about-modal">Clicca per maggiori informazioni</button>
      <div class="modal fade" id="about-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content about-modal-pf">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                <span class="pficon pficon-close"></span>
              </button>
            </div>
            <div class="modal-body">
              <h1>Prima applicazione  : {{antonioAppName}}</h1>
            </div>
            <div class="modal-footer">
              <img src="/assets/img/logo-alt.svg" alt=" Symbol">
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "Dashboard",
  props: {
  },
  mounted() {
    this.getDashboardData()
  },
  data() {
    return {
      antonioAppName: "",
      uiLoaded: false,  
      errorMessage: null,
      dashboardData: {
        "rspamd": null,
        "squidclamav": null
      },
      rspamdSince: 0,
      squidclamavSince: 0
    };
  },
  methods: {
    getDashboardData() {
      var ctx = this;
      nethserver.exec(
        ["nethserver-antonio/dashboard/read"],
        null,
        null,
        function(success) {
          success = JSON.parse(success);
          ctx.antonioAppName = success.appName;
          ctx.uiLoaded = true;
        },
        function(error) {
          ctx.showErrorMessage(ctx.$i18n.t("dashboard.error_getting_dashboard_data"), error)
        }
      );
    },
  }
};
</script>

<style>
.row {
  padding-left: 20px;
  padding-right: 20px;
}

.mg-top-minus-7 {
  margin-top: -7px;
}
</style>
