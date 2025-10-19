```json
{
  "id": "3857cf4fcc22cf9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293831,
  "host_pid": "9e6742732c60:1",
  "hash": "fc26ff749f4a017996dc639e9909650bd209736a024635aa3555ffeb47370baf",
  "cid": "QmV1fc26ff749f4a017996dc639e9909650bd209736a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293831,
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
      "evaluated_at": 1760293831
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
  "sig": "d789ec4691b76a42f56a58225d0fe95c227fd7fdc354b726a3d14ab950c252c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154990255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 28025356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '800f0de895a214ba'}}}