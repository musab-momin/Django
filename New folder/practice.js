// const Heros = [
//     {
//         name : 'Iron man',
//         powers : 'Money and Mind'
//     },
//     {
//         name : 'Captain America',
//         powers : 'Super Strength and Humbleness'
//     }
// ]


// const addHero = (cb)=>{
//     setTimeout(()=>{
//         Heros.push({ name: 'Thor', powers: 'Greek Thunder GOD' })
//         cb()
//     }, 2000)
// }


// const printHeros = (cb)=>{
//     setTimeout(()=>{
//         Heros.forEach(ele=>console.log(`${ele.name} : ${ele.powers}`))
//     }, 1000)
// }

// addHero(printHeros)


// const Heros = [
//     {
//         name : 'Iron man',
//         powers : 'Money and Mind'
//     },
//     {
//         name : 'Captain America',
//         powers : 'Super Strength and Humbleness'
//     }
// ]

// const addHero = ()=>{
//     return new Promise((resolve, reject)=>{
//         if(true){
//             setTimeout(()=>{
//                 Heros.push({ name: 'Thor', powers: 'Greek Thunder GOD' })
//                 resolve()
//             }, 2000)
            
//         }else{
//             reject()
//         }
//     })
// }

// addHero().then(()=>{
//     setTimeout(()=>{
//         Heros.forEach(ele=>console.log(`${ele.name} : ${ele.powers}`))
//     }, 1000)
// })

// const Heros = [
//     {
//         name : 'Iron man',
//         powers : 'Money and Mind'
//     },
//     {
//         name : 'Captain America',
//         powers : 'Super Strength and Humbleness'
//     }
// ]

// const addHero = ()=>{
//     return new Promise((resolve, reject)=>{
//         if(true){
//             setTimeout(() => {
//                 Heros.push({ name: 'Thor', powers: 'Greek Thunder GOD' })
//                 resolve()
//             }, 2000);
//         }else{
//             reject()
//         }
//     })
// }

// async function printHero(){
//     await addHero();
//     setTimeout(()=>{
//         Heros.forEach(ele=>console.log(`${ele.name} : ${ele.powers}`))
//     }, 1000)
// }

// printHero()


//find the second largest element in array

// function findSecondLargest(arr){
//     let first = 0, second = 0

//     for(let i of arr){
//         if (i > first){
//             second = first
//             first = i
//         }
//         if( i < first && i > second ){
//             second = i
//         }
//     }
//     console.log(second)

// }

// const arr = [35, 12, 84, 58, 64, 75, 57, 42, 34]
// findSecondLargest(arr)

// function findSecondLargest(arr){
//     let first = 0, second = 0;

//     for (let i of arr)
//         if(i > first) first = i
    
//     for (let j of arr){
//         if(j > second && j < first) second = j
//     }

//     console.log(first, second)

// }
// const arr = [35, 12, 84, 58, 64, 75, 57, 42, 34]
// findSecondLargest(arr)

// function printObj(...args){
//     console.log(this.name, ' : ', this.occupation, args)
// }

// const obj = {
//     name : 'Musab Momin',
//     occupation : 'Web Developer'
// }


// printObj.apply(obj, ['Learning new things', 'how wourld you access this second args'])
// printObj.call(obj)


// const firstPromise = (()=>{
//     return new Promise((resolve, reject)=>{
//         if(true){
//             setTimeout(()=>{
//                 resolve()
//             }, 1000)
//         }
//     })
// })

// firstPromise().then(()=>console.log('Hope is a good thing.'))



// const secondPromise = (()=>{
//     return new Promise((resolve, reject)=>{
//         if(true){
//             setTimeout(()=>{
//                 resolve()
//             }, 2000)
//         }
//     })
// })

// secondPromise().then(()=>console.log('have it and move on.'))

// Promise.all([firstPromise(), secondPromise()]).then(()=>console.log('Youll get all your answers just like this'))

// pollyfill for call() method

// Function.prototype.myCall = function(context){
//     context.myCb = this
//     context.myCb()
//     // console.log(context.myCb())
// }

// function printObj(){
//     console.log(this.name, this.occupation)
// }

// const obj = {
//     name : 'Musab Momin',
//     occupation: 'Web Developer'
// }

// printObj.myCall(obj)


// Function.prototype.myApply = function(context, remainder){
//     context.myFunction = this
//     context.myFunction(remainder)
// }


// function printObj(arr){
//     console.log(this.name, this.occupation, arr)
// }
// const obj = {
//     name : 'Musab Momin',
//     occupation: 'Web Developer'
// }

// printObj.myApply(obj, ['this is working...'])


// Promise.all = (promises)=>{
//     return new Promise((resolve, reject)=>{
//         let resovlePromises = [];
//         let rejectePromises = [];

//         promises.forEach((promise, index)=>{
//             promise.then(res=>{
//                 resovlePromises.push(res)

//                 if(index === promises.length - 1){
//                     if(rejectePromises.length > 0)
//                         reject(rejectePromises)
//                     else
//                         resolve(resovlePromises)
//                 }
//             }).catch(err=>{
//                 rejectePromises.push(err)
//                 reject(rejectePromises)
//             })
//         })
//     })
// }

// let p1 = Promise.resolve('Promise one resolved')
// let p2 = new Promise((resolve, reject)=>{
//     setTimeout(function(){
//         if(true)
//             resolve('Second promise gets resolved after 2 second')
//         else
//             reject('sorry second promise is not fullfiled')
        
//     }, 2000)
// })

// Promise.all([p1, p2]).then((resolved)=>{
//     resolved.forEach(promise=>console.log(promise))
//     console.log('All Promises gets resolved')
// })


// Function.prototype.myBind = (obj)=>{
//     func = this
//     return function(){
//         func(obj)
//     }
// }


// const cb = printObj.myBind(obj)
// cb()

// Function.prototype.myCall = function(context, ...args){
//     context.myFunc = this
//     context.myFunc(args)
// }


// Function.prototype.myApply = function(context, arr){
//     context.cb = this
//     context.cb(arr)
// }

// const printObj = function(args){
//     console.log(this.name, this.occupation, args)
// }

// const obj = {
//     name : 'Musab Momin',
//     occupation : 'Web Developer',
// }

// printObj.myCall(obj, 'Mumbai', 'India')

// printObj.myApply(obj, ['this is working..'])

// printObj.call(obj)


// Function.prototype.myBind = function(context, ...args){
//    context.cb = this
//    return function(){
//     context.cb(...args)
//    }
// }

// const obj = {
//     name : 'Musab Momin',
//     occupation : 'Web Developer',
// }

// const printObj = function(state, country){
//     console.log(this.name, this.occupation, state, country)
// }

// const fb = printObj.myBind(obj, "Mumbai", "Maharashtra")
// fb()