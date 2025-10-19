```json
{
  "id": "db794f509fa36f0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286491,
  "host_pid": "9e6742732c60:1",
  "hash": "e05ebaf5cbbb16f2ae03d762a1486b20c43ca5a9338096b5317314644290351c",
  "cid": "QmV1e05ebaf5cbbb16f2ae03d762a1486b20c43ca5a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286491,
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
      "evaluated_at": 1760286491
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
  "sig": "383c0f4b4ba99cf0dd4ba33d3f0ba59f9dc34150c7320f8736f7d2d27c455334"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598551005
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10129428, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': 'f05e3d2f96782052'}}}