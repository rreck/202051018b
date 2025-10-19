```json
{
  "id": "7f82f9d10ce50d0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288139,
  "host_pid": "9e6742732c60:1",
  "hash": "6b9d9a345e09c132906f806571f826acb4e803fdff2d399a17a38cc0c5219680",
  "cid": "QmV16b9d9a345e09c132906f806571f826acb4e803fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288139,
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
      "evaluated_at": 1760288139
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
  "sig": "fb512ee17cbd29d50179152c2df862a94e9132beb9c6fb4a5174bf0d7b2df3ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272419137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 21712488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}