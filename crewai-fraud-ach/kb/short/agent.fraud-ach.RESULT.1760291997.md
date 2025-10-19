```json
{
  "id": "7fc2f623b207b751",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291997,
  "host_pid": "9e6742732c60:1",
  "hash": "583ae0a1acf7cc70fcb2e58c164c9b23b2b7c268a2b657262c0f385cdd62c5e5",
  "cid": "QmV1583ae0a1acf7cc70fcb2e58c164c9b23b2b7c268",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291997,
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
      "evaluated_at": 1760291998
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
  "sig": "5ce60f2c6b44f958bee3438807dac192ea6df5e55964cde1e8626d50c204a4ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593402675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 40969524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '1478dad6bc2a5e7e'}}}