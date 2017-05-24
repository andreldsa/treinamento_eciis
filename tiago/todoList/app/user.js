"use strict";
function User(data) {
    data = data || {}
    _.extend(this, data)
};

User.prototype.del_task = function(taskID) {
	_.remove(this.tasks, task => task.id === taskID);
};

User.prototype.add_task = function(task) {
    this.tasks.push(task);
};