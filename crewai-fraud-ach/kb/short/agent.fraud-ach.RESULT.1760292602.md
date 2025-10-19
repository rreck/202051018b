```json
{
  "id": "3f1e5241a27be712",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292602,
  "host_pid": "9e6742732c60:1",
  "hash": "0abf34ff3f132cf7ce995f64e5d5e61a17ceb0abe223b5017525363cfc6f971f",
  "cid": "QmV10abf34ff3f132cf7ce995f64e5d5e61a17ceb0ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292602,
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
      "evaluated_at": 1760292602
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
  "sig": "f4854b61d4cef511d3a1b069873925849ea55e3f80549ee8e271c6f122825ab9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026169646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 59904834, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}