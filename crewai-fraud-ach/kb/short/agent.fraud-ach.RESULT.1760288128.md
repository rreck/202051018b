```json
{
  "id": "4e1bf269f13c123f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288128,
  "host_pid": "9e6742732c60:1",
  "hash": "8a7e6d73729c7c6f459840e1b395e36b83fc54ee4a32f00a32571856c4ec4780",
  "cid": "QmV18a7e6d73729c7c6f459840e1b395e36b83fc54ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288128,
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
      "evaluated_at": 1760288128
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
  "sig": "f7f96cc89a2fda7e2790e4fba12a632548bc63a3fb8be5dd3097cf53fc010549"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 26414584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}