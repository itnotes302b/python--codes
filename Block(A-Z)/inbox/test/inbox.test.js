const assert = require('assert');
const ganache = require('ganache-cli');
const Web3 = require('web3'); //capital 'Web3' means it is a constructor 
const web3 =  new Web3(ganache.provider()); //here we make instance of 'Web3' , provider just like telephone who communicate network with web3 


let accounts;
beforeEach(async ()=>{
    // Get a list of all account 
    /* web3.eth.getAccounts()   
    .then(fetchedAccounts =>{
        console.log(fetchedAccounts);
    }) */
    accounts = await web3.eth.getAccounts();

});

describe('inbox',()=>{
    it('deploys a contarct',()=>{
        console.log(accounts)
    });
});

/* 
example of mocha 
class Car {
    park(){
        return 'stopped';
    }
    drive(){
        return 'vroom';
    }
}

let car ; //gloabl varible decalre  
//beforeEach it run and initilaise car
beforeEach(()=>{
    car = new Car();
});

describe('Car blha blha',()=> {
    it('It can park  ',()=>{
        // const car = new Car();
        assert.equal(car.park(),'stopped');
    });
    it('can drive ',()=>{
    //    const car = new Car();
       assert.equal(car.drive(),'vroom'); 
    });
});
*/
