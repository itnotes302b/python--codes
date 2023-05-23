App={
  loading:false,
  contracts : {},
  load : async() => {
      //Load app 
      console.log("app loading ... ")
      await App.loadWeb3()
      await App.loadAccount()
      await App.loadContract()
      await App.render()
    },
  
      // https://medium.com/metamask/https-medium-com-metamask-breaking-change-injecting-web3-7722797916a8
  loadWeb3: async () => {

    if (typeof web3 !== 'undefined') {
      App.web3Provider = web3.currentProvider
      web3 = new Web3(web3.currentProvider)
    } else {
      window.alert("Please connect to Metamask.")
    }
    // Modern dapp browsers...
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccounts(accounts);
      } catch (error) {
        if (error.code === 4001) {
          // User rejected request
        }
        // console.log(error);
        // setError(error);
      }
    }
    
    //  if (window.ethereum) {
    //   window.web3 = new Web3(ethereum)
    //   try {
    //     // Request account access if needed
    //     await ethereum.enable()
    //     // Acccounts now exposed
    //     web3.eth.sendTransaction({/* ... */})
    //   } catch (error) {
    //     setError("Unable to connect to Metamask");

    //     // User denied account access...
    //   }
    // }
    
    // Legacy dapp browsers...
    else if (window.web3) {
      App.web3Provider = web3.currentProvider
      window.web3 = new Web3(web3.currentProvider)
      // Acccounts always exposed
      web3.eth.sendTransaction({/* ... */})
    }
    // Non-dapp browsers...
    else {
      console.log('Non-Ethereum browser detected. You should consider trying MetaMask!')
    }
  },

  loadAccount:async() => {

    //all below comments are methos don't work to retrive adress 
    // App.account = web3.eth.account[0];
    // web3.eth.requestAccounts().then(console.log);


    // web3.eth.getAccounts().then(e => let firstAcc=e[0]);
    // console.log(firstAcc)) ;  
    // console.log(App.account)

    // var myacc = await web3.eth.getAccounts().then(function(acc){ accounts = acc })
    // console.log(myacc[0])

    // const myAccounts = await web3.eth.getAccounts();
    // console.log(myAccounts +"asds") //undefined

      /* this is how to load accc new , proper way to this */
      const account = await window.ethereum.request({ method: 'eth_requestAccounts' });
      //set current blockchain account 
      App.account = account
      console.log(App.account)
      console.log(account[0]);
  },
  loadContract: async ()=>{
    //Create JS version of smart contarct 
    const todoList = await $.getJSON('TodoList.json')
    App.contracts.TodoList = TruffleContract(todoList)
    App.contracts.TodoList.setProvider(App.web3Provider)
    // console.log(todoList)
    
    //Hydarate the smart contarct with values from the bloackchain
    App.todoList = await App.contracts.TodoList.deployed()
  },
  render: async()=>{
    //prevent double loading
    if(App.loading){
      return
    }
    //update app loading state
    App.setLoading(true)
    // render account 
    $('#account').html(App.account)

    //render task 
    await App.renderTask()
    //update loading state 
    App.setLoading(false)

  },
renderTask :async ()=>{
  //Load the total task count from the blockchain 
  const taskCount = await App.todoList.taskCount()
  const $taskTemplate = $('.taskTemplate')
  //Render out reach task with a new task template 
  for (var i = 1; i<= taskCount;i++){
    //fetch the task data from the blockchain 
    const task = await App.todoList.tasks(i)
    const taskId = task[0].toNumber()
    const taskContent = task[1]
    const taskCompleted = task[2]

    //create the html for the task 
    const $newTaskTemplate = $taskTemplate.clone()
    $newTaskTemplate.find('.content').html(taskContent)
    $newTaskTemplate.find('input')
                    .prop('name',taskId)
                    .prop('checked',taskCompleted)
                    .on('click',App.toggleCompleted)

    //put the task in the correct list 
    if(taskCompleted){
      $('#completedTaskList').append($newTaskTemplate)
    }else{
      $('#taskList').append($newTaskTemplate)
    }

  //show the task 
    $newTaskTemplate.show()
  }
},

  createTask : async()=>{
    App.setLoading(true)
    const content = $('#newTask').val()
    await App.todoList.createTask(content)
    window.location.reload()
  },

  toggleCompleted: async (e) => {
    App.setLoading(true)
    const taskId = e.target.name
    await App.todoList.toggleCompleted(taskId)
    window.location.reload()
  },

  setLoading: (boolean) => {
    App.loading = boolean
    const loader = $('#loader')
    const content = $('#content')
    if (boolean) {
      loader.show()
      content.hide()
    } else {
      loader.hide()
      content.show()
    }
  }

}
$(() => {
  $(window).load(()=> {
    App.load()
  })
})
