export const loadTodoList = "loadTodoList";
export const successTodoList = "successTodoList";
export const failTodoList = "failTodoList";
export const errorTodoList = "errorTodoList";
export const resetTodoList = "resetTodoList";

export const loadTodoDetail = "loadTodoDetail";
export const successTodoDetail = "successTodoDetail";
export const failTodoDetail = "failTodoDetail";
export const errorTodoDetail = "errorTodoDetail";
export const resetTodoDetail = "resetTodoDetail";

const createTodo = constructorConstant("createTodo")

function constructorConstant(name: string){
    return {
        "load": `load_${name}`,
        "success": `success_${name}`,
        "fail": `fail_${name}`,
        "error": `error_${name}`,
        "reset": `reset_${name}`
    }
}