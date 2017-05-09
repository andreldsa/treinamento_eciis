(function() {
  'use strict';

  var app = angular
    .module('panelGroupsDemo', ['ngMaterial'])

    app.config(function($mdIconProvider) {
        //setup($mdIconProvider);
        $mdIconProvider.fontSet('md', 'material-icons');
    });

    app
    .controller('PanelGroupsCtrl', PanelGroupsCtrl)
    .controller('PanelMenuCtrl', PanelMenuCtrl);

  function PanelGroupsCtrl($mdPanel) {

      console.log($mdPanel)

    this.settings = {
      name: 'settings',
      items: [
        'Home',
        'About',
        'Contact'
      ]
    };
    this.favorite = {
      name: 'favorite',
      items: [
        'Add to Favorites'
      ]
    };
    this.more = {
      name: 'more',
      items: [
        'Account',
        'Sign Out'
      ]
    };
    this.tools = {
      name: 'tools',
      items: [
        'Create',
        'Delete'
      ]
    };
    this.code = {
      name: 'code',
      items: [
        'See Source',
        'See Commits'
      ]
    };

    this.menuTemplate = '' +
        '<div class="menu-panel" md-whiteframe="4">' +
        '  <div class="menu-content">' +
        '    <div class="menu-item" ng-repeat="item in ctrl.items">' +
        '      <button class="md-button">' +
        '        <span>{{item}}</span>' +
        '      </button>' +
        '    </div>' +
        '    <md-divider></md-divider>' +
        '    <div class="menu-item">' +
        '      <button class="md-button" ng-click="ctrl.closeMenu()">' +
        '        <span>Close Menu</span>' +
        '      </button>' +
        '    </div>' +
        '  </div>' +
        '</div>';

    $mdPanel.create('toolbar', {
      maxOpen: 2
    });

    $mdPanel.create('menus', {
      maxOpen: 3
    });

    this.showToolbarMenu = function($event, menu) {
      var template = this.menuTemplate;
      console.log("Teste")
      var position = $mdPanel.newPanelPosition()
          .relativeTo($event.srcElement)
          .addPanelPosition(
            $mdPanel.xPosition.ALIGN_START,
            $mdPanel.yPosition.BELOW
          );

      var config = {
        id: 'toolbar_' + menu.name,
        attachTo: angular.element(document.body),
        controller: PanelMenuCtrl,
        controllerAs: 'ctrl',
        template: template,
        position: position,
        panelClass: 'menu-panel-container',
        locals: {
          items: menu.items
        },
        openFrom: $event,
        focusOnOpen: false,
        zIndex: 100,
        propagateContainerEvents: true,
        groupName: ['toolbar', 'menus']
      };

      $mdPanel.open(config);
    };

    this.showContentMenu = function($event, menu) {
      var template = this.menuTemplate;

      var position = $mdPanel.newPanelPosition()
          .relativeTo($event.srcElement)
          .addPanelPosition(
            $mdPanel.xPosition.ALIGN_START,
            $mdPanel.yPosition.BELOW
          );

      var config = {
        id: 'content_' + menu.name,
        attachTo: angular.element(document.body),
        controller: PanelMenuCtrl,
        controllerAs: 'ctrl',
        template: template,
        position: position,
        panelClass: 'menu-panel-container',
        locals: {
          items: menu.items
        },
        openFrom: $event,
        focusOnOpen: false,
        zIndex: 100,
        propagateContainerEvents: true,
        groupName: 'menus'
      };

      $mdPanel.open(config);
    };
  }

  function PanelMenuCtrl(mdPanelRef) {
    this.closeMenu = function() {
        console.log("Passou aqui!")
      mdPanelRef && mdPanelRef.close();
    }
  }

  function setup($mdIconProvider) {
      $mdIconProvider.fontSet('md', 'material-icons')
  }
})();