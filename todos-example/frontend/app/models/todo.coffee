class exports.Todo extends Backbone.Model
  urlRoot: '/api/todos/'
  idAttribute: 'id'

  defaults:
    content: 'Empty todo...'
    done: no

  toggle: ->
    @save done: not @get 'done'

  clear: ->
    @destroy()
    @view.remove()
