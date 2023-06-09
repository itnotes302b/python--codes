const { assert } = require("chai")

const TodoList = artifacts.require('./TodoList.sol')
contract('TodoList',(account)=> {
    before(async()=>{
        this.todoList = await TodoList.deployed()
    })
    it('deploys sucessfully ',async ()=>{
        const adress = await this.todoList.adress
        assert.notEqual(adress,0x0)
        assert.notEqual(adress,'')
        // assert.notEqual(adress,null)
        // assert.notEqual(adress,undefined)
    })

    it('lists task ',async()=>{
        const taskCount = await this.todoList.taskCount()
        const task = await this.todoList.tasks(taskCount)
        assert.equal(task.id.toNumber(),taskCount.toNumber())
        assert.equal(task.content,"check out nullblocks.xyz")
        assert.equal(task.completed,false)
        assert.equal(taskCount.toNumber(),1)
    })

    it('creates task',async()=> {
        const result = await this.todoList.createTask('A new task')
        const  taskCount = await this.todoList.taskCount()
        assert.equal(taskCount,2)
        // console.log(result)
        const event = result.logs[0].args
        assert.equal(event.id.toNumber(),2)
        assert.equal(event.content,'A new task')
        assert.equal(event.completed,false)
    })

    it('toggles task completion',async()=>{
        const result = await this.todoList.toggleCompleted(1)
        const  task = await this.todoList.tasks(1)
        assert.equal(task.completed,true)
        const event = result.logs[0].args
        assert.equal(event.id.toNumber(),1)
        assert.equal(event.completed,true) 
    })

})
