```json
{
  "id": "b1ae50c74e9b678f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293357,
  "host_pid": "9e6742732c60:1",
  "hash": "16a4b0f9141eb573b8a067e3b0cc6a0cbea3f4070faba73f32eeccddc9b34792",
  "cid": "QmV116a4b0f9141eb573b8a067e3b0cc6a0cbea3f407",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293357,
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
      "evaluated_at": 1760293357
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
  "sig": "6c9ae6c7b463300616977a22200db77af06933b3d095b32dea2d61858814a1ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248569332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 32286779, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}}