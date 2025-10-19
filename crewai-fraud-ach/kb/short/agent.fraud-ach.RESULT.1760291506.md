```json
{
  "id": "9e0646d1936a5223",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291506,
  "host_pid": "9e6742732c60:1",
  "hash": "5fe794b7b36ef135f13256cc9df767a0161db6fb22818585421f242e6d3074e8",
  "cid": "QmV15fe794b7b36ef135f13256cc9df767a0161db6fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291506,
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
      "evaluated_at": 1760291506
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
  "sig": "43d119cfe0f068d4330aabd5dfbb6fdd3eace0b6806a514dc102ec5b8de80e82"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 56011648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}