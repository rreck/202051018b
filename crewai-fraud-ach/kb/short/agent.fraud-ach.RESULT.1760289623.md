```json
{
  "id": "0823577c83723395",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289623,
  "host_pid": "9e6742732c60:1",
  "hash": "759fd3a015a375a6cdd8c68b9c0632a494258074ebed1a17b8b63c5bb6e28931",
  "cid": "QmV1759fd3a015a375a6cdd8c68b9c0632a494258074",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289623,
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
      "evaluated_at": 1760289623
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
  "sig": "cfa5dedf5075e41504959f66dd1d6a6f8f25da658345d865a5245147fa6759fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 49626240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}