```json
{
  "id": "202d118fb4621bcc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292275,
  "host_pid": "9e6742732c60:1",
  "hash": "9e13131664351a1a34be780bfa68facc27fd4639981abef3d6a02b4d924c5117",
  "cid": "QmV19e13131664351a1a34be780bfa68facc27fd4639",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292275,
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
      "evaluated_at": 1760292276
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
  "sig": "36f566fa15145a36e10d5b53d0d2b63dcdf12409a23e80022d0f55e2dbf1c64e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153448153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 93747978, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285764, 'matching_hash': '55db9843fa0daece'}}}