```json
{
  "id": "4e29871c37f11977",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293627,
  "host_pid": "9e6742732c60:1",
  "hash": "f6a1f612400881ed3504dc3860c2da05307b596795ccca6c2544809e5f5afa4c",
  "cid": "QmV1f6a1f612400881ed3504dc3860c2da05307b5967",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293627,
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
      "evaluated_at": 1760293627
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
  "sig": "c40a5a1252f6cd117dc9e2f305464dd4e4868c9139cf0e91fbd1dca2f2b803b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245742893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 81185622, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '17d6d8b38d025182'}}}