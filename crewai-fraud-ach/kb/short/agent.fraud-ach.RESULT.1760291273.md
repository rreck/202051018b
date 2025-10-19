```json
{
  "id": "2ac5b35a918991c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291273,
  "host_pid": "9e6742732c60:1",
  "hash": "9da6d23817c508ac2a8f8311e7d90534c0985c3db318d436c49421607e6b1b06",
  "cid": "QmV19da6d23817c508ac2a8f8311e7d90534c0985c3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291273,
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
      "evaluated_at": 1760291273
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
  "sig": "222b7547bafea4d28d190472db9bd230f5af0d29cb4a3990f1e0e9ca6c8e4c36"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021479776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 39421656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '6c002fd60c3e5dde'}}}