```json
{
  "id": "660cf3991777801b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288338,
  "host_pid": "9e6742732c60:1",
  "hash": "14fb89b5ac5ac349f28c9c3e7cf84d32d1f8fc9b5211909117cf86ea8606ffa6",
  "cid": "QmV114fb89b5ac5ac349f28c9c3e7cf84d32d1f8fc9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288338,
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
      "evaluated_at": 1760288338
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
  "sig": "e1f64ce7b30fa9c6b7ae32810fccc5102b14735c49f12aad7eef4d64750cadca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 24484050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}