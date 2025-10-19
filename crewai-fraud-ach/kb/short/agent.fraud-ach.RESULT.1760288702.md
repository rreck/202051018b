```json
{
  "id": "8d84c47f5300b637",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288702,
  "host_pid": "9e6742732c60:1",
  "hash": "bdf4d3577303abc568084cfe0a275807ff4c70a5e4a181577f6bfb26cbbb40d0",
  "cid": "QmV1bdf4d3577303abc568084cfe0a275807ff4c70a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288702,
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
      "evaluated_at": 1760288702
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
  "sig": "d104e8a9dca656e2f2e159bf05a4942da1d56418e87158bb1e17826731e7d0fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 12524808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}