```json
{
  "id": "f8adee4d309aba13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293977,
  "host_pid": "9e6742732c60:1",
  "hash": "46efa9a48be481347cd65dd4b8c5fab06f9758f8c3d3f62a5563d3d6e7ffa7e9",
  "cid": "QmV146efa9a48be481347cd65dd4b8c5fab06f9758f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293977,
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
      "evaluated_at": 1760293977
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
  "sig": "86a77ce90d984759a368f5c8304ebdb610c1d02b2728bf6014a67634a751b129"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270130572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 46803020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '3a095194dc4eaf85'}}}