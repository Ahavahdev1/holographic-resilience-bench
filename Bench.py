# -*- coding: utf-8 -*-
"""
==============================================================================
 MEA CORE — PUBLIC CLIENT VERIFICATION HARNESS (CHAOS BENCHMARK)
 Demonstração Pública de Resiliência sob Perda Física de Hardware
 Copyright (c) 2026 Bruno Loureiro Desidera. All rights reserved.
==============================================================================
"""
import os
import sys
import time
import logging

# Silencia logs internos
os.environ["GIBBERLINK_MODE"] = "local_ml"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.basicConfig(level=logging.ERROR)
for l in ["sentence_transformers", "transformers", "urllib3", "httpx", "httpcore"]:
    logging.getLogger(l).setLevel(logging.ERROR)

import numpy as np
from mea.memory import UnifiedMemoryManager, LocalMLGibberlink, HolographicQuantumMemory

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar_tela()
    print("=" * 76)
    print(" 🧬 MEA HOLOGRAPHIC CORE: PUBLIC VERIFICATION BENCHMARK")
    print("    Auditoria de Degradação Graciosa sob Perda Progressiva de Canais")
    print("=" * 76)

    # 1. Inicializa o Gerenciador e cataloga a vacina
    print("\n[+] Inicializando Kernel MEA e catalogando memória vetorial (384-D)...")
    manager = UnifiedMemoryManager()
    manager.long_term = LocalMLGibberlink()

    patogeno = "CUDA out of memory in tensor allocation"
    vacina = "torch.cuda.empty_cache(); use batch_size=16"
    manager.publish_insight(patogeno, vacina)

    vetor_puro = manager.long_term.model.encode(patogeno, convert_to_numpy=True, show_progress_bar=False)

    # 2. Inicializa o Core Holográfico Proprietário (Caixa Preta)
    holo = HolographicQuantumMemory(dimension=len(vetor_puro))
    holo.gravar_insight(vetor_puro.tolist())
    print("    -> Sinal projetado no núcleo holográfico contínuo.")

    # 3. Execução da Bateria de Testes de Estresse
    print("\n" + "=" * 76)
    print(f"{'DESTRUIÇÃO FÍSICA':<20} | {'SIMILARIDADE':<18} | {'STATUS DA MEMÓRIA':<25}")
    print("-" * 76)

    # Bateria completa: de 10% até o Apocalipse de 100%
    bateria_taxas = [0.10, 0.30, 0.50, 0.70, 0.80, 0.85, 0.87, 0.89, 0.95, 1.00]

    for taxa in bateria_taxas:
        
        vetor_rec = np.array(holo.recuperar_sob_estresse(taxa_perda_hardware=taxa), dtype=np.float32)

        # Cálculo padrão de similaridade angular
        norm_p = np.linalg.norm(vetor_puro)
        norm_r = np.linalg.norm(vetor_rec)
        sim = float(np.dot(vetor_puro, vetor_rec) / (norm_p * norm_r)) * 100 if norm_r > 0 else 0.0

        # Consulta a vacina na memória RAM
        resultado = manager.fetch_vaccines_by_vector(vetor_rec, threshold=0.50)
        
        if resultado:
            status = "✅ VIVA (Cura Resgatada)"
        elif taxa >= 1.0:
            status = "🛑 ZERO ABSOLUTO (Sem Crash)"
        else:
            status = "💀 AMNÉSIA (Ruído Térmico)"

        barra = "█" * int(sim / 5)
        print(f"{taxa*100:>5.1f}% Destruído     | {sim:>6.2f}% Similaridade | {status:<25} {barra}")
        time.sleep(0.15)

    print("=" * 76)
    print(" 👑 PROVA DE RESILIÊNCIA CONCLUÍDA: O SISTEMA NUNCA SOFRE CRASH!")
    print("=" * 76)

if __name__ == "__main__":
    main()
