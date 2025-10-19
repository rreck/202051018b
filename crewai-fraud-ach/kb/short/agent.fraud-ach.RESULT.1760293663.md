```json
{
  "id": "c96ec015de2cae7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293663,
  "host_pid": "9e6742732c60:1",
  "hash": "69f296bba0d2df774e6fa2aeb4122b8f0be09e09590ccc77370ad7b7290864fc",
  "cid": "QmV169f296bba0d2df774e6fa2aeb4122b8f0be09e09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293663,
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
      "evaluated_at": 1760293663
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
  "sig": "dccff73377aa42d4e30bd842cc14cd3e5235ea5d007651db22507a2f4b7f2877"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150369382
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 79791184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '1d04175be49b6deb'}}}