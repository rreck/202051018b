```json
{
  "id": "cea4f6018d8c5795",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285913,
  "host_pid": "9e6742732c60:1",
  "hash": "659a9ffc33be72d3fd2db84766a6a5b1f4056c1b5c22ca42ea3e78b25e0c900f",
  "cid": "QmV1659a9ffc33be72d3fd2db84766a6a5b1f4056c1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285913,
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
      "evaluated_at": 1760285913
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
  "sig": "03b9b40129336e374a2d375cea95a89b0c8a40daafad3aae3f2249443e5636e1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241330040
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}