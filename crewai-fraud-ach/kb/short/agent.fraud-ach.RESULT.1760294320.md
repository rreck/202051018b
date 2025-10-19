```json
{
  "id": "92c55a8c8c806e08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294320,
  "host_pid": "9e6742732c60:1",
  "hash": "56129d7abee9fe2c22414b9fed0e012b041ad0f13187aadfdcc7bfecff318ac7",
  "cid": "QmV156129d7abee9fe2c22414b9fed0e012b041ad0f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294320,
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
      "evaluated_at": 1760294320
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
  "sig": "c6b1dba5329a0bc18ca6cedb3b1dc721e69f0610a84d47e5519a0dca95f74f52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030232602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 14237880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}