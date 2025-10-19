```json
{
  "id": "239543aac8877bef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292018,
  "host_pid": "9e6742732c60:1",
  "hash": "a0cab592413e8264d27c55ce52eae43fcff003101e23e76da1a716265e1bbc4e",
  "cid": "QmV1a0cab592413e8264d27c55ce52eae43fcff00310",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292018,
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
      "evaluated_at": 1760292018
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
  "sig": "48227c2753e91fc56880ca8fc05b7602c73ee44a6a7ae500c874b85bdfb01da0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248710981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 48244748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}