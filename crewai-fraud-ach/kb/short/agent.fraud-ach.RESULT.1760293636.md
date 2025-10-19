```json
{
  "id": "2b47cb2e4be7ed99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293636,
  "host_pid": "9e6742732c60:1",
  "hash": "09be8b659b2ac4f6af469af8d001ea7fa20b74029d7349d6c70bcb38193bf61d",
  "cid": "QmV109be8b659b2ac4f6af469af8d001ea7fa20b7402",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293636,
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
      "evaluated_at": 1760293636
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
  "sig": "093868930962fa2ee1b24b12ac553dec188ea229caaf805c293f24b77dc2a8d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243232456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 74095608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': '1b0a7dc1f650d378'}}}