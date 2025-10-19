```json
{
  "id": "3e8fac7324efe5c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288495,
  "host_pid": "9e6742732c60:1",
  "hash": "047e9929e500823a44c1255d201692345557ba7814c0304aaa3d491bf72388de",
  "cid": "QmV1047e9929e500823a44c1255d201692345557ba78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288495,
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
      "evaluated_at": 1760288495
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
  "sig": "83a8afbced68cdaed6f131516bd17fa7fa40f809d52ead271646773c7e4520c7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595571766
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 46700005, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '7b9b43f48a0de4d3'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}