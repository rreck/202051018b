```json
{
  "id": "66c7c820404351cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292786,
  "host_pid": "9e6742732c60:1",
  "hash": "0f553de7e205d54b5ba3888393f92f85586014d6fed60ab423a328e73325ecf9",
  "cid": "QmV10f553de7e205d54b5ba3888393f92f85586014d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292786,
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
      "evaluated_at": 1760292786
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
  "sig": "e0218bd182a414cecc0a24b761a577522fc2d3222a2b5b0c0d7e0d27bd5bd6f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 51837735, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}