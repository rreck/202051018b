```json
{
  "id": "2e24b4d23309e49f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288557,
  "host_pid": "9e6742732c60:1",
  "hash": "c7d4bc16b235515bc2e58c67a62c22fe474679d56a56425d13225ec92f6c7dc6",
  "cid": "QmV1c7d4bc16b235515bc2e58c67a62c22fe474679d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288557,
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
      "evaluated_at": 1760288557
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
  "sig": "3fde7a62bf5afc8c45070679d8c4cf3515d18a2a943245a43cfe5a0edfae3b8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 43555522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}