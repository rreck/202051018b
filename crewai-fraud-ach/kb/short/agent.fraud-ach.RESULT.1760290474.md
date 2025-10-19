```json
{
  "id": "b6db193d95d2462e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290474,
  "host_pid": "9e6742732c60:1",
  "hash": "0d80e7d882a8474d3706bde1e54494f092c538a374e38ac60363878e47106732",
  "cid": "QmV10d80e7d882a8474d3706bde1e54494f092c538a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290474,
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
      "evaluated_at": 1760290474
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
  "sig": "87afe34b8deea62c80db5563e48a9aa49704a50e9629c8eec5ed7e46f6ecef52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467837924
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 14938581, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '256da828ea708baa'}}}