```json
{
  "id": "6b524dc6afdcce92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288758,
  "host_pid": "9e6742732c60:1",
  "hash": "04a8b930795602db45385d0d668a215531f3b8caec2792fb17acebc75441f33d",
  "cid": "QmV104a8b930795602db45385d0d668a215531f3b8ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288758,
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
      "evaluated_at": 1760288758
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
  "sig": "111fdf983e2d4f05fd61e8a07eae3c4d2aaa0d60f3d282b2862668a6ec2d9a71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597950940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 27440951, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': 'cd3d42208c2780a3'}}}