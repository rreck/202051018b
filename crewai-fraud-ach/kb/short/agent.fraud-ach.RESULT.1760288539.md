```json
{
  "id": "80490d051adf0330",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288539,
  "host_pid": "9e6742732c60:1",
  "hash": "fa811197de215c744838bb2c1287363ec6dde671910de2cc58fa9caecc26aa74",
  "cid": "QmV1fa811197de215c744838bb2c1287363ec6dde671",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288539,
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
      "evaluated_at": 1760288539
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
  "sig": "650c9fbc14a6bc8fb9d28ae9180ca3b3d8c98a2f9f63a5e22e52b0ffaa7eea2b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466004729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 27384672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}