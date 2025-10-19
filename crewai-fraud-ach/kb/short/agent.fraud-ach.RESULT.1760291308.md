```json
{
  "id": "6be4aeb637742320",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291308,
  "host_pid": "9e6742732c60:1",
  "hash": "f26dd6ad84e01d99df034419ba1e324a2f2ca7e6a0f63da4bdea6cef8cce9e9d",
  "cid": "QmV1f26dd6ad84e01d99df034419ba1e324a2f2ca7e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291308,
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
      "evaluated_at": 1760291308
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
  "sig": "ecca8d7cd358711fa1bd7c7dc2f78f51515e79ac909b628868d581bd5b873fc3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032979175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 56343416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '92afbef802abc12c'}}}