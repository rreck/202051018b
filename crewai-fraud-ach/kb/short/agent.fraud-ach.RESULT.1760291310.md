```json
{
  "id": "e9222e3019fcc405",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291310,
  "host_pid": "9e6742732c60:1",
  "hash": "7ed8d0f6a7b5897972052c0024c22a6d5625f0b81e882a07b57b4e5d22700d81",
  "cid": "QmV17ed8d0f6a7b5897972052c0024c22a6d5625f0b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291310,
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
      "evaluated_at": 1760291310
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
  "sig": "be70258bcefecfeb7cd048d1f28591ca46a995d8e34e81e885678280079b22b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025853793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 46768864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': 'ff3a3f7dec7a702a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}