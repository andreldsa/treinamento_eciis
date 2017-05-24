
function User(data) {
    data = data || {};
    _.extend(this, data);
}

User.prototype.addList = function(list) {
    this.lists.push(list);
}

User.prototype.delList = function(index) {
    this.lists.splice(index, 1);
}


function List(data) {
    data = data || {};
    _.extend(this, data);
}

List.prototype.addTask = function(task) {
    this.tasks.push(task);
}

List.prototype.delTask = function(taskId) {
    _.remove(this.tasks, function(task) {
        return task == taskId;
    });
}


function Task(data) {
    data = data || {};
    _.extend(this, data);
}

Task.prototype.changePriority = function(priority) {
    if(_.includes(['high', 'medium', 'low'], priority)){
        this.priority = priority;
    }
}

Task.prototype.changeStatus = function() {
    this.done = !this.done;
}


