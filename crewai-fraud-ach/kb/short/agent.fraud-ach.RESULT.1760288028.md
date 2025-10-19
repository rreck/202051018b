```json
{
  "id": "311b9977439ddc09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288028,
  "host_pid": "9e6742732c60:1",
  "hash": "436f8a333404cd270a2ff506f94a2f5736ec9358099f3eed3cb078cb6ba606a9",
  "cid": "QmV1436f8a333404cd270a2ff506f94a2f5736ec9358",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288028,
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
      "evaluated_at": 1760288028
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
  "sig": "7d0403ed6ed1a0258f0970174b436d53a98aa0cb61a1037fc1b8f4cb96e4380d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460644681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 27301040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}