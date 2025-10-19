```json
{
  "id": "ada32cc0a69967e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293172,
  "host_pid": "9e6742732c60:1",
  "hash": "bb85cd39f2415a2d96a5d9dc19803c62f6ee0bdbde16e26a385b4fb3a3c21fc9",
  "cid": "QmV1bb85cd39f2415a2d96a5d9dc19803c62f6ee0bdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293172,
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
      "evaluated_at": 1760293172
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
  "sig": "661ff17527f5bfc9f560ce5a51b6126fe479461e1b0f8a3460b6116dcabf7ceb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024487889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 88025445, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285764, 'matching_hash': '1280efea2d0c7f9c'}}}