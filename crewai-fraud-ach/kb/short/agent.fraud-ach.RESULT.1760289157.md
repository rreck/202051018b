```json
{
  "id": "575ffe92b6b1572e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289157,
  "host_pid": "9e6742732c60:1",
  "hash": "585f64b9a1bba1ac5ea9ad0d96edcac725d70855892f07d1717424e668e32565",
  "cid": "QmV1585f64b9a1bba1ac5ea9ad0d96edcac725d70855",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289157,
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
      "evaluated_at": 1760289157
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
  "sig": "d7035e5fb3df0122a47c5ef573c04bb36f6e361c9ac9a715dc9cb13edb4955d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 15895530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}