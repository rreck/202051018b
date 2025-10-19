```json
{
  "id": "c03813a8370b60dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294299,
  "host_pid": "9e6742732c60:1",
  "hash": "9878e6c63294aa89e697121fcc486f9d2babdc6a778b1ca33d2c98c35983cbe7",
  "cid": "QmV19878e6c63294aa89e697121fcc486f9d2babdc6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294299,
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
      "evaluated_at": 1760294299
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
  "sig": "b02effe86904b9963ea4690b1544769f0541627549a42757ada8e0ccd0a74b33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 101267845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}