```json
{
  "id": "15874cd9bc5ad22c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290215,
  "host_pid": "9e6742732c60:1",
  "hash": "98d14a5a570f71630b8d9c363c51e8081df0e861095d6cae4f18ff4f566c71d1",
  "cid": "QmV198d14a5a570f71630b8d9c363c51e8081df0e861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290215,
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
      "evaluated_at": 1760290215
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
  "sig": "a363103f32a6a237d3b06a37d823b77a45814bd99961801536f4051558debf57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462765128
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 43429392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': 'e332841741f2145e'}}}