```json
{
  "id": "9b8e4e4162b686cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287432,
  "host_pid": "9e6742732c60:1",
  "hash": "aaf6a0190bd54a3622f9e92ada808854b1080b5bc4d75a5d4e925026ed388a3c",
  "cid": "QmV1aaf6a0190bd54a3622f9e92ada808854b1080b5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287432,
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
      "evaluated_at": 1760287432
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "565cfd8023759e85055c48965e2a14e36d90d984ae4f8c04657a4aad34ce96eb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000022959454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}een': 1760285763, 'matching_hash': '36d51f87c7d176f1'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7493680}}}