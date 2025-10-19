```json
{
  "id": "868f595045a2cb87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292051,
  "host_pid": "9e6742732c60:1",
  "hash": "54cf62ba41b76a610c42c17fe270a60f677de30e44b6c8e2b80bb2902c95bac7",
  "cid": "QmV154cf62ba41b76a610c42c17fe270a60f677de30e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292051,
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
      "evaluated_at": 1760292051
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
  "sig": "9da2590a8b59ddb99bd2b63a65490e9ea1d3faafb0d62430ad02a9203310d44f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461947560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 61093494, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': '1e39107ec95e1ca0'}}}