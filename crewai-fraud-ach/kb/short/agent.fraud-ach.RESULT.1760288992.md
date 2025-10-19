```json
{
  "id": "90d64fa4d6d2eec0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288992,
  "host_pid": "9e6742732c60:1",
  "hash": "0a6176e0ecbd04e495fa97eb6620fe1a42bfcb73489a453fba02283be72a6de6",
  "cid": "QmV10a6176e0ecbd04e495fa97eb6620fe1a42bfcb73",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288992,
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
      "evaluated_at": 1760288992
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
  "sig": "edab958de8d08e7b40980cf8343bd6f0bc9aca0ad73b010fbad04e552f50742c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 78379284, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}