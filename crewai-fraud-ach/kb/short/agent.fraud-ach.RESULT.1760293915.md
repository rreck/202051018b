```json
{
  "id": "2cc98df2637c4012",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293915,
  "host_pid": "9e6742732c60:1",
  "hash": "e85831e1934adfd141eb6c33a8975a5489dded1a0bd42c683318c67052e10dc2",
  "cid": "QmV1e85831e1934adfd141eb6c33a8975a5489dded1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293915,
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
      "evaluated_at": 1760293915
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
  "sig": "1dfad76044cca2881bc774ac455160825e5b4cf98c32bcdc41d3821501ca9bbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463677078
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 11400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '2c78ec7dacd934fb'}}}