```json
{
  "id": "d0151c3de1e2031f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290012,
  "host_pid": "9e6742732c60:1",
  "hash": "b6bab247218ef27da1bd1e10bc6b5490391927be7a1a4dd9e5e5ac5d1eda9abd",
  "cid": "QmV1b6bab247218ef27da1bd1e10bc6b5490391927be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290012,
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
      "evaluated_at": 1760290012
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
  "sig": "bf14b81c0f9120adc6e2c5559bfa6a7ae06e5027f4c0661dacff9a3b1522d8de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 37313021, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}