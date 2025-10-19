```json
{
  "id": "412a120ca22a4a79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290283,
  "host_pid": "9e6742732c60:1",
  "hash": "e8f65e26c01ab7b95ee6d3e7e97797a650dbcde350bd4fefed3e408a676bb8fd",
  "cid": "QmV1e8f65e26c01ab7b95ee6d3e7e97797a650dbcde3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290283,
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
      "evaluated_at": 1760290283
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
  "sig": "29c3ff10722dd1c3c204ffce355caa7c1f2afdd974fd6ab94312b5da0428fe52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}