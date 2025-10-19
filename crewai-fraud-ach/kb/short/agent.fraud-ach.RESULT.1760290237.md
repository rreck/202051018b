```json
{
  "id": "e8b3818f657dbf3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290237,
  "host_pid": "9e6742732c60:1",
  "hash": "801978c79d3b1d9ac2e91b67723646cb1a7648cea000e768a74b150edec954e7",
  "cid": "QmV1801978c79d3b1d9ac2e91b67723646cb1a7648ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290237,
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
      "evaluated_at": 1760290237
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
  "sig": "2503dbce61838110a9023c5a80e6bd071057f1d0e5677327ed3bac27be2e425b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596367142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 65693990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '4f1a5a8d43b99e0b'}}}