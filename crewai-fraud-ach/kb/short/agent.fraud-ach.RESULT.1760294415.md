```json
{
  "id": "b3a503eb60db3e99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294415,
  "host_pid": "9e6742732c60:1",
  "hash": "a28dd3ca7628213ae12426d0db7d83b6ef34ac6542c05dd45ef338acad55fe72",
  "cid": "QmV1a28dd3ca7628213ae12426d0db7d83b6ef34ac65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294415,
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
      "evaluated_at": 1760294415
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
  "sig": "f118ea3212eea45d63110ded099029d09d2fb68649bf2b458007442e18be1e27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 38610381, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}