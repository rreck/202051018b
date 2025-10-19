```json
{
  "id": "691eb6159ac2ad06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290839,
  "host_pid": "9e6742732c60:1",
  "hash": "a01501b831120ff9fc0bddf3dc67244fd0c50eb92e5d92a93cd5ac9732046efe",
  "cid": "QmV1a01501b831120ff9fc0bddf3dc67244fd0c50eb9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290839,
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
      "evaluated_at": 1760290839
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
  "sig": "9ea76775ac15ea39bbae55911a6cd276ec76a586c3c7f14ed91cce29ffdf4c59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 50919680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}