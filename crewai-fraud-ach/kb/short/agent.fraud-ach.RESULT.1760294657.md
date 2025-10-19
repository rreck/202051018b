```json
{
  "id": "7bb7557c9e1b208b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294657,
  "host_pid": "9e6742732c60:1",
  "hash": "24e139fad841433e2aae790e508f577bb13b866d9cb1ad45eb49f701a9ffbbd7",
  "cid": "QmV124e139fad841433e2aae790e508f577bb13b866d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294657,
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
      "evaluated_at": 1760294657
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
  "sig": "796106ffdcbb8f709f3d8ca24e1e78a7497417a28a9efa2cc1907e16b24173ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031152991
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 29245458, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '75441ab8b948ac4d'}}}