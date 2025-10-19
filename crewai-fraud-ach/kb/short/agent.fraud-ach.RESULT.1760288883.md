```json
{
  "id": "cfd1940c872f8766",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288883,
  "host_pid": "9e6742732c60:1",
  "hash": "bfdecc4cab245e2ec0ae025591a7981a96f273d4cf08d15aa51f84fdb1bf1d2d",
  "cid": "QmV1bfdecc4cab245e2ec0ae025591a7981a96f273d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288883,
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
      "evaluated_at": 1760288883
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
  "sig": "b46caad5de7e0d8adead1f57cdfb0dbfec82e0c4b8ba38aeeac85200e3ab66ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157761036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': '6f087e4012bb31a6'}}}