```json
{
  "id": "5dc9a26735b8b7d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290156,
  "host_pid": "9e6742732c60:1",
  "hash": "f8e9efcc8c0b9c2508c92e084616fa9c709e5e59058753915d9d4703604ba2c2",
  "cid": "QmV1f8e9efcc8c0b9c2508c92e084616fa9c709e5e59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290156,
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
      "evaluated_at": 1760290156
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
  "sig": "22b145f1f8af1ded587d36dc03358286942f5f4371ab01ce882de0383afbbfb1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030505524
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 64274353, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285764, 'matching_hash': '58071665864a5dbb'}}}