```json
{
  "id": "55ad68be2c303431",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288764,
  "host_pid": "9e6742732c60:1",
  "hash": "56bcd6aaf0773b61ad94b917b43aa052799d4d7a234f251648c7f311afc7259a",
  "cid": "QmV156bcd6aaf0773b61ad94b917b43aa052799d4d7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288764,
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
      "evaluated_at": 1760288764
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
  "sig": "861d09b96357af6dd5146072e03d867f1f6e2067cae235111f229ddb971acdda"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036717829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 17792117, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285764, 'matching_hash': '49d069f76f563267'}}}