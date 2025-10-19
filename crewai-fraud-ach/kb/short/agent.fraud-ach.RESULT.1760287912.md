```json
{
  "id": "ee1d175f96abac1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287912,
  "host_pid": "9e6742732c60:1",
  "hash": "9381964427f5619ea0debfa9e22ce344571aa1ea3dcb82671cfa434dd6df6503",
  "cid": "QmV19381964427f5619ea0debfa9e22ce344571aa1ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287912,
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
      "evaluated_at": 1760287912
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
  "sig": "0e80b16a95bddf3c7688218fdef286a0709f5378e5a77dc1f0c5564dd9c763b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 19779152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}