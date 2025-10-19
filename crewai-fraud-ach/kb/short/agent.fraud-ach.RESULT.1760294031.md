```json
{
  "id": "7a70b28ad3038250",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294031,
  "host_pid": "9e6742732c60:1",
  "hash": "046e4f807727e92474ec2a22e4f3b23c70574ef382700ec690bfc14ff9ce2594",
  "cid": "QmV1046e4f807727e92474ec2a22e4f3b23c70574ef3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294031,
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
      "evaluated_at": 1760294031
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
  "sig": "8e7581d23bef089e6ad19d5feba1e2c801185de31d5f7d33b700a861cb3dce66"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026184073
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 71810830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '5c433365b4c36f89'}}}