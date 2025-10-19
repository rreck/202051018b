```json
{
  "id": "3c51ad1fe3a59726",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293892,
  "host_pid": "9e6742732c60:1",
  "hash": "d03ec8da38759d823c2b1d925da754fe3d43ad9876d66b3d4e898670971f43b6",
  "cid": "QmV1d03ec8da38759d823c2b1d925da754fe3d43ad98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293892,
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
      "evaluated_at": 1760293892
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
  "sig": "15a040e4e6c1e4fa6ad6765eae988ecb907322d2e925e158c09e895d8a3f625f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 25149557, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}