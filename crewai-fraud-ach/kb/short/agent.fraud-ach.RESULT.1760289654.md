```json
{
  "id": "daa9bb65b889477e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289654,
  "host_pid": "9e6742732c60:1",
  "hash": "9a11e5cdb559908d33f5e74e4e01ef40cbb1df0ac46bac8e530e8bbcc6eb5651",
  "cid": "QmV19a11e5cdb559908d33f5e74e4e01ef40cbb1df0a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289654,
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
      "evaluated_at": 1760289654
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
  "sig": "4d9986be558bfc8d80b1138441386794e6f17480dbd48ccdf4a4a5a51f483c0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 64380933, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}