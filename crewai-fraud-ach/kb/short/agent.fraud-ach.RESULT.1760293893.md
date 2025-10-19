```json
{
  "id": "5fb1aec5bffb001f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293893,
  "host_pid": "9e6742732c60:1",
  "hash": "7dbe5725c811ca08a6d6c455f04e46f9665b04a6a7acb4dd43bb1d3c62af3d62",
  "cid": "QmV17dbe5725c811ca08a6d6c455f04e46f9665b04a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293893,
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
      "evaluated_at": 1760293893
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
  "sig": "9b0530dfbe8a07b88d24a8418104261415ecbfbb1bf2ffbfccfebd5161567ebe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 72242296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}