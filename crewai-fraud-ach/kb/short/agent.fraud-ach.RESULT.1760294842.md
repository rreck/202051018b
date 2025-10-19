```json
{
  "id": "f9ededff31b3c82f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294842,
  "host_pid": "9e6742732c60:1",
  "hash": "e98225ae95ef1d1f940b8cf5adbbb29eda11e0dc17ed012f2ebfaf13e903ed61",
  "cid": "QmV1e98225ae95ef1d1f940b8cf5adbbb29eda11e0dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294842,
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
      "evaluated_at": 1760294842
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
  "sig": "49fd705569571e66a2c45513ede380dbb7d72c660583d589e10e4f77fb9cd814"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033181833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 91641025, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '52cd22d87934f676'}}}