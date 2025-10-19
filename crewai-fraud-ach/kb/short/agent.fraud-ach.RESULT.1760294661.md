```json
{
  "id": "6f60c0fb5282a56d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294661,
  "host_pid": "9e6742732c60:1",
  "hash": "3c1c1e8ad11fae59fd29baaeb5e9860fcd21e08594a78a0fabc4a47ac4b7c71c",
  "cid": "QmV13c1c1e8ad11fae59fd29baaeb5e9860fcd21e085",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294661,
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
      "evaluated_at": 1760294661
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
  "sig": "0b618a4b44555e4308dcb5f1fbc55b6edaa7c5d29a66db6fc2dc4551b38c62b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274268796
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 62713574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': 'ac75b07ed83ae58c'}}}