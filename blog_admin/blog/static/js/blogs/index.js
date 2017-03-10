(function(node) {
    var $node = $(node);

    //dom
    var $blog;
    var parseDom = function() {
        $blog = $node.find('.js-desc');
    }
    var bindLinstener = function() {

    };
    var initPlugins = function() {
        console.log($blog)
    };
    var init = function() {
        parseDom();
        bindLinstener();
        initPlugins();
    };
    init();
}('.js-blogs'));
