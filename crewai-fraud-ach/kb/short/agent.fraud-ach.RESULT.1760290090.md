```json
{
  "id": "2fb6f63d376e3183",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290090,
  "host_pid": "9e6742732c60:1",
  "hash": "b2d7db1033f119180bb3468cd528c3365767c5d11e8a2ccf88b8d5de4db6fe94",
  "cid": "QmV1b2d7db1033f119180bb3468cd528c3365767c5d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290090,
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
      "evaluated_at": 1760290090
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
  "sig": "0c623abe942278ec360f3162b06d8df4f30dacb7b332b58e8089f4223bf6bd98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021328085
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 14991011, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760284979, 'matching_hash': 'f7c67db4baca4bf3'}}}