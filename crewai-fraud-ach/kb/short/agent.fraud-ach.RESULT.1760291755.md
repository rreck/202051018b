```json
{
  "id": "1397b7e981d976ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291755,
  "host_pid": "9e6742732c60:1",
  "hash": "8109810f6fccac6b810fa79cce64331ab3a884e34ea8b6ec00cbdb9deaddd81c",
  "cid": "QmV18109810f6fccac6b810fa79cce64331ab3a884e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291755,
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
      "evaluated_at": 1760291755
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
  "sig": "858c6c6d3a2a769346b2bb7b80a18c7fea0483d6662b37ed0dbc4ffe8e9b9981"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 62072556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}