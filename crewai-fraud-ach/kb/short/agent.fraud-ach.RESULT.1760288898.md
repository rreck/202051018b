```json
{
  "id": "6020cae08bd6abd2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288898,
  "host_pid": "9e6742732c60:1",
  "hash": "c3e4b22cb5a1b6b04756b2b90eb97c0fa04d4e3e2bd7484afca938e6cf9f1d6b",
  "cid": "QmV1c3e4b22cb5a1b6b04756b2b90eb97c0fa04d4e3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288898,
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
      "evaluated_at": 1760288898
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
  "sig": "da24d2a1ba1601e06446e33d5cfe3f442c3cdae4765d537e07c3b6fa0d96e3f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245748791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 21354204, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': 'b01b0e655b1e1c55'}}}