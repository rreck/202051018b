```json
{
  "id": "5cc0fab69bfedeeb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286455,
  "host_pid": "9e6742732c60:1",
  "hash": "5df2639bedd5517838b1d7ebe2350bb3ad26f99489eec6d0e4e63d7190c29724",
  "cid": "QmV15df2639bedd5517838b1d7ebe2350bb3ad26f994",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286455,
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
      "evaluated_at": 1760286455
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
  "sig": "ac7bb2c51be4369814d9dc1bb3f6d2bf4270634cc05836ab9fc6cfa83c5cd7c2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278201542
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': 'ee525b8c336c7bb1'}}}