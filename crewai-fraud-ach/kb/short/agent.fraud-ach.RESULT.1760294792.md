```json
{
  "id": "56ea5a0385ae294f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294792,
  "host_pid": "9e6742732c60:1",
  "hash": "aa0c94612d944a8f9e8ea6687b9764cd4410bbd6f32a5603d2264c8c58922b4c",
  "cid": "QmV1aa0c94612d944a8f9e8ea6687b9764cd4410bbd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294792,
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
      "evaluated_at": 1760294792
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
  "sig": "dbef0df89d14e99c151756410f1115c8ce4d23b50da0f42a1e4fda000508f6cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 48060192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}