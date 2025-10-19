```json
{
  "id": "f9d982f4fb4a42b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287969,
  "host_pid": "9e6742732c60:1",
  "hash": "a03d79f67ff13c77edb38085d3e489b245ed866de130d1aeb2db626ba654dc2c",
  "cid": "QmV1a03d79f67ff13c77edb38085d3e489b245ed866d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287969,
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
      "evaluated_at": 1760287969
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
  "sig": "097147b28fdf08a6f18eb396cf7148496111bf5cb9740db256aefc486d06711c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245911336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 38827308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': '6e0081c3975eda61'}}}