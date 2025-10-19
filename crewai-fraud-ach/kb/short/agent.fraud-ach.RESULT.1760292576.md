```json
{
  "id": "6de4dff92bd1baaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292576,
  "host_pid": "9e6742732c60:1",
  "hash": "81ca9a16f3a5f55fbc63c1ded4516486960d19be364ea3356d462ae372d5bab5",
  "cid": "QmV181ca9a16f3a5f55fbc63c1ded4516486960d19be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292576,
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
      "evaluated_at": 1760292576
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
  "sig": "5c1b5b68d735d2d08315140f09d302d97c5399b768c21cdb8e9f66618c68fd06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 63649600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}