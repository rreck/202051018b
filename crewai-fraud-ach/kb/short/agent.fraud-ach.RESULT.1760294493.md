```json
{
  "id": "4a10150f65e4d0bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294493,
  "host_pid": "9e6742732c60:1",
  "hash": "a424abf52a41c9d0b77e2655f2a35cba614c07e2b9c84aca3682168c15a9ce66",
  "cid": "QmV1a424abf52a41c9d0b77e2655f2a35cba614c07e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294493,
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
      "evaluated_at": 1760294493
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
  "sig": "eecdd2eb31f30ddec26f6b7551fe7b9f97e95f1fdade07212c01a21be757755e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151550703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 91453350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': '1af10bcd1b5a60d5'}}}