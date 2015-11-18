var app = angular.module('Alchemy', ['ngMaterial', 'ngMdIcons']);

app.config(function($mdThemingProvider) {
	$mdThemingProvider.theme('default')
		.primaryPalette('blue')
		.accentPalette('pink');
});

