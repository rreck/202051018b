```json
{
  "id": "3a54b17e4c62aa3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292209,
  "host_pid": "9e6742732c60:1",
  "hash": "9a33cfdc7ed33a5d9366f312a22f02272f27a784cb0a950a5095b665d045265c",
  "cid": "QmV19a33cfdc7ed33a5d9366f312a22f02272f27a784",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292209,
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
      "evaluated_at": 1760292209
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
  "sig": "6b8e414837b25a1179b7c6ca1e4af2780efad64c9c2eaa67aec13e25533cb5b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 61103616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}