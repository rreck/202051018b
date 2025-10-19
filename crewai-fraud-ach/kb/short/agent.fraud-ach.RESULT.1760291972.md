```json
{
  "id": "86990550f3d5b46b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291972,
  "host_pid": "9e6742732c60:1",
  "hash": "473d310d324ebeea90798b193845b097b1972f6c27c0eeaf1051fd5fc906e00f",
  "cid": "QmV1473d310d324ebeea90798b193845b097b1972f6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291972,
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
      "evaluated_at": 1760291972
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
  "sig": "d9c6705cd55e3750b94f587222880caf7cdf944414c74bd1e0c02f873dad4f7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027229959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 81216905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'f31e697a4f515fbb'}}}