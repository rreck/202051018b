```json
{
  "id": "3cde27d1b9dc6aa5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293759,
  "host_pid": "9e6742732c60:1",
  "hash": "36eeb66cc9cd6818d65697fcfa8d985dc9701da427b312e7bcba2ae0b54c4a23",
  "cid": "QmV136eeb66cc9cd6818d65697fcfa8d985dc9701da4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293759,
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
      "evaluated_at": 1760293759
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
  "sig": "e1748070f4da11195e65cd20f0c33380b36ad6c1b7b2d0c470bf90528d111184"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 59978250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}