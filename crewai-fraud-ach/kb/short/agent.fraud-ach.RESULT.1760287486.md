```json
{
  "id": "696f36046d5ec682",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287486,
  "host_pid": "9e6742732c60:1",
  "hash": "bd2ce02961785cb683e252f2dbecc2a8a95d969cee252b45e7c44790eb924cd6",
  "cid": "QmV1bd2ce02961785cb683e252f2dbecc2a8a95d969c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287486,
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
      "evaluated_at": 1760287486
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4ef23f8ecc1b708f81e08fcc6d90b6e4fa1c1a9a8c155bff256295d11c37e243"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 122105158500131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': 'd40f962f80a48e01'}}}60285763, 'matching_hash': 'bea146cfc71ce9bb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}