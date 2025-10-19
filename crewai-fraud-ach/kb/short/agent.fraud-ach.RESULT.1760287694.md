```json
{
  "id": "dc129e2abbef3b45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287694,
  "host_pid": "9e6742732c60:1",
  "hash": "f37f841144d9191b203e19ecd51ed7b5a2c70e381d2bc75520b4d6fe4e3297c6",
  "cid": "QmV1f37f841144d9191b203e19ecd51ed7b5a2c70e38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287694,
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
      "evaluated_at": 1760287694
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
  "sig": "53a64a38b10d3dbf63c921d62365a1ff4d341214c19124aedcf53f86e1df348e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157375662
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 14302075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760284979, 'matching_hash': '8218a7a652f8297c'}}}