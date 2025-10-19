```json
{
  "id": "f9c5223b006a8b21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292573,
  "host_pid": "9e6742732c60:1",
  "hash": "d493bab2c6b2b95187a03cfe80643e5741a8399a4fcd4fc3403222894bc2dff4",
  "cid": "QmV1d493bab2c6b2b95187a03cfe80643e5741a8399a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292573,
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
      "evaluated_at": 1760292573
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
  "sig": "88201b660adc7cfcf3aa91489ae0ce26874104fbbe6c413d067f3aec133dc8cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 13305800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}