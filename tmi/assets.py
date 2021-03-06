from flask.ext.assets import Bundle

from tmi.core import assets

js_assets = Bundle(
    'vendor/angular/angular.js',
    'vendor/angular-route/angular-route.js',
    'vendor/angular-animate/angular-animate.js',
    'vendor/angular-contenteditable/angular-contenteditable.js',
    'vendor/angular-truncate/src/truncate.js',
    'vendor/angular-bootstrap/ui-bootstrap.js',
    'vendor/angular-bootstrap/ui-bootstrap-tpls.js',
    'vendor/angular-loading-bar/build/loading-bar.js',
    'js/app.js',
    filters='uglifyjs',
    output='assets/app.js'
)

css_assets = Bundle(
    'style/app.less',
    filters='less',
    output='assets/style.css'
)

assets.register('js', js_assets)
assets.register('css', css_assets)
