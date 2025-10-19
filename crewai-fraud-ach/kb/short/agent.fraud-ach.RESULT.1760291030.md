```json
{
  "id": "a29a3eddd9010235",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291030,
  "host_pid": "9e6742732c60:1",
  "hash": "f12413ccf972e9596e317c995f724ea99d957768450b8236e9bb721ffdfb88c1",
  "cid": "QmV1f12413ccf972e9596e317c995f724ea99d957768",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291030,
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
      "evaluated_at": 1760291030
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
  "sig": "d0031aa969b4e0e26e7a5813097ed7e5c2ce3e9ec9b13b1e9c63ff221b83aec6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245537248
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 24122175, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': '5bdcebee79eae34d'}}}