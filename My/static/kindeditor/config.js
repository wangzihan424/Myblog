KindEditor.ready(function (K) {
    window.editor = K.create('textarea[name=blog_content]', {
        width: '700px',
        height: '200px',
        uploadJson: '/admin/upload/kindeditor',
    })
})