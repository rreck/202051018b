```json
{
  "id": "5c30f4fa618820af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292743,
  "host_pid": "9e6742732c60:1",
  "hash": "967beca8fca1546e361ad5c60906598d4fad8655ea32ebcc35e894c6e7d12895",
  "cid": "QmV1967beca8fca1546e361ad5c60906598d4fad8655",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292743,
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
      "evaluated_at": 1760292743
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
  "sig": "4f0a3f8eb5f7c1f961869a6202e9c7f0e6e26ac1f8688fb2ee6a227e1300b543"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595557022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 97100124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': '3443c05f2ecc9733'}}}