```json
{
  "id": "cf93e23c99db9ace",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288796,
  "host_pid": "9e6742732c60:1",
  "hash": "75a6803b5df1b137ca2eca09f1f30e3439c79a34185dee4fd07b671c02cf1506",
  "cid": "QmV175a6803b5df1b137ca2eca09f1f30e3439c79a34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288796,
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
      "evaluated_at": 1760288796
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
  "sig": "2857b0a73882e593d2ef8d012fb96c7d90bbc6d13487456d2b7ceb243f1cbaf3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025723119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 49044216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}