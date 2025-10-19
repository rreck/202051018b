```json
{
  "id": "d443c5f99189da25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289678,
  "host_pid": "9e6742732c60:1",
  "hash": "5d2c8329c966f58f658fcf2f3f8580dfb04fb485195c28503dfd426909b3af83",
  "cid": "QmV15d2c8329c966f58f658fcf2f3f8580dfb04fb485",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289678,
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
      "evaluated_at": 1760289679
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
  "sig": "ddd6e4f60bb0445dc02c21ef4039aa28cdaeba800dc830338bc4f7405898ea08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020626056
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 13000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': 'ca4ea9492786d8a3'}}}