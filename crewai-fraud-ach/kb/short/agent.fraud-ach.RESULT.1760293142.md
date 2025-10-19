```json
{
  "id": "a2db521b6e0a3783",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293142,
  "host_pid": "9e6742732c60:1",
  "hash": "f191e475d3a1c5252b979a0ffaede4b1ee78901a741a0a826096bb557bf252d9",
  "cid": "QmV1f191e475d3a1c5252b979a0ffaede4b1ee78901a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293142,
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
      "evaluated_at": 1760293142
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
  "sig": "089493cb986611ea63304c3b2ea8e138d6f63c54278411721736156501db5fcf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 24120936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}