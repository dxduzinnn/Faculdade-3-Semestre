function rodar() {
    const simbolos = ["🍒", "🍋", "🍉", "⭐", "💎"];

    let s1 = simbolos[Math.floor(Math.random() * simbolos.length)];
    let s2 = simbolos[Math.floor(Math.random() * simbolos.length)];
    let s3 = simbolos[Math.floor(Math.random() * simbolos.length)];

    document.getElementById("slot1").textContent = s1;
    document.getElementById("slot2").textContent = s2;
    document.getElementById("slot3").textContent = s3;

    let resultado = document.getElementById("resultado");

    if (s1 === s2 && s2 === s3) {
        resultado.textContent = "🎉 JACKPOT! Você ganhou!";
    } else {
        resultado.textContent = "😢 Tente novamente!";
    }
}
