```json
{
  "id": "a6a9838ea665d253",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289396,
  "host_pid": "9e6742732c60:1",
  "hash": "f2f350b97d4e15add29b02fed444a12eb6bc90c7ac44056c6fcaa59ac23d4e98",
  "cid": "QmV1f2f350b97d4e15add29b02fed444a12eb6bc90c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289396,
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
      "evaluated_at": 1760289396
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
  "sig": "c44f8c8dbae6f2071ec44f5caadd5c5fd2435507fe493c8cda40592db44ffd65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 53642180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}