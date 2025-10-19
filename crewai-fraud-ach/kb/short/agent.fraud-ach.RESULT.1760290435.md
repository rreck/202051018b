```json
{
  "id": "a9c95f26cf166ca0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290435,
  "host_pid": "9e6742732c60:1",
  "hash": "3e514c9a7397a13352689c1db0061a5c0665f1f9201c87de199491f09eaa5f02",
  "cid": "QmV13e514c9a7397a13352689c1db0061a5c0665f1f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290435,
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
      "evaluated_at": 1760290435
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
  "sig": "73819160b1df2c39320633c4727720c58ec5dcef44f61ba2a4e30585f3edf17f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241978752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 33540450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '600b54b59692179b'}}}