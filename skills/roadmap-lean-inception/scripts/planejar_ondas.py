#!/usr/bin/env python3
"""Compõe ondas que respeitam as seis regras de Lean Inception.

Uso: python scripts/planejar_ondas.py epicos.json
O resultado JSON vai para stdout; erros e inviabilidade geram exit code 1.
"""

import itertools
import json
import sys
from functools import lru_cache


def solve(payload):
    items = payload.get("epicos")
    if not isinstance(items, list) or not items:
        raise ValueError("Forneça uma lista não vazia em 'epicos'.")
    if len(items) > 22:
        raise ValueError("Limite de 22 épicos por execução; divida a análise em lotes e preserve dependências.")

    ids = [x.get("id") for x in items]
    if not all(isinstance(x, str) and x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError("Cada épico precisa de id de texto único.")
    indices = {value: i for i, value in enumerate(ids)}
    deps = []
    for epic in items:
        for field in ("usuario", "negocio", "esforco"):
            if type(epic.get(field)) is not int or epic[field] not in (1, 2, 3):
                raise ValueError(f"{epic['id']}: {field} deve ser 1, 2 ou 3.")
        conf = str(epic.get("confianca", "")).lower()
        if conf not in ("vermelho", "amarelo", "verde"):
            raise ValueError(f"{epic['id']}: confiança deve ser vermelho, amarelo ou verde.")
        epic["confianca"] = conf
        references = epic.get("depende_de", [])
        if not isinstance(references, list):
            raise ValueError(f"{epic['id']}: depende_de deve ser uma lista.")
        if any(d not in indices or d == epic["id"] for d in references):
            raise ValueError(f"{epic['id']}: dependência inexistente ou circular consigo mesmo.")
        deps.append(sum(1 << indices[d] for d in references))

    all_mask = (1 << len(items)) - 1

    def valid_wave(group):
        if len(group) > 3 or len(group) < 2:
            return False
        selected = [items[i] for i in group]
        return (
            sum(x["usuario"] for x in selected) >= 4
            and sum(x["negocio"] for x in selected) >= 4
            and sum(x["esforco"] for x in selected) <= 5
            and sum(x["confianca"] == "vermelho" for x in selected) <= 1
            and (len(selected) < 3 or any(x["confianca"] == "verde" for x in selected))
        )

    @lru_cache(None)
    def search(completed):
        if completed == all_mask:
            return ()
        ready = [i for i in range(len(items)) if not completed & (1 << i) and deps[i] & completed == deps[i]]
        candidate_groups = []
        for size in (2, 3):
            for group in itertools.combinations(ready, size):
                if valid_wave(group):
                    candidate_groups.append(group)
        # Prefer high combined value per effort and lower uncertainty, but backtrack if needed.
        candidate_groups.sort(key=lambda g: (
            -sum(items[i]["usuario"] + items[i]["negocio"] for i in g) / sum(items[i]["esforco"] for i in g),
            sum(items[i]["confianca"] == "vermelho" for i in g),
            -len(g),
            tuple(ids[i] for i in g),
        ))
        for group in candidate_groups:
            mask = sum(1 << i for i in group)
            continuation = search(completed | mask)
            if continuation is not None:
                return (group,) + continuation
        return None

    result = search(0)
    if result is None:
        return {"status": "inviavel", "motivo": "Nenhuma divisão de todos os épicos satisfaz simultaneamente as seis regras. Rever agrupamento, divisão dos épicos ou premissas com o PM.", "epicos": ids}

    waves = []
    for number, group in enumerate(result, 1):
        selected = [items[i] for i in group]
        waves.append({
            "onda": number,
            "epicos": [x["id"] for x in selected],
            "valor_usuario": sum(x["usuario"] for x in selected),
            "valor_negocio": sum(x["negocio"] for x in selected),
            "esforco_tecnico": sum(x["esforco"] for x in selected),
            "confianca": [x["confianca"] for x in selected],
        })
    return {"status": "viavel", "ondas": waves}


def main():
    if len(sys.argv) != 2:
        print("Uso: planejar_ondas.py epicos.json", file=sys.stderr)
        return 2
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as handle:
            payload = json.load(handle)
        result = solve(payload)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["status"] == "viavel" else 1
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"status": "erro", "motivo": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
