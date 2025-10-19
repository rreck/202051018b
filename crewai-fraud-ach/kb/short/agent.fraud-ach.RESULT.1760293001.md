```json
{
  "id": "3ab2d3a1d6722b7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293001,
  "host_pid": "9e6742732c60:1",
  "hash": "cea54749eb6d921cc5ff00eb650309d9156f4046b6d73ee7ca5904378d8d7ed6",
  "cid": "QmV1cea54749eb6d921cc5ff00eb650309d9156f4046",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293001,
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
      "evaluated_at": 1760293001
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
  "sig": "0a61b13cfa6eff8f7acdeef226e023dc5fc5495a31dad8b8b565b74c5fdd5b70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 50258648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}