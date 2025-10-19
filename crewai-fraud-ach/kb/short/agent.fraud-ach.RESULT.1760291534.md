```json
{
  "id": "1ef093496dddf31f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291534,
  "host_pid": "9e6742732c60:1",
  "hash": "7cbff20a4f7f3fd98e7b8e04b25bcb2b1a31d192cc2c60bb7de89f52d5c29088",
  "cid": "QmV17cbff20a4f7f3fd98e7b8e04b25bcb2b1a31d192",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291534,
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
      "evaluated_at": 1760291534
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
  "sig": "4260616c8d276d094254deb60c06609f62ea22a7f61984a843d40d6e3b78aaaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279804164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 41759964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '5884f0f9ee4a893d'}}}