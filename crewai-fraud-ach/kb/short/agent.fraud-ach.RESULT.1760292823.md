```json
{
  "id": "bff038d6f341b37b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292823,
  "host_pid": "9e6742732c60:1",
  "hash": "40ca956edd4ba889647b5588567d89f17e64498ccc5553948e3356ca008a2efb",
  "cid": "QmV140ca956edd4ba889647b5588567d89f17e64498c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292823,
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
      "evaluated_at": 1760292823
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "b1216547b8fa0c9acbb3d8263ba2014e89d1497ae596bebf88c8cfaf95ac9eca"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467541453
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 103000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '2d82340c3dc0e840'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}