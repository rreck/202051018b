```json
{
  "id": "0e9ee77210d30b46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288594,
  "host_pid": "9e6742732c60:1",
  "hash": "b979ded553049f73271d0fc5171c107447aa260998e30ace72972ee8805938d5",
  "cid": "QmV1b979ded553049f73271d0fc5171c107447aa2609",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288594,
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
      "evaluated_at": 1760288594
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
  "sig": "a25bc0414246a8f07d9e557acccd8499912280ce37c2115db5516a0b3c0d7b71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}een': 1760285763, 'matching_hash': '1f36f93e880b57ba'}}}