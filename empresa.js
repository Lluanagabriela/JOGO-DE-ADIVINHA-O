let programacao = ['Heloa',' Maria Rafaela', 'Maria Eduarda', 'Diego', 'João Victor', 'Gabriel', 'Luana', 'Thauanne', 'Aline', 'Lucas'];

let seguranca = ['Leonardo', 'Miguel', 'João Paulo', 'Rafael'];
 
// Remanejando Rafael
seguranca.pop();
programacao.push ('Rafael');

console.log('Time de programação:', programacao);
console.log('*************************')
console.log('Time de segurança:', seguranca);
console.log('*************************')

// Juntando funcionarios
let empresa = programacao.concat (seguranca)
console.log ('Todos os funcionarios da empresa:', empresa)