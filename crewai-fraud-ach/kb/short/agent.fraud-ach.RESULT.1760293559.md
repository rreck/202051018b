```json
{
  "id": "633940c077811212",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293559,
  "host_pid": "9e6742732c60:1",
  "hash": "292f83ff67ef20c82096168bf2af1aad18a1f6dd3334a318048420efac5637c3",
  "cid": "QmV1292f83ff67ef20c82096168bf2af1aad18a1f6dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293559,
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
      "evaluated_at": 1760293559
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
  "sig": "f6d959d010afbfdcd17cd4fd90c741f64d1d5ab434279e8b72e432b02f59b141"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278849424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 63311859, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '586e1ac2088494e1'}}}