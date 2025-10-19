```json
{
  "id": "f82e4dffc8319fba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286962,
  "host_pid": "9e6742732c60:1",
  "hash": "49819f0b5d5848196b90134d707bfbc81516494274b33a6fa8291b57e5e87692",
  "cid": "QmV149819f0b5d5848196b90134d707bfbc815164942",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286962,
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
      "evaluated_at": 1760286962
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
  "sig": "3817c31533c72ce54d775410f40eacbfa2af89d661192439500a15222635bb85"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000242634243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19268257, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285764, 'matching_hash': '8925ee68733f12e3'}}}