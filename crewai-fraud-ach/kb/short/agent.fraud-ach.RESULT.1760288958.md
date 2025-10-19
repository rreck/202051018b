```json
{
  "id": "055b3f6fc444275c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288958,
  "host_pid": "9e6742732c60:1",
  "hash": "287926dd0eac69c8685b7e702664682c13cdf07c4430c96a1f64e0e00caaef10",
  "cid": "QmV1287926dd0eac69c8685b7e702664682c13cdf07c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288958,
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
      "evaluated_at": 1760288958
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
  "sig": "f5ad278d776a95ccd202612c681cc6abc5cafa8bb1b4e8117f51ec5fc25905bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025262531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 34726310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': 'cd477724f7ce5ce7'}}}