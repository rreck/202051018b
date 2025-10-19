```json
{
  "id": "a32db837839b9ed1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294301,
  "host_pid": "9e6742732c60:1",
  "hash": "27ac116019e7690599f519506a0d3eb15bccb024e323ab88358f43d96e82d48e",
  "cid": "QmV127ac116019e7690599f519506a0d3eb15bccb024",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294301,
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
      "evaluated_at": 1760294301
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
  "sig": "2c9874e2532f3523d3cf8d6808a89f46d9b700be8069a634d97e61b6a1b3db0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463787734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 75506675, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': 'c4d507dbbdae18b2'}}}