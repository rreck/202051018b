```json
{
  "id": "3f9ce8a34be84262",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290424,
  "host_pid": "9e6742732c60:1",
  "hash": "dc2329276b27af795cb048c67b3570cf17538139196e61c466f9f694169d0354",
  "cid": "QmV1dc2329276b27af795cb048c67b3570cf17538139",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290424,
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
      "evaluated_at": 1760290424
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
  "sig": "eaa2d22589fb031dc8ecf7f5917a615769a8e5244331b7968dea5c7325d72a47"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247830233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 21276150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '6844006e916a1387'}}}