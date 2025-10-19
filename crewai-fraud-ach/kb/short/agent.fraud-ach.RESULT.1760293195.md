```json
{
  "id": "d1989a71d5e4f252",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293195,
  "host_pid": "9e6742732c60:1",
  "hash": "05f128bacb75cf7a807f0cbcb740071d8273f9aca9f6abd1c44375a560a6dadf",
  "cid": "QmV105f128bacb75cf7a807f0cbcb740071d8273f9ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293195,
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
      "evaluated_at": 1760293195
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
  "sig": "4fdbe395dd64a8b943fc2a7228b2b201f8f44edd8b215fbb867f314528bf6ae4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 82581165, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}