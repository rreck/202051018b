```json
{
  "id": "e7b47f090e0d3777",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287614,
  "host_pid": "9e6742732c60:1",
  "hash": "875d05d86b6b892b0b9c822766169a63da60559eb02413b06be90d29f0197001",
  "cid": "QmV1875d05d86b6b892b0b9c822766169a63da60559e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287614,
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
      "evaluated_at": 1760287614
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
  "sig": "53a3875d0ed2de71017426f6b4ead6025ff1b234e4660251e9d3a6ff23e24843"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 122105152922139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 13198152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': '36c7f170a3aff02c'}}}