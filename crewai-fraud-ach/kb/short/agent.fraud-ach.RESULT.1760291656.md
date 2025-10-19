```json
{
  "id": "c33afc6b92a5e55e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291656,
  "host_pid": "9e6742732c60:1",
  "hash": "aec0d5f13cf0f43fea1d7a3bd88d3595bc2948d8e40ca2bd0d01f287384d90d5",
  "cid": "QmV1aec0d5f13cf0f43fea1d7a3bd88d3595bc2948d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291656,
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
      "evaluated_at": 1760291656
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
  "sig": "d25d3d94d8bf6b0f62023ecd67f612eedbbe650293d92c74d1a20d0d73118fdd"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022304560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 90000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '2db1b4b6a652c406'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}