```json
{
  "id": "944f17a751dcf83c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291289,
  "host_pid": "9e6742732c60:1",
  "hash": "e0233d8b03fce61d28c8cc7661f3c972c59e0eacc1271b4143bf758a2a61e14a",
  "cid": "QmV1e0233d8b03fce61d28c8cc7661f3c972c59e0eac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291289,
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
      "evaluated_at": 1760291289
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
  "sig": "d4e5f22b1f132ddfaaefdc0290de08d23717c12900b9c1df73b4284c271e80ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 56133486, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}