public class ContaPoupanca extends Conta{
    
    public ContaPoupanca(int numeroConta) {
        super(numeroConta);
    }

    public ContaPoupanca() {
    }

    public void sacar(double valor){
        valor -= valor * 0.05;
        if(valor <= saldo){
            saldo -= valor;
            System.out.println("Você sacou: R$" + valor + " e agora tem R$ " + saldo);
        }
        else{
            System.out.println("Saldo insuficiete!");
        }
    }
    
}
