```json
{
  "id": "791e5cf60b74cba9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294336,
  "host_pid": "9e6742732c60:1",
  "hash": "3ff78f2a269142a637f0d12e643b12bf13172740ea7c27f889574536553bb73c",
  "cid": "QmV13ff78f2a269142a637f0d12e643b12bf13172740",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294336,
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
      "evaluated_at": 1760294336
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
  "sig": "40427d923147993a8a5d665ca69c33e9b9e7c22f7e34af3220fd269796d7b8e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039514582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 75232316, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'c5d30db04a2c4cc4'}}}