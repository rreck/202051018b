```json
{
  "id": "b0440aad6d6fe887",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288667,
  "host_pid": "9e6742732c60:1",
  "hash": "95eb297b86aeca7e459db1e5ce629cef41ca6b74f40ed19f580d92f0553c45cf",
  "cid": "QmV195eb297b86aeca7e459db1e5ce629cef41ca6b74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288667,
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
      "evaluated_at": 1760288667
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
  "sig": "1ed52dbcb24c26421a6dc10520c913bc26522f606dc37b7a7bd8b99912eef8e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464170386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285764, 'matching_hash': 'cc3f2cd033134006'}}}