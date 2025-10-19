```json
{
  "id": "287d366c7aa89bff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288552,
  "host_pid": "9e6742732c60:1",
  "hash": "beba8644d1fe18651a3f59894d979877ddad6289e38dd70c007c830a43458933",
  "cid": "QmV1beba8644d1fe18651a3f59894d979877ddad6289",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288552,
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
      "evaluated_at": 1760288552
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
  "sig": "82a00aba6cf2460aa1b82a808e472da73923359a832d73b3acf469f4f6327dbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271052795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 21398976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': '457d955844db0007'}}}