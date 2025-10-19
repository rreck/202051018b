```json
{
  "id": "b428899e652f2b03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291995,
  "host_pid": "9e6742732c60:1",
  "hash": "4f7b167a41aba72fbba11a193370cc7010616ef5eaea288fb981574f15df1758",
  "cid": "QmV14f7b167a41aba72fbba11a193370cc7010616ef5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291995,
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
      "evaluated_at": 1760291995
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
  "sig": "589e93f3c501230001ddf25f1f8e33f31f2d0c556b2bd43a0c20fa246dbe1120"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 67652364, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}