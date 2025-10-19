```json
{
  "id": "391c5e14bea11586",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287816,
  "host_pid": "9e6742732c60:1",
  "hash": "01a8faf4b9ccc32e07f5d8271e88ef4f66b493f4bba70acfcdd0b2cc84a5b72f",
  "cid": "QmV101a8faf4b9ccc32e07f5d8271e88ef4f66b493f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287816,
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
      "evaluated_at": 1760287816
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
  "sig": "46230420b05ba87b24556a2102e02e6aab0a70ca9cd7d8ff24e15e704e138f0e"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 34488850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}