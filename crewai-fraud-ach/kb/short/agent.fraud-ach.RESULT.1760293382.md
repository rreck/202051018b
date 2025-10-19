```json
{
  "id": "d99e1c5a2db5ceec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293382,
  "host_pid": "9e6742732c60:1",
  "hash": "223bd9f2a191422555c5e433d9a103ebc79c9c6beba89fc0d761897d45f2b45c",
  "cid": "QmV1223bd9f2a191422555c5e433d9a103ebc79c9c6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293382,
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
      "evaluated_at": 1760293382
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
  "sig": "aaa15de7669853613f9d4c6700c3e5e461b9568f4a2794dfacb4edb20c98d78a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593077739
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 59336480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': 'dc5b0e0c6a053908'}}}