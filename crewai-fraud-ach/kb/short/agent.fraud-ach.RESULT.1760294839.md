```json
{
  "id": "d412c1b32a590511",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294839,
  "host_pid": "9e6742732c60:1",
  "hash": "917d016bbe347b2e83270e34ad3645150f8a8d52d222a2e5682109875011f54f",
  "cid": "QmV1917d016bbe347b2e83270e34ad3645150f8a8d52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294839,
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
      "evaluated_at": 1760294839
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
  "sig": "bd7afae1bd9e1485e02ac0d54e67c5663c2e355f43d9aa6c03627736d3a206ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 62345150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}