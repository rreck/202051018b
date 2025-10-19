```json
{
  "id": "e53bbfad6f7f32ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288851,
  "host_pid": "9e6742732c60:1",
  "hash": "f050ab1efa61ea6c8454c72ec0402f8894a1f9f48f6aeb72314fb2c7d9bdaaa6",
  "cid": "QmV1f050ab1efa61ea6c8454c72ec0402f8894a1f9f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288851,
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
      "evaluated_at": 1760288851
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
  "sig": "b01d7dba9010c16551feb331fb9a3a634ab8dbab610035176494fb25ee351afd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028760265
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 29460580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': 'ff1172b8afcaa4bc'}}}