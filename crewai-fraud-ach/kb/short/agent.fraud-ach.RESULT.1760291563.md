```json
{
  "id": "cb8a5fdae390f2c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291563,
  "host_pid": "9e6742732c60:1",
  "hash": "d8561ee32b132d5c1231041e921b343eed06e8c4f68772e157aefc1fae803ff6",
  "cid": "QmV1d8561ee32b132d5c1231041e921b343eed06e8c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291563,
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
      "evaluated_at": 1760291563
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
  "sig": "c13d88b70dd3dfd15a1eda04139c97e3c567645679b05084124f92180eb8630f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028270724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': 'c4ee7f0f971d402b'}}}een': 1760285763, 'matching_hash': '3f378333472d9dcb'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}