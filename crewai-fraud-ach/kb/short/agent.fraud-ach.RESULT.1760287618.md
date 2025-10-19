```json
{
  "id": "c20cdf0a9d02c9ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287618,
  "host_pid": "9e6742732c60:1",
  "hash": "3856a0c3378964de5a80548914c84fafac52a55a1f6bc5af9891c65f381460f2",
  "cid": "QmV13856a0c3378964de5a80548914c84fafac52a55a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287618,
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
      "evaluated_at": 1760287618
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
  "sig": "e48b91d67776592c84d3e81e99b70ae26ad144a94e40231ef2c7f37caa920def"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 12999888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}