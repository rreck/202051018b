```json
{
  "id": "d19f195b999e9d3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287877,
  "host_pid": "9e6742732c60:1",
  "hash": "507f789c1c25a1bfa73e35bcc9dffe1a15e8df1631764f6cd0e069c6064fdc20",
  "cid": "QmV1507f789c1c25a1bfa73e35bcc9dffe1a15e8df16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287877,
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
      "evaluated_at": 1760287877
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
  "sig": "6e55bb3e725361da95ba1fcbc53d2eeb40f73036b69c9bd88357832874bc088f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246033311
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 35990250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285764, 'matching_hash': 'd9b4b01f0add79d3'}}}