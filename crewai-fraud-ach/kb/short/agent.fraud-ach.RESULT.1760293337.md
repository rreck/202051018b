```json
{
  "id": "1561595195c7deed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293337,
  "host_pid": "9e6742732c60:1",
  "hash": "5f73a58db9746d31951c302187a2b847f6fd2c241ff741bde25e23d1c7e2ed11",
  "cid": "QmV15f73a58db9746d31951c302187a2b847f6fd2c24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293337,
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
      "evaluated_at": 1760293337
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
  "sig": "9c102a9018183102228eeec1005e75d2a63b4d3c130a2bd38b4102f4b486f499"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039663431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 32167368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}