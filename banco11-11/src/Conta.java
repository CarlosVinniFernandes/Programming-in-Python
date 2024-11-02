public class Conta {
    protected int numeroConta;
    protected double saldo;
    
    public Conta(int numeroConta) {
        this.numeroConta = numeroConta;
        this.saldo = 0.0;
    }

    public Conta(){
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void depositar(double valor){
        saldo += valor;
        System.out.println("Você adicionou R$" + valor + " agora sua conta tem R$" + getSaldo());
    }

    public void sacar(){
    }

    
}
