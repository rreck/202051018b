```json
{
  "id": "13352c468efc9dc9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289906,
  "host_pid": "9e6742732c60:1",
  "hash": "01ed59e8d1ed65af760adf2eaeedcbd4796ce453429c65f0b8e45659c60083ba",
  "cid": "QmV101ed59e8d1ed65af760adf2eaeedcbd4796ce453",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289906,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289906
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "52d18ec8e4aa64180ef5904b758effba06a93522fefa0c0f6480c164ed63226c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 20925096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}