```json
{
  "id": "771881be7dcac9ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293376,
  "host_pid": "9e6742732c60:1",
  "hash": "8839aae20dedc94ecb29f356fe8f55c585ca4b572112d130e1ae8df5e5f717ed",
  "cid": "QmV18839aae20dedc94ecb29f356fe8f55c585ca4b57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293376,
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
      "evaluated_at": 1760293376
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
  "sig": "c6bb6c9bac9fe1079ea1582e0162edb33e74737b64842d0a22c1bfd388c7b1cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030330812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 43986334, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '72f4f50a1c3c0bfc'}}}