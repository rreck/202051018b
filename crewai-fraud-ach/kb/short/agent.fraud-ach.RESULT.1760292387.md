```json
{
  "id": "cac5c5cd64f7884c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292387,
  "host_pid": "9e6742732c60:1",
  "hash": "923cd7d746855b3524a02ce8d1ae288360e31df01753bf119bead6d44d905ea6",
  "cid": "QmV1923cd7d746855b3524a02ce8d1ae288360e31df0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292387,
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
      "evaluated_at": 1760292387
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
  "sig": "55fb82f29db7acfb63b8310b6ae7c72d9b9be79e2b867fb141432ab85a4cf97f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 89922644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}