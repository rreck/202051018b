```json
{
  "id": "614a52a0ffc8bd01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288432,
  "host_pid": "9e6742732c60:1",
  "hash": "d50b5815d68e1b7d3cd519ae7b67b271e54360057ca5848133793a31540ab70f",
  "cid": "QmV1d50b5815d68e1b7d3cd519ae7b67b271e5436005",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288432,
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
      "evaluated_at": 1760288432
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
  "sig": "6af2149bc89a27ec79cfb66020d94d5b96d0baf7080ae9a6129ab75a79b3d279"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591273341
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': '7aa2b4ab7394d79b'}}}een': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}