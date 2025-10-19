```json
{
  "id": "333d56657407fe88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294891,
  "host_pid": "9e6742732c60:1",
  "hash": "23906b2f0dfdfb5695caf4505af4bc4eaa3df093ca2ec0c2498ee53999dcf6c7",
  "cid": "QmV123906b2f0dfdfb5695caf4505af4bc4eaa3df093",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294891,
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
      "evaluated_at": 1760294891
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
  "sig": "ec542fc1a31cb13493c5423f81b4c36fb5968a5e6277b3ad00e477b66ce45914"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593702879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 48560646, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '1b01d510f5fcfc0c'}}}