```json
{
  "id": "0f2275a897492f28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293660,
  "host_pid": "9e6742732c60:1",
  "hash": "b8af0fe888229fddca7e5d79c862ae92e40fe3a61d339bc71b2a04b4f0408c9d",
  "cid": "QmV1b8af0fe888229fddca7e5d79c862ae92e40fe3a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293660,
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
      "evaluated_at": 1760293660
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
  "sig": "5db9fb46c255861005c7a474c67b38c5a4ecd0266262f39300757276ff4c41e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025657387
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 70912216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '1be88e7372567f08'}}}