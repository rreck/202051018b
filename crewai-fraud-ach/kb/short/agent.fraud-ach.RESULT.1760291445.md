```json
{
  "id": "8554b4ebf9a119db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291445,
  "host_pid": "9e6742732c60:1",
  "hash": "f57612d75b144ac843359480d880c24c9900c9de2dece5e247e66f335b74c662",
  "cid": "QmV1f57612d75b144ac843359480d880c24c9900c9de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291445,
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
      "evaluated_at": 1760291445
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
  "sig": "04c826a0a1f3336b500d48be438bad83dfbdb8c9df825176f1d326926acba054"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022462179
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 71019375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': 'b017d6ab8abfffc0'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '442437646', 'validation_error': 'Invalid routing number checksum'}}}