```json
{
  "id": "24e1e97f244d791a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292589,
  "host_pid": "9e6742732c60:1",
  "hash": "bca3050f2395c5d9f99432d98b3e2a80b4262c2acd2d039adb2a08fa12767583",
  "cid": "QmV1bca3050f2395c5d9f99432d98b3e2a80b4262c2a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292589,
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
      "evaluated_at": 1760292589
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
  "sig": "e6a239aef856767fdcc91baa55b65c8cd289b7e52e7aa16575a4b35900cce702"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027962561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 10050000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}