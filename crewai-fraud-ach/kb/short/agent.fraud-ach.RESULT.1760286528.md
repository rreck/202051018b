```json
{
  "id": "0c4f8c1b242addc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286528,
  "host_pid": "9e6742732c60:1",
  "hash": "6cb3a8a5988848218c0ec4ee6fecff6a788b6c70dd0af73488235e302b26e346",
  "cid": "QmV16cb3a8a5988848218c0ec4ee6fecff6a788b6c70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286528,
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
      "evaluated_at": 1760286528
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "01f8a772ddd2458acc67ba8648f01fc0cf59d3ff39ba89fdd16b866c3dadccf3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105151102645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11508952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '9dd268c0fa996698'}}}