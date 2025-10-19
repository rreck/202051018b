```json
{
  "id": "10534c36ccb2649b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293929,
  "host_pid": "9e6742732c60:1",
  "hash": "6516ffb272fa36d01a65969216698d6d2d45a3e7de50b53e7411c621c49a68da",
  "cid": "QmV16516ffb272fa36d01a65969216698d6d2d45a3e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293929,
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
      "evaluated_at": 1760293929
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
  "sig": "940c9501c45e6500dfc009d6b758344fad9ed406e8059f0254f461e3f8dfd23a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021328085
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 304, 'threshold': 50, 'total_amount': 21001232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 303, 'first_seen': 1760284979, 'matching_hash': 'f7c67db4baca4bf3'}}}