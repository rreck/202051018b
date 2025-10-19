```json
{
  "id": "53968248ed14d396",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291031,
  "host_pid": "9e6742732c60:1",
  "hash": "ef8372d4c46501d0aee4654a39c58d6859ea31fe46a1f7afe82e211e5da59ba2",
  "cid": "QmV1ef8372d4c46501d0aee4654a39c58d6859ea31fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291031,
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
      "evaluated_at": 1760291031
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
  "sig": "ee5a143c8f0a8f3b7f43eb109dcfba3a755d0cbaa75ab96604ed8df49f97f252"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034981344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 62666340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': '0030d58ae3a464b4'}}}