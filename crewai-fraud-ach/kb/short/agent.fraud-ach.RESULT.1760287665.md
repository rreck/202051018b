```json
{
  "id": "a50ac9971e4ee848",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287665,
  "host_pid": "9e6742732c60:1",
  "hash": "fdee27da91a60c3a69b06c3eb7200e6f3ac40220bf244a334d63d82b7c93b581",
  "cid": "QmV1fdee27da91a60c3a69b06c3eb7200e6f3ac40220",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287665,
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
      "evaluated_at": 1760287665
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
  "sig": "665367f2ec855d32f0fa4a46588d2439e98f34cb479415eadee89c2a58eae585"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}t_seen': 1760284979, 'matching_hash': 'aab4f056297a675d'}}}ting_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}