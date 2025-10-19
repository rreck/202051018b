```json
{
  "id": "b8883499420c4b84",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293649,
  "host_pid": "9e6742732c60:1",
  "hash": "08aa07cffe8e221fccac48f5bf56e67dba38fc0bee69cd742b7a1baa47c2d70d",
  "cid": "QmV108aa07cffe8e221fccac48f5bf56e67dba38fc0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293649,
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
      "evaluated_at": 1760293649
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
  "sig": "8bdf2cb62e61409c1b3b9b4b017ba5d68b82c10b36f10aa4bfc503f9806e42fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595927429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 32244239, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'ad7b7e4988d8fb8c'}}}