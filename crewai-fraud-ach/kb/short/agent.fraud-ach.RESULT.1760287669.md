```json
{
  "id": "ac11c980d3bb807c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287669,
  "host_pid": "9e6742732c60:1",
  "hash": "a385e310253a37347f4036621c7b857b9cdc0a61e9a355665e8115535030c89e",
  "cid": "QmV1a385e310253a37347f4036621c7b857b9cdc0a61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287669,
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
      "evaluated_at": 1760287669
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
  "sig": "ee58119abeacc61406ccf32edb673e9840be0a980655cfbf8348e30a761c5cb8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 23100144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}