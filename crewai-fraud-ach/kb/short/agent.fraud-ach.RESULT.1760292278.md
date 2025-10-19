```json
{
  "id": "024ed1791e6e175b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292278,
  "host_pid": "9e6742732c60:1",
  "hash": "41af1c30a15c63f46c26664e967554f82de342017ba7765a92cefc259a7ef7ec",
  "cid": "QmV141af1c30a15c63f46c26664e967554f82de34201",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292278,
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
      "evaluated_at": 1760292278
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
  "sig": "851d1969dabb0e028ffb0ddaf0d106fc8b5f19450d5d872ac330afcd8157072e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039514582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 61843514, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'c5d30db04a2c4cc4'}}}