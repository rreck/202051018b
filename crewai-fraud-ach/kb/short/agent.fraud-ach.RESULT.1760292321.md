```json
{
  "id": "f318226c0c957469",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292321,
  "host_pid": "9e6742732c60:1",
  "hash": "995f82729b74ca07e44aeef09a612836d9ae3077d05f9fbcda20ef8f09136758",
  "cid": "QmV1995f82729b74ca07e44aeef09a612836d9ae3077",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292321,
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
      "evaluated_at": 1760292321
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
  "sig": "57659e05504c6307d5d98f13bbea860e3240060c4e4b9b256f3d5c40d0bf16fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158691889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 54623400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285764, 'matching_hash': '7f09a9884a1a1f0e'}}}