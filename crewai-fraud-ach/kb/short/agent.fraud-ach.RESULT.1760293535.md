```json
{
  "id": "c358311fb197534a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293535,
  "host_pid": "9e6742732c60:1",
  "hash": "b366de5abc34509c7df07fc52b1d3bb2affeddfc46b91767220867e25a4a3b1a",
  "cid": "QmV1b366de5abc34509c7df07fc52b1d3bb2affeddfc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293535,
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
      "evaluated_at": 1760293535
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
  "sig": "df1f4c47373326f47497bd940e4d650963968ef1c42d9cff6a829c234c612712"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279221197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 98234400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': '706f719d80b46657'}}}