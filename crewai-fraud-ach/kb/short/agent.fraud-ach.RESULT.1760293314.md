```json
{
  "id": "b171ddbcb129ee25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293314,
  "host_pid": "9e6742732c60:1",
  "hash": "6b3999f5d05a88fc25948e2512d8957f8ad4053aefb9ff5f8fa24964dabde3d3",
  "cid": "QmV16b3999f5d05a88fc25948e2512d8957f8ad4053a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293314,
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
      "evaluated_at": 1760293314
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
  "sig": "ff17c56de2557e5e1cc4c566615fe94049410e9e6639cb9cfdaa15af4f237f52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 73525320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}