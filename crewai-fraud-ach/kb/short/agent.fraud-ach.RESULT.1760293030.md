```json
{
  "id": "e8ec5d62e9f9fd4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293030,
  "host_pid": "9e6742732c60:1",
  "hash": "f3f548c93399b9d1d60d5a1c53179d7e27d9160205a82b560ec00c83d5469502",
  "cid": "QmV1f3f548c93399b9d1d60d5a1c53179d7e27d91602",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293030,
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
      "evaluated_at": 1760293030
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
  "sig": "be2303472330a013c4286882763e28b52a3e6ae35154d5089206d2d59891707d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 18564420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}