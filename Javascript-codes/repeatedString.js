// Complete the repeatedString function below.
function repeatedString(s, n) {

    let numberOfAs = 0

    if (n >= s.length) {

        let occurencesOfA = [...s].filter(letter => letter === 'a').length

        numberOfAs = Math.floor((n / s.length) * occurencesOfA)

    }

    let tailString = n % s.length

    for (let i = 0; i < tailString; i++){
        if (s[i] === 'a'){
            numberOfAs++
        }
    }

    console.log(numberOfAs)

}

repeatedString('aba', 10)