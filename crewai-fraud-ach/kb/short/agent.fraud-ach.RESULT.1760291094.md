```json
{
  "id": "b2aca6c667d2c216",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291094,
  "host_pid": "9e6742732c60:1",
  "hash": "253a71b55795a8336a6c4681bb750cc995481716db923e93ef2aa01606e1f5c2",
  "cid": "QmV1253a71b55795a8336a6c4681bb750cc995481716",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291094,
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
      "evaluated_at": 1760291094
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
  "sig": "25b1062e03a144d96b207f99519446c1bcbab9914d6137096ab9abb58d922436"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460168239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 13738923, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'c8b812a49265f53e'}}}