```json
{
  "id": "79f4740e58753970",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294519,
  "host_pid": "9e6742732c60:1",
  "hash": "217e90c02888986213143da97b6fa12ad54a8c8a7b6dffcfe1803722267502b9",
  "cid": "QmV1217e90c02888986213143da97b6fa12ad54a8c8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294519,
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
      "evaluated_at": 1760294519
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
  "sig": "9eb2c1309a7e5994da381348feaa3ea1cc0efc09c43ae17228ca28da677f4f79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159928324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 105086627, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': 'f9e49b53b0020755'}}}