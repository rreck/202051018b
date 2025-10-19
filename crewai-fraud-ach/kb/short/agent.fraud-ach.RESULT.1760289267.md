```json
{
  "id": "638b32934a519efd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289267,
  "host_pid": "9e6742732c60:1",
  "hash": "f0e8d2d5fdcc7152e6e1e652795aaa6efa0826d1bb9783d2bfbaac913dc199f5",
  "cid": "QmV1f0e8d2d5fdcc7152e6e1e652795aaa6efa0826d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289267,
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
      "evaluated_at": 1760289267
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
  "sig": "b16dd792bdcebc98e61883cd078403e675cf3bace76f0a3f897f8a641f66071d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598542542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 39465218, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}