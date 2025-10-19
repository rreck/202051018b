```json
{
  "id": "9edb6eb41bbbacb7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287603,
  "host_pid": "9e6742732c60:1",
  "hash": "43757d0bef2392b384d5e6c2dcab73235cbe4a0b67fd788a9648e793430340aa",
  "cid": "QmV143757d0bef2392b384d5e6c2dcab73235cbe4a0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287603,
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
      "evaluated_at": 1760287603
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
  "sig": "2108d7ff2d726a8ba3d281740b9d4ddfadc5eb44424d0c8baa01518961c35781"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 021000024762963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285764, 'matching_hash': 'dd3a0eba0797b423'}}}een': 1760285763, 'matching_hash': '5c86a9c2afef995d'}}}