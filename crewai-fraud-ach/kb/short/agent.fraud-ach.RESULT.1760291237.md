```json
{
  "id": "e1b6304ab5e7065d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291237,
  "host_pid": "9e6742732c60:1",
  "hash": "98a8bceb9e7ca85a8c948f668128679e457c92f6905d91f9fc946766f30b9722",
  "cid": "QmV198a8bceb9e7ca85a8c948f668128679e457c92f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291237,
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
      "evaluated_at": 1760291237
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
  "sig": "f15dfa4a6307718ce2dac923ae87e39870ffa3d3e2b611801cf2c56766800c2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 58588590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}