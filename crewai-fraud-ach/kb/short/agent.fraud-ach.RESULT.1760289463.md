```json
{
  "id": "4a8733f1d8dcd752",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289463,
  "host_pid": "9e6742732c60:1",
  "hash": "dff588b43eb8b81d5730e7348dc22af3d00900dba6d4f91b2f8ec315ed365af5",
  "cid": "QmV1dff588b43eb8b81d5730e7348dc22af3d00900db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289463,
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
      "evaluated_at": 1760289463
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
  "sig": "ffcce570927b69877a24e770baf5c1aad6eda5fde562456bf864e7696ac2cd02"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219972
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 60631412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '09b5d296b49f9602'}}}