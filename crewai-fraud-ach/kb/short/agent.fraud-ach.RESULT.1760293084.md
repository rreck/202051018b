```json
{
  "id": "f20729b2fb056a81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293084,
  "host_pid": "9e6742732c60:1",
  "hash": "f8fa32d2cc36dcaf7a36765dd5114ca3d338dbf286bbaf23e8ff47beb5cac2b8",
  "cid": "QmV1f8fa32d2cc36dcaf7a36765dd5114ca3d338dbf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293084,
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
      "evaluated_at": 1760293084
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
  "sig": "599ce28c0dcb17fc9dd0db5115fb7ac6485434398124d0f581636ad9bb7029d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027931714
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 57410779, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': 'e2e3d7aa40c6ad9f'}}}